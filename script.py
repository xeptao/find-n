# expected array structure is every item (int/float)
# also all of the items should increase or decrease by the same number
def find_n(array, wanted):
    # get first and second item
    first = array[0]
    second = array[1]

    # do inverse operations to isolate n
    # the form is an+c
    a = second-first
    c = (2*first)-second
    n = (wanted/a) - c

    return {"wanted": wanted, "pos": int(n)}
