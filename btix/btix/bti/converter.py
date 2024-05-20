
class BaseConverter(object):
    def __init__(self, data, mapping, partial=False):
        data = self.before(data)
        self._partial = partial
        self._input = data
        self._history = {}
        self._mapping = mapping
        self._output = {}
        for key, value in mapping.items():
            if key in data:
                self.update(value, data.get(key))
            if hasattr(self, f'get_{key}') and ((partial is False) or (partial is True and key in data)):
                self.update(value, getattr(self, f'get_{key}')(data))
        self.after()

    @property
    def is_partial(self):
        return self._partial

    @property
    def data(self):
        return self._output

    def before(self, data):
        return data

    def after(self):
        pass

    def update(self, key, value):
        self._output.update({key: value})

    def remove(self, key):
        if key in self._output:
            self._history.update({key: self._output.pop(key)})
