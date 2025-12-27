# Credit to https://stackoverflow.com/users/11753311/royr
# https://stackoverflow.com/questions/27974126/get-all-n-choose-k-combinations-of-length-n#:~:text=Adding%20the%20recursive%20function


def combinations(array, tuple_length, prev_array=[]):
    if len(prev_array) == tuple_length:
        return [prev_array]
    combs = []
    for i, val in enumerate(array):
        prev_array_extended = prev_array.copy()
        prev_array_extended.append(val)
        combs += combinations(array[i + 1 :], tuple_length, prev_array_extended)
    return combs
