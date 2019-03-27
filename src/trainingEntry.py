class TrainingEntry:
    def __init__(self, sentence, token, lemma):
        self.sentence = sentence
        self.token = token
        self.lemma = lemma

    def __repr__(self):
        return ("{} || {} || {}".format(self.sentence, self.token, self.lemma))
