from chatterbot.trainers import ChatterBotCorpusTrainer

def train(chatbot):
    trainer = ChatterBotCorpusTrainer(chatbot)
    print("Training beginning...")
    trainer.train(
        "chatterbot.corpus.english",
    )
    print("Training finished")
