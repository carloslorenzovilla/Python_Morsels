# I want you to write a function that accepts 
# an iterable and returns a new iterable with 
# all items from the original iterable except 
# for duplicates.
import collections

def uniques_only(list_):
    gen = set()
    return (x for x in list_ if not (x in gen or gen.add(x)))

if __name__ == "__main__":
    x = uniques_only([1, 2, 1, 2, 3, 3, 1, 4])
    print(x)
    for y in x:
        print(y)