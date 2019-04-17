from pluggable import Pluggable

class Plugin(Pluggable):
    def __init__(self, *args, **kwargs):
        super(Plugin, self).__init__(*args, **kwargs)
        print("Test plugin", args, kwargs)

    def _execute(self, a, b):
        return a - b
