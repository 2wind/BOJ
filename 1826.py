import heapq

gas_stations = []
# number of gas stations
N = int(input())
for _ in range(N):
    d, g = [int(x) for x in input().split()]
    gas_stations.append((d, g))

# insert, and sort gas station by distance, and gas
gas_stations.sort(key=lambda x: -x[1])
gas_stations.sort(key=lambda x: x[0])

# print(gas_stations)

# distance until village, petrollum remaining intially.
L, P = [int(x) for x in input().split()]

candidates = []
in_heap = set()
count = 0

while P < L:
    # put reachable, unsearched stations into heap
    for station in gas_stations:
        distance, gas = station[0], station[1]
        if distance <= P and station not in in_heap:
            # sort by most gas obtainable
            heapq.heappush(candidates, (-gas, distance, gas))
            in_heap.add(station)

    if not candidates:
        if P < L:
            count = -1
        break

    # get best one
    # print(candidates)
    best = heapq.heappop(candidates)

    distance, gas = best[1], best[2]
    # add to remaining petrol
    P += gas
    # print(P)
    count += 1

print(count)
