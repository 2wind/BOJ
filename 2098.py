import sys

def isVisit(route, k):
    return route & (1 << k - 1) != 0

def passbys(route):
    # actually fastest way to count 1 in binary
    return bin(route).count("1")

def get_route(N, W, i, route, dp):
    distance = sys.maxsize
    for j in range(1, N): # for route passing j, (1 from N)
        if isVisit(route, j): # if j is in route,
            before = route & ~(1 << j-1) # get route before going thru j
            d = W[i][j] + dp[j][before] # current distance = (i --> j) + (j -- before --> 0)
            if d < distance:
                distance = d
    return distance

N = int(sys.stdin.readline().strip())
W = [[0 for _ in range(N)] for _ in range(N)]

dp = [[0 for _ in range(2 ** (N-1))] for _ in range(N)] # dp = i -- route --> 0 minimum distance

for i in range(N):
    W[i] = list(map(int, sys.stdin.readline().strip().split())) # W = direct route i --> j

# print(W)

for i in range(N):
    for j in range(N):
        if W[i][j] == 0:
            W[i][j] = sys.maxsize # initialize nonreachable as maxsize

for i in range(1, N):
    dp[i][0] = W[i][0] # initialize i -- (nothing) --> 0 from W[i][0]


for i in range(1, N-1): # from i in range 1, N-1 (going thru 1 to N-1 locations) (ex, 2)
    for route in range(1, 2 ** (N-1)): # for every possible route
        if passbys(route) == i: # select route that pases only i locations (ex. 2, 3)
            for j in range(1, N): # for each route, select j from 1 to N-1
                if not isVisit(route, j): # if j is not in route as bitmasking, (ex, 1, 4, etc)
                    dp[j][route] = get_route(N, W, j, route, dp) # update j -- (route) --> 0 using get_route
                    # dp[1][0b001100] = get_route(N, W, 1, 0b001100, dp)
                # if j is in route, it is invalid: you want to know j -- (route) --> 0.

dp[0][2 ** (N-1) -1] = get_route(N, W, 0, 2 ** (N-1)-1, dp)
# solution is 0 -- 2 ** (N-1)-1 (every other locations) --> 0.

# print(dp)
print(dp[0][2 ** (N-1) -1])