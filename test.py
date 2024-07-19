import speech_recognition as sr
import pyttsx3

def main():
    # Inicializar el motor de texto a voz
    engine = pyttsx3.init()
    
    # Decir "Buenos días"
    engine.say("Buenos días")
    engine.runAndWait()

    # Configurar el reconocedor de voz
    recognizer = sr.Recognizer()

    # Escuchar el micrófono
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)  # Ajustar para el ruido ambiental
        audio = recognizer.listen(source)

    # Intentar reconocer el audio
    try:
        print("Reconociendo...")
        text = recognizer.recognize_google(audio, language='es-ES')
        print("Lo que dijiste:", text)
    except sr.UnknownValueError:
        print("No pude entender lo que dijiste.")
    except sr.RequestError as e:
        print("Error al conectar con el servicio de reconocimiento de voz:", e)

if __name__ == "__main__":
    main()
