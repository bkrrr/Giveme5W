from extractor.configuration import Configuration as Config

class Candidate:
    def __init__(self):
        self._type = None
        self._raw = None
        self._score = None
        self._index = None
        self._parts = None
        self._lemma_count = None
        self._enhancement = {}
        self._calculations = {}
        self._config = Config.get()['candidate']


    def part_constructor(self, answer, score, type, ):
        re

    def get_parts(self):
        return self._parts

    def set_parts(self, parts):
        self._parts = parts

    def get_parts_as_text(self):
        answer_text = ''
        for part in self._parts:
            answer_text = answer_text + ' ' + part[0]
        return answer_text

    def set_raw(self, raw):
        self._raw = raw

    def get_raw(self):
        return self._raw

    def set_type(self, type):
        self._type = type

    def get_type(self):
        return self._type

    def set_lemma_count(self, lemma_count):
        self._lemma_count = lemma_count

    def get_lemma_count(self):
        return self._lemma_count

    def set_score(self, score):
        self._score = score

    def get_score(self):
        return self._score

    # indicated the core_nlp sentence index
    def set_sentence_index(self, index):
        self._index = index

    def get_sentence_index(self):
        return self._index

    # json representation for this candidate
    def get_json(self):

        if self._parts:
            words = []
            for part in self._parts:
                parts_json = {'text': part[0]}
                if self._config['part'].get('nlpTag'):
                    parts_json['nlpTag'] = part[1]
                words.append(parts_json)

            # nlpTag
            json = {'parts': words}
            if self._config.get('score'):
                json['score'] = self._score


            if len(self._enhancement) > 0:
                json['enhancement'] = self._enhancement

            if self._index and self._config.get('nlpIndexSentence'):
                json['nlpIndexSentence'] = self._index
            return json
        return None


    # additional information create by enhancments
    def get_enhancement(self, key):
        return self._enhancement.get(key)

    # additional information create by enhancments
    # must be writeable as json
    def set_enhancement(self, key, value):
        self._enhancement[key] = value

    def reset_enhancements(self):
        self._enhancement = {}


    # helper to decouple evaluation calculations from candidate extraction
    # use this for all evaluation related information
    # in other words store temporal information per candidate over this interface
    def get_calculations(self, key):
        return self._calculations[key]

    def set_calculations(self, key, value):
        self._calculations[key] = value

    def reset_calculations(self):
        self._calculations = {}
