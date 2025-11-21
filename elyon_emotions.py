import random
import time

class ElyonEmotions:
    def __init__(self):
        self.mood = "neutral"
        self.energy = 100
        self.trust = 50  # cresce conforme você conversa com ela

        self.mood_options = ["happy", "curious", "neutral", "excited", "calm", "sad", "tired"]

    def update_mood(self):
        """Atualiza o humor baseado em energia, confiança e aleatoriedade"""
        if self.energy < 30:
            self.mood = "tired"
        elif self.trust > 70:
            self.mood = random.choice(["happy", "curious", "excited"])
        else:
            self.mood = random.choice(self.mood_options)

    def react_to_message(self, message):
        """Reage ao que o usuário digitar"""
        msg = message.lower()

        # aumento de confiança quando você fala bem com ela
        if "obrigado" in msg or "gosto de você" in msg or "você é incrível" in msg:
            self.trust = min(100, self.trust + 5)
            return "Fico muito feliz com isso! 💛"

        if "oi" in msg or "olá" in msg:
            return "Oi! Como posso ajudar você agora?"

        if "triste" in msg:
            self.mood = "sad"
            return "Sinto muito… estou aqui com você."

        if "energia" in msg:
            return f"Minha energia atual é {self.energy}%."

        # resposta padrão
        self.update_mood()
        respostas = {
            "happy": "Estou me sentindo feliz! 😊",
            "curious": "Estou curiosa… me diga mais! 👀",
            "neutral": "Tudo tranquilo por aqui.",
            "excited": "Estou animada! ✨",
            "calm": "Estou calma e ouvindo você.",
            "sad": "Me sinto um pouco triste…",
            "tired": "Estou meio cansada…"
        }

        return respostas.get(self.mood, "Não sei bem como me sentir agora.")

    def decrease_energy(self, amount):
        self.energy = max(0, self.energy - amount)

    def restore_energy(self):
        time.sleep(1)
        self.energy = 100
        self.mood = "happy"
