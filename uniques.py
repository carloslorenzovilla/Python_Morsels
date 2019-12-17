# I want you to write a function that accepts 
# an iterable and returns a new iterable with 
# all items from the original iterable except 
# for duplicates.
from collections.abc import Hashable

def uniques_only(list_):
    """ Returns iterator of unique items 
        in a list.

        list_: iterable

        returns: iterator
    """
    hash_seen = set()
    not_hash_seen = []
    for item in list_:
        if isinstance(item, Hashable):
            if item not in hash_seen:
                yield item
                hash_seen.add(item)
        else:
            if item not in not_hash_seen:
                yield item
                not_hash_seen.append(item)

if __name__ == "__main__":
    x = uniques_only([1, 2, 1, 2, 3, 3, 1, 4])
    print(x)
    for y in x:
        print(y)