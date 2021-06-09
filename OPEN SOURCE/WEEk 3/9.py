from 8 import mutate

def nearly_equal(a, b):
    mutants = mutate(b)
    if a in mutants:
        print("{} and {} are nearly equal.".format(a, b))
    else:
        print("{} and {} are not nearly equal.".format(a, b))

nearly_equal("apple", "banana")
nearly_equal("bnaana", "banana")