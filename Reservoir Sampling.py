from random import randint


def sample(arr: list[int]) -> int:
    """Randomly select an element from arr, without random.choice"""
    selected_idx = cap = 0

    for i in range(len(arr)):
        if randint(0, cap) == 0:
            selected_idx = i
        cap += 1

    return arr[selected_idx]


"""
Let's focus on the first element in an array of 3 elements
i = 0, selected_idx = 0 because randint selects an int between [0, 0]
i = 1, selected_idx = 0 when randint(0, 1) returns 1
(selected_idx is not reassigned, 1/2 chance)
so far, the probability of selected_idx = 0 is 1 * 1/2 = 1/2
i = 2, select_idx = 0 when randint(0, 2) return 1 or 2 (2/3 chance)
the chance of selected_idx = 0 is 1 * 1/2 * 2/3 = 1/3
(must have selected 0 and not changed to 1 or 2)

If we consider the second number, the chance of selected_idx = 1 on
i = 1 is randint(0, 1) returning 1 which is 1/2.
i = 2, the chance of `randint(0, 2) != 0` is 2/3
The probability of selected_idx = 1 is 1/2 * 2/3 = 1/3

The third number doesn't care about the first two selections, only if
randint(0, 2) == 2 which is a 1/3 probability.

The chance of selecting any element is the same. This can be applied to
any target number condition by scanning the array once.

This holds for any number of elements we need to select.
"""
