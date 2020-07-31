def palindrome_recursive(input_string):
    if len(input_string) < 2:
        return True
    else:
        l = list(input_string)
        return list(l)[0] == list(l)[-1] and palindrome_recursive(l[1:-1])

def palindrome(input_string):
    return palindrome_recursive(input_string)

def palin(number):
    return str(number) == str(number)[::-1]

def main():
    while True:
        number = int(input())
        if number == 0:
            return
        else:
            print("yes") if palindrome(str(number)) else print("no")

main()