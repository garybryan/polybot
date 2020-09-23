from chatterbot.trainers import ChatterBotCorpusTrainer

from chatbot import chatbot


def train(chatbot):
    trainer = ChatterBotCorpusTrainer(chatbot)
    print("Training beginning...")
    trainer.train(
        "chatterbot.corpus.english",
        "chatterbot.corpus.french",
    )
    print("Training finished")


train(chatbot)
