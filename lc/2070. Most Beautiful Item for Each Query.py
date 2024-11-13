class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort(key=lambda x: x[0])
        queries_and_index = [(q, i) for i, q in enumerate(queries)]
        queries_and_index.sort(key=lambda x: x[0])

        result = [0] * len(queries)
        item_index = max_beauty = 0
        for q, i in queries_and_index:
            while item_index < len(items) and items[item_index][0] <= q:
                max_beauty = max(max_beauty, items[item_index][1])
                item_index += 1

            result[i] = max_beauty

        return result
