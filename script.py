# expected array structure is every item (int/float)
# also all of the items should increase or decrease by the same number
# read assets/info.pdf or you won't understand the name of the variables
def find_n(array, s):
    # get first and second item
    k = array[0]
    l = array[1]

    # apply the formula of n
    n = (s-2*k+l)/(l-k)

    return {"wanted": s, "pos": int(n)}
