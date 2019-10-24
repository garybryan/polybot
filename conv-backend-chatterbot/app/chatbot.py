import os

from chatterbot import ChatBot

# TODO make these safe
MONGO_DATABASE = os.environ.get('MONGO_DATABASE')
MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')

database_uri = f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@mongodb/{MONGO_DATABASE}'
chatbot = ChatBot(
    'English chatbot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=(
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
    ),
    database_uri=database_uri
)

