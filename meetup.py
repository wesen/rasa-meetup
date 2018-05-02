from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer

from rasa_nlu import config

def test_run():
    training_data = load_data('data/demo-rasa.json')
    trainer = Trainer(config.load('cfg/config_spacy.yml'))
    trainer.train(training_data)
    model_directory = trainer.persist('projects/python/')
    return model_directory

from rasa_nlu.model import Metadata, Interpreter

def test_interpreter(model_directory):
    interpreter = Interpreter.load(model_directory)
    interpreter.parse(u"The text I want to understand")


def foobar():
    return 10