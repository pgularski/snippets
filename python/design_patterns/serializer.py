#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class MisterClass(object):
    def __init__(self):
        self.field = "something"


class OtherClass(object):
    def __init__(self):
        self.field = "else"
        self.inner = InnerClass()


class InnerClass(object):
    def __init__(self):
        self.something = "something else"


class Serializer(object):
    def __init__(self):
        self.serializers = dict(
            MisterClass = self.serialize_misterclass,
            OtherClass = self.serialize_otherclass,
            InnerClass = self.serialize_innerclass,
        )
        self.deserializers = dict(
            MisterClass = self.deserialize_misterclass,
            OtherClass = self.deserialize_otherclass,
            InnerClass = self.deserialize_innerclass,
        )

    def serialize_misterclass(self, obj):
        return dict(field=obj.field)

    def serialize_otherclass(self, obj):
        # json recognizes obj.inner as an object and so it recurses over it.
        return dict(name="other info", field=obj.field, inner=obj.inner)

    def serialize_innerclass(self, obj):
        return dict(name="inner", something=obj.something)

    def deserialize_misterclass(self, data):
        mister = MisterClass()
        mister.field = data['field']
        return mister

    def deserialize_otherclass(self, data):
        other = OtherClass()
        other.field = data['field']
        other.inner = data['inner']
        return other

    def deserialize_innerclass(self, data):
        inner = InnerClass()
        inner.something = data['something']
        return inner

    def encode(self, obj):
        data = self.serializers[obj.__class__.__name__](obj)
        data['__type__'] = obj.__class__.__name__
        return data

    def decode(self, data):
        if '__type__' in data:
            return self.deserializers[data['__type__']](data)
        else:
            return data

    def serialize(self, obj):
        return json.dumps(obj, indent=4, default=self.encode)

    def deserialize(self, data):
        return json.loads(data, object_hook=self.decode)


def test():
    serializer = Serializer()

    obj1 = MisterClass()
    obj2 = OtherClass()

    to_save = dict(mister=obj1, other=obj2)
    saved = serializer.serialize(to_save)
    print saved

    to_read = '''{
    "other": {
        "field": "else",
        "__type__": "OtherClass",
        "inner": {
            "__type__": "InnerClass",
            "something": "something else",
            "name": "inner"
        },
        "name": "other info"
    },
    "mister": {
        "field": "something",
        "__type__": "MisterClass"
    }
}'''
    print to_read

    readin = serializer.deserialize(to_read)
    print readin['other'].inner.something


if __name__ == "__main__":
    test()
