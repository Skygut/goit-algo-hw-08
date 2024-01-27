import heapq


def min_cost_to_combine_cables(cable_lengths):
    heapq.heapify(cable_lengths)

    total_cost = 0
    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        combined = first + second
        total_cost += combined

        heapq.heappush(cable_lengths, combined)

    return total_cost


cable_lengths_example = [5, 4, 2, 8]
print(min_cost_to_combine_cables(cable_lengths_example))
