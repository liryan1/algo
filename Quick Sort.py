def quickSort(a, lo=0, hi=None, comparator=None):
    """
    Place the pivot element at the right place, then sort the left and
    right arrays. O(n log n), recursive
    """
    hi = len(a) - 1 if hi is None else hi
    comparator = comparator or (lambda x: x)

    if lo < hi:
        pivot_idx = _partition(a, lo, hi, comparator)
        quickSort(a, lo, pivot_idx - 1, comparator)
        quickSort(a, pivot_idx + 1, hi, comparator)


def _partition(a, lo, hi, comparator):
    pivot = comparator(a[hi])
    i = lo  # index right of elements smaller than pivot
    for j in range(lo, hi):
        # if a[j] is smaller than pivot, swap to the left side
        if comparator(a[j]) <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    # insert the pivot at i
    # now all a[:i] <= a[i] < a[i+1:]
    a[i], a[hi] = a[hi], a[i]
    return i
