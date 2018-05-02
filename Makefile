.PHONY: train

train:
	python3 -m rasa_nlu.train --config cfg/config_spacy.yml --data data/demo-rasa.json --path projects

serve:
	python3 -m rasa_nlu.server --path projects
