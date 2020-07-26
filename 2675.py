def seq_repeater(R, S):
    result = ""
    for letter in list(S):
        result += letter * R
    return result

def solver():
    T = int(input())
    results = []
    while T > 0:
        T -= 1
        raw_input = input().split()
        results.append(seq_repeater(int(raw_input[0]), str(raw_input[1])))
    for result in results:
        print(result)
solver()