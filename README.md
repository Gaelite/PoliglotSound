# PoliglotSound - Audio Translator

PoliglotSound is a web application that allows users to translate spoken text into multiple languages using voice recognition and automatic translation. The application is built with Flask for the web server and utilizes Python libraries for audio processing and translation.

## Description

This application allows users to select a language and speak to translate their phrases. The translation is done in real-time, and the translated text is saved in a document for future reference. Available languages include Chinese, Spanish, English, Hindi, Arabic, Portuguese, Bengali, Russian, and Japanese.

## Features

- Voice recognition to capture spoken text.
- Automatic translation of text into different languages.
- Web interface for user interaction.
- Function to save translations in a document.

## Requirements

Ensure you have Python 3.x installed on your system.

## Setting Up the Environment

1. **Clone the repository:**
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
2. **Create a virtual environment:**

  On Windows:
    -python -m venv Restore
  On macOS/Linux:
    -python3 -m venv Restore
3. **Activate the virtual environment:**
  On Windows:
    -Restore\Scripts\activate
  On macOS/Linux:
    -source Restore/bin/activate
4. **Install the dependencies:**
  pip install -r requirements.txt
5. **Running the Application**
  Start the Flask application:
    -python FlaskTrad.py

  Access the application in your browser at http://127.0.0.1:5000.

# Usage
Select the desired language by pressing the "Selected Language" button.
Press the microphone icon and speak to capture the text you want to translate.
The translation will appear in the text area.
You can transcribe all translations to a document by pressing the corresponding button in the footer.

# Dependencies
The requirements.txt file includes the following dependencies:

Flask==2.3.2
SpeechRecognition==3.10.0
pyttsx3==2.90
googletrans==4.0.0-rc1
python-docx==0.8.11
