class Elyon:
    def __init__(self, name="Elyon-01", version="1.0"):
        self.name = name
        self.version = version
        self.memory = []
        print(f"{self.name} carregado com sucesso!")
    
    def info(self):
        return {
            "name": self.name,
            "version": self.version,
            "description": "Núcleo principal do robô Elyon."
        }
    
    def speak(self, text):
        print(f"{self.name}: {text}")

elyon = Elyon()
print(elyon.info())

# Teste de fala textual
elyon.speak("Oi Raphael! Estou ativa e pronta para aprender.")
