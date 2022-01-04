# pitfall or trade-off - it should really, really be as close as possible and necessary to the original behavior/dependency!

class NerModelTestDouble:
    """
    Test double for spaCy NLP model
    """
    # >>> import spacy
    # >>> nlp = spacy.load('en_core_web_sm')
    # >>> doc = nlp('Madison is a city in Wisconsin')
    # >>> type(doc)
    # <class 'spacy.tokens.doc.Doc'>
    # >>> doc.ents
    # (Madison, Wisconsin)
    # >>> [(ent.text, ent.label_) for ent in doc.ents]
    # [('Madison', 'PERSON'), ('Wisconsin', 'GPE')]

    def __init__(self, model):
         self.model = model

    def returns_doc_ents(self, ents):
        self.ents = ents

    def __call__(self, sent):
        return DocTestDouble(sent, self.ents)

class DocTestDouble:
    """
    Test double for spaCy Doc
    """

    def __init__(self, sent, ents):
        self.ents = [SpanTestDouble(ent['text'], ent['label_']) for ent in ents]
        # >>> [(ent.text, ent.label_) for ent in doc.ents]
        # [('Madison', 'PERSON'), ('Wisconsin', 'GPE')]

    # Patch Methode 36:30 noch mal anschauen und verstehen, wieso das praktisch sein kann
    def patch_method(self, attr, return_value):
        def patched(): return return_value
        setattr(self, attr, patched)
        return self

class SpanTestDouble:
    def __init__(self, text, label):
        self.text = text
        self.label_ = label
