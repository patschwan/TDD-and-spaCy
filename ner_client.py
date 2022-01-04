import spacy

class NamedEntityClient:
    def __init__(self, model):
        # 1. Idea) self.model = spacy.load("en_code_web_sm") 
        # returns a callable that we can pass a string and get a document back 
        # but everytime testing  we load an external language model 
        # and while testing client we have link to that external
        # 2. Idee: wir parametrisieren model und verwenden nicht spaCy im test!
        # wir brauchen etwas dessen Verhalten wir beeinflussen können und das sich verhält, wie das Sprachmodel
        self.model = model
        pass

    def get_ents(self, sentence):
        doc = self.model(sentence)
        entities = [{ 'ent': ent.text, 'label': self.map_label(ent.label_) } for ent in doc.ents]
        return { 'ents': entities, 'html': ''}

    @staticmethod
    def map_label(label):
        label_map = {
            'PERSON': 'Person',
            'NORP': 'Group',
            'LOC': 'Location',
            'GPE': 'Location',
            'LANGUAGE': 'Language'
        }

        return label_map.get(label)