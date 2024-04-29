class PayloadMapping:
    def __init__(self, *, payload):
        self.payload = payload


class ProcessFileMapping(PayloadMapping):

    @property
    def type(self):
        return self.payload.get('file')

