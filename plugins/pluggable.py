class Pluggable(object):
    def __init__(self, *args, **kwargs):
        print("Pluggable class")

    def execute(self, a, b):
        return self._execute(a, b)