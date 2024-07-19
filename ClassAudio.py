import speech_recognition as sr
import pyttsx3
from ClassTraductor import traductor

class audio(traductor):
    def __init__(self):
        super().__init__()
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.mic = None
        self.idioma = "es-MX"

        # Cargar voces disponibles
        self.voices = self.engine.getProperty('voices')
        self.default_voice = self.find_voice()

        # Configurar la voz por defecto
        self.engine.setProperty('voice', self.default_voice)

    def find_voice(self):
        """Encuentra y devuelve el ID de la voz apropiada basada en el idioma"""
        for voice in self.voices:
            if 'es' in voice.name:
                return voice.id
            elif 'en' in voice.name:
                return voice.id
        # Si no se encuentra una voz específica, usa la primera disponible
        return self.voices[0].id

    def set_texto(self):
        """Captura el texto del micrófono y maneja errores"""
        while True:
            try:
                self.texto = None
                with sr.Microphone() as source:
                    print("Ajustando el micrófono...")
                    self.r.adjust_for_ambient_noise(source)  # Ajustar para el ruido ambiental
                    print("Escuchando...")
                    self.mic = self.r.listen(source, timeout=5)  # Establecer un tiempo de espera para evitar bloqueos

                # Reconocimiento de voz según el idioma
                self.texto = self.r.recognize_google(self.mic, language=self.idioma)
                print(f"Texto reconocido: {self.texto}")  # Mensaje de depuración
                self.iden()  # Identificar el idioma y configurar la voz
                return self.texto  # Salir del bucle después de obtener la entrada correcta
            
            except sr.UnknownValueError:
                print(self.traductor.translate("No pude entender lo que dijiste", dest=self.texto_elegido).text)
            except sr.RequestError as e:
                print(self.traductor.translate("Error al conectarse con el servicio de reconocimiento de voz", dest=self.texto_elegido).text)
            except (AttributeError, TypeError) as e:
                print(self.traductor.translate("Puedes repetirlo por favor", dest=self.texto_elegido).text)

    def get_texto(self):
        """Obtiene el texto traducido"""
        return self.traductor.translate(self.texto, dest=self.texto_elegido).text
    
    def get_idioma(self):
        """Obtiene el idioma actual"""
        return self.idioma
    
    def hablar(self, texto):
        """Reproduce el texto usando el motor de texto a voz"""
        self.engine.say(texto)
        self.engine.runAndWait()
    
    def iden(self):
        """Identifica el idioma y configura la voz apropiada"""
        self.idioma = super().iden()
        # Configura la voz según el idioma
        self.engine.setProperty('voice', self.find_voice())

    def set_idioma_elegido(self):
        """Establece el idioma elegido por el usuario"""
        while True:
            self.set_texto()
            try:
                return super().set_idioma_elegido()
            except TypeError:
                self.set_texto()
