class QssHelper(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def load(file):
        with open(file, 'r') as f:
            return f.read()