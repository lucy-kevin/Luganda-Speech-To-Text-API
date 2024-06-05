from flask import Flask, request, jsonify
import io
import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

app = Flask(__name__)

# Load pre-trained model and processor (outside of a function for efficiency)
processor = Wav2Vec2Processor.from_pretrained("indonesian-nlp/wav2vec2-luganda")
model = Wav2Vec2ForCTC.from_pretrained("indonesian-nlp/wav2vec2-luganda")

def audio_preprocessor(audio_bytes):
    """
    Preprocesses audio data by:
        - Loading the audio data from the request.
        - Resampling the audio to 16 kHz using the resampler.
        - Converting the audio to a NumPy array and squeezing it to remove unnecessary dimensions.

    Args:
        audio_bytes (bytes): The audio data received in the request.
    Returns:
        torch.Tensor: The preprocessed audio tensor.
    """
    if not audio_bytes:
        raise ValueError("No audio data provided in the request.")

    # Load audio from bytes
    audio, sampling_rate = torchaudio.load(io.BytesIO(audio_bytes))

    if sampling_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sampling_rate, new_freq=16000)
        audio = resampler(audio)

    return audio.squeeze().numpy()

@app.route("/transcribe", methods=["POST"])
def transcribe():
    """
    Transcribes uploaded audio data using the Wav2Vec2 model.

    Returns:
        dict: A JSON response containing the predicted transcription.
    """
    if request.method != "POST":
        return jsonify({"error": "Method not allowed. Please use POST."}), 405

    # Read audio data from the request
    try:
        audio_bytes = request.files["audio"].read()
    except KeyError:
        return jsonify({"error": "Missing 'audio' field in request form."}), 400

    # Preprocess audio
    try:
        audio_array = audio_preprocessor(audio_bytes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Prepare model input
    inputs = processor(audio_array, sampling_rate=16000, return_tensors="pt", padding=True)

    # Disable gradient calculation
    with torch.no_grad():
        logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

    # Find the most likely character for each position
    predicted_ids = torch.argmax(logits, dim=-1)

    # Decode the predicted sequence
    prediction = processor.batch_decode(predicted_ids)[0]

    return jsonify({"transcription": prediction})

if __name__ == "__main__":
    app.run(debug=True)
