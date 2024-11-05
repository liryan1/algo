# Find the minimum cost of a rountrip flight between the cities A and B
# starting from city A.
#
# Inputs:
# - D: An integer array of flight costs from A->B, where D[i] is the cost of
# flying from city A to city B on day i.
# - R: An integer array of flight costs from B->A, where R[j] is the cost of
# flying from city B to city A on day j.
#
# Output:
# - The minimum cost of a rountrip from A -> B -> A.
#
# Example:
# - Input:
#   - D: [10, 8, 9, 11, 7]
#   - R: [8,  8, 10, 7, 9]
# - Output: 15 (minimum cost is D[1] + R[3])


def minimumCost(d: list[int], r: list[int]) -> int:
    """
    Process the return flights. From the right side,
    save the minimum cost seen so far. Return anytime in the future,
    i.e. if there's a cheaper flight later, always wait until then.
    """
    m = 1_000_000_000
    for i in range(len(r) - 1, -1, -1):
        m = min(m, r[i])
        r[i] = m

    min_cost = 1_000_000_000
    for i in range(len(d)):
        min_cost = min(min_cost, d[i] + r[i])

    return min_cost
