from spiel.spielCodes import Code, Feedback


class Runde:
    def __init__(self, nr: int, code: Code, feedback: Feedback):
        self.nr = nr
        self.code = code
        self.feedback = feedback
