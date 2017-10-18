from __future__ import absolute_import, print_function, unicode_literals

from collections import OrderedDict


class OverrideOrderedDict(OrderedDict):
    """
    Override magic method dunder new to instantiate Order Indices list.

    Python initialization process >> call __new__ followed by __init_.
    """
    def __new__(cls, *args, **kwargs):
        __instance = OrderedDict.__new__(cls, *args, **kwargs)
        __instance.__items = list()
        __instance.__uniq_items = set()
        return __instance

    # Overriding __setitem__ of OrderedDict, each new key will be appended to the Order Indices list
    def __setitem__(self, key, value, dict_setitem=dict.__setitem__):
        super(OverrideOrderedDict, self).__setitem__(key, value)

        if key not in self.__uniq_items:
            self.__uniq_items.add(key)
            self.__items.append(key)

        return self

    def __delitem__(self, key, dict_delitem=dict.__delitem__):
        super(OverrideOrderedDict, self).__delitem__(key)
        self.__items.remove(key)
        return self

    def __update_element(self, index, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('Needs object to inserted at given position')

        keys = list()
        to_update = dict()
        if args:
            obj = args[0]
            keys.extend(obj.keys())
            to_update.update(obj)

        if kwargs:
            to_update = kwargs
            keys = list(to_update.keys())  # Returns dict_keys

        if(len(keys) > 1):
            raise Exception('Cannot insert multiple keys at same index')

        self.update(to_update)

        if keys[0] not in self.__uniq_items:
            self.__uniq_items.add(keys[0])
            self.__items.insert(index, keys[0])

        else:
            self.__items.remove(keys[0])
            self.__items.insert(index, keys[0])

    def insert_before(self, index, *args, **kwargs):
        index -= 1
        self.__update_element(index, *args, **kwargs)

    def insert_aftet(self, index, *args, **kwargs):
        index += 1
        self.__update_element(index, *args, **kwargs)

    def insert_at_pos(self, index, *args, **kwargs):
        self.__update_element(index, *args, **kwargs)


if __name__ == "__main__":
    orderdict = OverrideOrderedDict({
        'carD':('blue', 1),
        'carB':('red', 2),
        'carE':('blue', 3),
        'carC':('red', 4),
        'carA':('blue', 5),
        })
    print(orderdict.values)
