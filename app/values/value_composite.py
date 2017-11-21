import json


class ValueComposite(object):

    def initialize(self, value):
        self._value = value

    def serialize_with(self, **entry):
        self._value.update(entry)

    def serialize_from_value(self, value):
        self._value.update(value)

    def serialize_and_append(self, entry):
        self._value.append(entry)

    def serialize_and_append_from_value(self, value):
        self._value.append(value.raw)

    def serialize_and_append_from_values(self, values):
        self._value += map(lambda value: value.raw, values)

    def to_dict(self):
        return dict(self._value)

    @property
    def raw(self):
        return self._value

    def json(self):
        return json.dumps(self._value)