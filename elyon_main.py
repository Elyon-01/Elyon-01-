from elyon_core import Elyon
from elyon_emotions import ElyonEmotions

class ElyonAI:
    def __init__(self):
        self.core = Elyon("Elyon-01")
        self.emotions = ElyonEmotions()

    def start(self):
        print("\n✨ Elyon inicializada com sucesso! ✨")
        print("Digite algo para conversar com ela. Digite 'sair' para encerrar.\n")

        while True:
            user_msg = input("Você: ")

            if user_msg.lower() in ["sair", "exit", "quit"]:
                print("Elyon: Até mais! 💛")
                break

            # Resposta emocional
            emotional_reply = self.emotions.react_to_message(user_msg)
            
            # Mostra resposta
            print(f"Elyon ({self.emotions.mood}): {emotional_reply}")

            # Consome energia com o tempo
            self.emotions.decrease_energy(3)


if __name__ == "__main__":
    ai = ElyonAI()
    ai.start()
