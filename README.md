sortabledict
============

###A python dictionary implementation with sortable output

Calling this extension from the commandline provides the following output:


    This is an extension of the Python standard dictionary to provide support
    for retrieving ordered output from the 'dict' builtin type.

    Usage:

        <SortableDict>.sortedKeys() or <SortableDict>.sortedValues() with or without
        the reversed parameter:
            - returns a list of the specified objects sortable via the builtin
              .sort() either normal or reversed.
            ex. dict.sortedleKeys()
                dict.sortedleValues()
                dict.sortedKeys(reversed) - list reverse sorted
                dict.sortedValues(reversed) - list reverse sorted

        <SortableDict>.sortedItems(<'key, 'value'>)
        or
        <SortableDictict>.sortedItems(<'key', value'>, reversed):
            - return (key, value) tuples either sorted by key or value, either 
              forward or reversed as specified.
            ex. dict.sortedItems() - returns (key, value) tuples sorted forward by
                                     key by default
                dict.sortedItems('key') - key is the default value but this is
                                          accecpted for readability / clarity.
                                          same as dict.sortedItems().
                dict.sortedItems('value') - returns (key, value) tuples sorted
                                            forward by value, , sorting by key if
                                            values are equal.
                dict.sortedItems(reversed) - returns (key, value) tuples reverse
                                             sorted by key by default
                dict.sortedItems('key', reversed) - returns (key, value) tuples
                                                    reverse sorted by key.  Key is
                                                    the default value but this is
                                                    accecpted for readability /
                                                    clarity.
                dict.sortedItems('values', reversed) - returns (key, value) tuples
                                                       reverse sorted by value

        <SortableDict>.keysSortedByValue()
        or
        <SortableDict>.keysSortedByValue(reversed):
            - returns a list of keys either forward or reverse sorted by thier
              associated values, sorting by key if values are equal.

        <SortableDict>.valuesSortedByKey()
        or
        <SortableDict>.valuesSortedByKey(reversed):
            - returns a list of values either forward or reverse sorted by thier
              associated keys, further sorting equal values by key.

        run ./sortabledict.py from command line for concrete examples.

        Ideal usage is to copy this python class to an accessible directory and
        implement via 'from sorteddict import *' and to initialize all dictionaries
        as <x> = SortableDict() or <x> = SortableDict(<dict>)

        lambda's as sorting functions are now implemented.   As long as one of the
        parameters is a callable it will be used as the sorting method.
     

    ***** INPUT *****
    This is the input string for SortableDict: {'b' : 1, 'A' : 6, 1 : 5, 'C' : 3, 'c' : 8, 2 : 4, 'a' : 2, 3 : 8, 'd' : 7, 'B' : 0, 'D' : 8}
    Original dict as evaluated: {'A': 6, 1: 5, 'C': 3, 3: 8, 'D': 8, 'c': 8, 2: 4, 'B': 0, 'a': 2, 'b': 1, 'd': 7} 

    ***** SortableDict.sortedKeys() ******
    SortableDict.sortedKeys [1, 2, 3, 'A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']
    SortableDict.sortedKeys(reversed): ['d', 'c', 'b', 'a', 'D', 'C', 'B', 'A', 3, 2, 1] 

    ***** SortableDict.sortedValues ******
    SortableDict.sortedValues(): [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8]
    SortableDict.sortedValues(reversed): [8, 8, 8, 7, 6, 5, 4, 3, 2, 1, 0] 

    ***** SortableDict.sortedItems ******
    SortableDict.sortedItems(): [(1, 5), (2, 4), (3, 8), ('A', 6), ('B', 0), ('C', 3), ('D', 8), ('a', 2), ('b', 1), ('c', 8), ('d', 7)]
    SortableDict.sortedItems('key'): [(1, 5), (2, 4), (3, 8), ('A', 6), ('B', 0), ('C', 3), ('D', 8), ('a', 2), ('b', 1), ('c', 8), ('d', 7)]
    SortableDict.sortedItems('value'): [('B', 0), ('b', 1), ('a', 2), ('C', 3), (2, 4), (1, 5), ('A', 6), ('d', 7), (3, 8), ('D', 8), ('c', 8)]
    SortableDict.sortedItems(reversed): [('d', 7), ('c', 8), ('b', 1), ('a', 2), ('D', 8), ('C', 3), ('B', 0), ('A', 6), (3, 8), (2, 4), (1, 5)]
    SortableDict.sortedItems('key', reversed): [('d', 7), ('c', 8), ('b', 1), ('a', 2), ('D', 8), ('C', 3), ('B', 0), ('A', 6), (3, 8), (2, 4), (1, 5)]
    SortableDict.sortedItems('value', reversed): [('c', 8), ('D', 8), (3, 8), ('d', 7), ('A', 6), (1, 5), (2, 4), ('C', 3), ('a', 2), ('b', 1), ('B', 0)] 

    ***** SortableDict.keysSortedByValue *****
    SortableDict.keysSortedByValue(): ['B', 'b', 'a', 'C', 2, 1, 'A', 'd', 3, 'D', 'c']
    SortableDict.keysSortedByValue(reversed): ['c', 'D', 3, 'd', 'A', 1, 2, 'C', 'a', 'b', 'B'] 

    ***** SortableDict.valuesSortedByKey *****
    SortableDict.valuesSortedByKey(): [5, 4, 8, 6, 0, 3, 8, 2, 1, 8, 7]
    SortableDict.valuesSortedByKey(reversed): [7, 8, 1, 2, 8, 3, 0, 6, 8, 4, 5] 

