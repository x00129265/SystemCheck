
class Pluggable(object):
    def __init__(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        return self._execute()