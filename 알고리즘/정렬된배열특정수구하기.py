from bisect import bisect_left, bisect_right

def count_by_range(arr, l, r) :
    l_index = bisect_left(arr, l)
    r_index = bisect_right(arr, r)
    return r_index - l_index
