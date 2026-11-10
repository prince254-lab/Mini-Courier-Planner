import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from algorithms.sorting import merge_sort_parcels
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra


print("========== EDGE CASE TESTING ==========\n")

# TEST 1: Empty Parcel List
empty_result = merge_sort_parcels([])
assert empty_result == []
print("TEST 1 PASSED: Empty parcel list")

# TEST 2: Single Parcel
single_parcel = [{
    "parcel_id": "P101",
    "priority": 1,
    "deadline": "10:00"
}]

single_result = merge_sort_parcels(single_parcel)
assert len(single_result) == 1
assert single_result[0]["parcel_id"] == "P101"
print("TEST 2 PASSED: Single parcel sorting")

# TEST 3: Empty Knapsack
selected, weight, value, dp = knapsack([], 20)

assert len(selected) == 0
assert weight == 0
assert value == 0
print("TEST 3 PASSED: Empty knapsack")

# TEST 4: Zero Capacity
parcels = [{
    "parcel_id": "P101",
    "weight": 5,
    "value": 100,
    "priority": 1,
    "deadline": "10:00"
}]

selected, weight, value, dp = knapsack(parcels, 0)

assert weight == 0
assert value == 0
print("TEST 4 PASSED: Zero capacity")

# TEST 5: Shortest Path
graph = {
    "W": [("A", 5)],
    "A": [("W", 5)]
}

distances, parents = dijkstra(graph, "W")

assert distances["A"] == 5
print("TEST 5 PASSED: Dijkstra shortest path")

print("\nALL EDGE CASE TESTS COMPLETED SUCCESSFULLY!")