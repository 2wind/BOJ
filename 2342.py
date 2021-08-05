import sys

def calc_cost(foot, current):
    if foot == current:
        return 1
    elif foot == 0:
        return 2
    elif abs(foot - current) == 2:
        return 4
    else:
        return 3

def calc_dp(moved_left, moved_right, current):
    cost_ll = moved_left[0] + calc_cost(moved_left[1], current)     # moved left --> move left feet
    cost_lr = moved_left[0] + calc_cost(moved_left[2], current)     # moved left --> move right feet
    cost_rl = moved_right[0] + calc_cost(moved_right[1], current)    # moved right --> move left feet
    cost_rr = moved_right[0] + calc_cost(moved_right[2], current)    # moved right --> move right feet

    lmove_cost = cost_ll if cost_ll < cost_rl else cost_rl
    # lmove_left = current
    lmove_right = moved_left[2] if cost_ll < cost_rl else moved_right[2]
    
    rmove_cost = cost_lr if cost_lr < cost_rr else cost_rr
    rmove_left = moved_left[1] if cost_lr < cost_rr else moved_right[1]
    # rmove_right = current
    
    return [[lmove_cost, current, lmove_right], [rmove_cost, rmove_left, current]]

    
instructions = [int(x) for x in sys.stdin.readline().strip().split()]

dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(len(instructions))]
# [cost, lfoot, rfoot] of moving left, [cost, lfoot, rfoot] of right
index = 0
while True:
    current = instructions[index]
    if current == 0:
        break

    moved_left, moved_right = dp[index]

    dp[index+1] = calc_dp(moved_left, moved_right, current)

    index += 1

print(dp)
print(min(dp[index][0][0], dp[index][1][0]))
