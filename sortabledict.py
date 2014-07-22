#!/usr/bin/env python

from operator import itemgetter
from types import FunctionType

class SortableDict(dict):

    """
    This is an extension of the Python standard dictionary to provide support
    for retrieving ordered output from the 'dict' builtin type.

    Usage:

        <SortableDict>.sortedKeys() or <SortableDict>.sortedValues() with or without the reversed parameter:
            - returns a list of the specified objects sortable via the builtin .sort() either normal or reversed.
            ex. dict.sortedleKeys()
                dict.sortedleValues()
                dict.sortedKeys(reversed) - list reverse sorted
                dict.sortedValues(reversed) - list reverse sorted

        <SortableDict>.sortedItems(<'key, 'value'>) or <SortableDictict>.sortedItems(<'key', value'>, reversed):
            - return (key, value) tuples either sorted by key or value, either forward or reversed as specified.
            ex. dict.sortedItems() - returns (key, value) tuples sorted forward by key by default
                dict.sortedItems('key') - key is the default but this is accecpted for readability / clarity.  Same as
                                          dict.sortedItems().
                dict.sortedItems('value') - returns (key, value) tuples sorted forward by value, sorting identical values by
                                            key since keys are unique.
                dict.sortedItems(reversed) - returns (key, value) tuples reverse sorted by key by default
                dict.sortedItems('key', reversed) - returns (key, value) tuples reverse sorted by key.  Key is the default
                                                    but this is accecpted for readability / clarity.
                dict.sortedItems('values', reversed) - returns (key, value) tuples reverse sorted by value, sorting identical
                                                       values by keys since they are unique.

        <SortableDict>.keysSortedByValue() or <SortableDict>.keysSortedByValue(reversed):
        - returns a list of keys either forward or reverse sorted by thier associated values.

        <SortableDict>.valuesSortedByKey() or <SortableDict>.valuesSortedByKey(reversed):
        - returns a list of values either forward or reverse sorted by thier associated keys.

        run ./sortabledict.py from command line for concrete examples.

        Ideal usage is to copy this python class to an accessible directory and implement via 'from sorteddict import *' and
        to initialize all dictionaries as <x> = SortableDict()'

        lambda's as sorting functions are now implemented.   As long as one of the parameters is a callable it will be used
        as the sorting method. The last "callable" in the argument stack will be the sorting function.
    """

    def sortedKeys(self, returnFunc=lambda x : x):
        outList = super(SortableDict, self).keys()
        outList.sort()
        return list(returnFunc(outList))

    def sortedValues(self, returnFunc=lambda x : x):
        outList  = super(SortableDict, self).values()
        outList.sort()
        return list(returnFunc(outList))

    def sortedItems(self, *args):
        returnFunc  = lambda x: x
        key = itemgetter(0)
        if args:
            for arg in args:
                if not callable(arg):
                    if arg.lower() not in ('key', 'value'):
                        raise ValueError(
                            'The specified argument "' +
                            str(arg) +
                            '" is not recognized for the sorted functions'
                        )
                    elif arg.lower() == 'value':
                        key = itemgetter(1,0)
                else: 
                    returnFunc = arg
        return list(returnFunc(sorted(super(SortableDict, self).items(), key=key)))

    def keysSortedByValue(self, returnFunc=lambda x : x):
        outList = []
        for item in self.sortedItems('value'):
            outList.append(item[0])
        return list(returnFunc(outList))

    def valuesSortedByKey(self, returnFunc=lambda x : x):
        outList = []
        for item in self.sortedItems('key'):
            outList.append(item[1])
        return list(returnFunc(outList))

    def example(self):
        testString = "{'b' : 1, 'A' : 6, 1 : 5, 'C' : 3, 'c' : 8, 2 : 4, 'a' : 2, 3 : 8, 'd' : 7, 'B' : 0, 'D' : 8}"
        test = SortableDict(eval(testString))
        print test.__doc__, '\n'
        print "*****", "INPUT", "*****"
        print "This is the input string for SortableDict:",testString
        print "Original dict as evaluated:", test, '\n'
        print "*****","SortableDict.sortedKeys()","******"
        print "SortableDict.sortedKeys", test.sortedKeys()
        print "SortableDict.sortedKeys(reversed):", test.sortedKeys(reversed),'\n'
        print "*****","SortableDict.sortedValues","******"
        print "SortableDict.sortedValues():", test.sortedValues()
        print "SortableDict.sortedValues(reversed):", test.sortedValues(reversed), '\n'
        print "*****","SortableDict.sortedItems","******"
        print "SortableDict.sortedItems():", test.sortedItems()
        print "SortableDict.sortedItems('key'):", test.sortedItems('key')
        print "SortableDict.sortedItems('value'):", test.sortedItems('value')
        print "SortableDict.sortedItems(reversed):", test.sortedItems(reversed)
        print "SortableDict.sortedItems('key', reversed):", test.sortedItems('key', reversed)
        print "SortableDict.sortedItems('value', reversed):", test.sortedItems('value', reversed), '\n'
        print "*****", "SortableDict.keysSortedByValue", "*****"
        print "SortableDict.keysSortedByValue():", test.keysSortedByValue()
        print "SortableDict.keysSortedByValue(reversed):", test.keysSortedByValue(reversed), '\n'
        print "*****", "SortableDict.valuesSortedByKey", "*****"
        print "SortableDict.valuesSortedByKey():", test.valuesSortedByKey()
        print "SortableDict.valuesSortedByKey(reversed):", test.valuesSortedByKey(reversed), '\n'

if __name__ == "__main__":
    SortableDict().example()
