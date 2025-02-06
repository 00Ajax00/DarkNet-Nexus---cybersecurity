# ml_models/nlp_entity_model.py
import spacy

class NLPEntityModel:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_entities(self, text):
        doc = self.nlp(text)
        return {ent.text: ent.label_ for ent in doc.ents}

# Usage
# model = NLPEntityModel()
# print(model.extract_entities("John works at Google in California"))
