N, K = [int(x) for x in input().split()]

# N개의 물병과 x개의 물병을 이용해 K개의 물병 만들기.
# [N]으로 시작 --> [N%2, N//2]로 감소 가능
# ex. N = 7, K = 3이면 1L 7개 --> 1L 1개 2L 3개 --> 1L 1개 2L 1개 4L 1개
# 7 = 0b111이니까 바로 가능
# N = 9, K = 2이면 1:9 --> 1:1, 2:4 --> 1:1, 2:0, 4:2 --> 1:1, 2:0, 4:0, 8:1
# 9 = 0b1001이니까 바로 가능
# N = 13, K = 2이면 13 = 0b1101, 가장 가까운 1이 2개인 수는 17 = 0b10001
# 14 = 0b1110, 15=0b1111, 16 = 0b10000
# 1씩 더하면서 가장 가까운 1의 갯수가 K보다 작거나 같은 숫자를 찾으면 된다.
# 불가능한 경우: K == 0이면 옮기는 것이 불가능. 그 외는 어떻게든 2의 배수로 만들면 옮길 수 있다.

def calc_bottle(N, K):
    if K == 0:
        return -1
    
    original = N

    while True:
        if (bin(N).count("1") <= K):
            break
        N += 1

    return N - original


print(calc_bottle(N, K))