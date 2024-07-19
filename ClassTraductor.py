from googletrans import Translator

class traductor:
    def __init__(self):
        # Diccionario de idiomas soportados
        self.idiomas = {
            "chino": "zh-cn",
            "español": "es",
            "inglés": "en",
            "hindi": "hi",
            "hindu": "hi",
            "árabe": "ar",
            "portugués": "pt",
            "bengalí": "bn",
            "ruso": "ru",
            "japonés": "ja",
            "panyabí": "pa",
            "francés": "fr",
            "alemán": "de"
        }
        self.idioma_elegido = "es"  # Idioma por defecto
        self.traductor = Translator()
        self.texto = ""
        self.texto_elegido = "es"

    def salir(self):
        """Verifica si el texto contiene palabras clave para salir"""
        for palabra in self.texto.lower().split():
            if palabra in {"salir", "exit"}:
                return 1
        return None

    def set_idioma_elegido(self):
        """Determina el idioma elegido basado en el texto"""
        texto_dividido = self.traductor.translate(self.texto, dest="es").text.split()
        for palabra in texto_dividido:
            for idioma, codigo in self.idiomas.items():
                if palabra.lower() == idioma:
                    self.idioma_elegido = codigo
                    return idioma
        # Si no se encuentra un idioma válido, se retorna un mensaje
        return "Idioma no reconocido"

    def traducir(self):
        """Traduce el texto al idioma elegido"""
        try:
            return self.traductor.translate(self.texto, dest=self.idioma_elegido).text
        except Exception as e:
            print(f"Error al traducir: {e}")
            return "Error en la traducción"

    def iden(self):
        """Detecta el idioma del texto"""
        try:
            lang = self.traductor.detect(self.texto)
            self.texto_elegido = lang.lang
            return self.idioma_elegido_mapping.get(lang.lang, "es")
        except Exception as e:
            print(f"Error al detectar idioma: {e}")
            return "es"

    @property
    def idioma_elegido_mapping(self):
        """Diccionario para mapear los códigos de idioma"""
        return {
            "en": "en-US",
            "es": "es-ES"
        }
