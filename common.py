class Module(object):
    _parent = None
    @property
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self, value):
        self._parent = value
