# Luganda Speech-to-Text API

## Inspiration
The inspiration for developing the Luganda Speech-to-Text (STT) system stemmed from the desire to bridge the communication gap faced by deaf students in Luganda-speaking communities. Recognizing the need for a tool that could transcribe spoken Luganda into text, we aimed to create a solution that enables these students to access educational content and participate fully in classroom activities.

## What It Does
The Luganda STT application transcribes spoken Luganda into text in real-time. Users can save these transcriptions for future reference, enhancing accessibility and communication for Luganda-speaking individuals, particularly in educational settings.

## How We Built It
1. **Literature Review**: We reviewed existing literature on speech-to-text systems to understand methodologies, challenges, and opportunities.
2. **System Architecture**: Designed a robust system architecture that includes a mobile application and an API.
3. **Mobile Application**: Developed a user-friendly mobile application using the Flutter framework and Dart language. The app records audio, sends it to the API for transcription, and displays the transcribed text. You can clone it from this [repo](https://github.com/lucy-kevin/Luganda-Speech-to-Text) 
4. **API Development**: Created the API using Flask, which interacts with the pre-trained [Indonesian-nlp/wav2vec2-luganda](https://huggingface.co/indonesian-nlp/wav2vec2-luganda) model to process audio data and return transcriptions.
5. **Testing**: Conducted comprehensive testing, including accuracy and usability tests, to ensure the system’s functionality and performance.

## Challenges We Ran Into
- **Communication**: Ensuring seamless communication between the mobile application and the API required significant effort.
- **Hosting Costs**: Hosting the API is quite costly, posing a challenge for scalability and sustainability.

## Accomplishments That We're Proud Of
- Successfully developed a working Luganda STT application that transcribes spoken Luganda into text.
- Empowered deaf students by providing a tool that enhances their communication and access to educational content.
- Hosting the API on an AWS EC2 instance ensures the system is scalable and reliable, capable of handling an increasing number of users.

## What We Learned
- Gained valuable experience in mobile application development using Flutter, API development with Flask, and integrating speech recognition models.
- The quality and diversity of training data are crucial for the accuracy of speech-to-text models.
- Designing user-friendly interfaces and conducting thorough testing are essential for creating tools that effectively meet users’ needs.

## Getting Started

### Prerequisites
- Python 3.7+
- Flask
- AWS account (for hosting)
- Postman

## Installation
1. Clone the repository:

```bash
git clone https://github.com/yourusername/luganda-stt-api.git
cd luganda-stt-api
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```
## Running the API
1. Start the Flask server:

```bash
flask run
```
The API will be accessible at http://localhost:5000.

## Endpoints
POST /transcribe: Accepts audio data and returns the transcribed text.
You can text is using postman software or you can just clone the App and edit the endpoints
[The Luganda Speech to text App](https://github.com/lucy-kevin/Luganda-Speech-to-Text)
```bash
curl -X POST -F 'file=@path_to_audio_file' http://localhost:5000/transcribe
```
