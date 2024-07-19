# 🌐 PoliglotSound - Audio Translator

PoliglotSound is a web application that enables users to translate spoken text into multiple languages using voice recognition and automatic translation. Built with Flask for the web server, this application leverages Python libraries for audio processing and translation.

## 📋 Description

This application allows users to:
- **Select** a language and speak to translate their phrases.
- **Translate** text in real-time.
- **Save** the translated text in a document for future reference.

Available languages include:
- Chinese
- Spanish
- English
- Hindi
- Arabic
- Portuguese
- Bengali
- Russian
- Japanese
- 
**Note:** This project is my first school project. I am excited to share it and welcome any feedback or suggestions for improvement!

## ✨ Features

- 🎤 Voice recognition to capture spoken text.
- 🌍 Automatic translation of text into different languages.
- 💻 Web interface for user interaction.
- 📄 Function to save translations in a document.

## 📦 Requirements

Ensure you have Python 3.x installed on your system.

## 🛠 Setting Up the Project

1. **Clone the repository:**
      ```bash
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
   
           -Start the Flask application:
        
             -python FlaskTrad.py

  Access the application in your browser at http://127.0.0.1:5000.

## 🚀 Usage

1. Select the desired language by pressing the "Selected Language" button.
2. Press the microphone icon and speak to capture the text you want to translate.
3. The translation will appear in the text area.
4. You can transcribe all translations to a document by pressing the corresponding button in the footer.

## 📜 Dependencies

The `requirements.txt` file includes the following dependencies:

- `Flask==2.3.2`
- `SpeechRecognition==3.10.0`
- `pyttsx3==2.90`
- `googletrans==4.0.0-rc1`
- `python-docx==0.8.11`

## 💡 Open to Suggestions for Improvement

This is my first school project, and I welcome any suggestions or feedback to help improve the application. Feel free to open an issue or reach out with ideas on how to enhance the project.
