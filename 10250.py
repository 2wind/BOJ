def calculateRoomNumber(height, width, number):
    order = number - 1
    quotient, remainder = (order) // height, (order) % height
    room_height = remainder + 1
    room_width = quotient + 1
    room_number = (room_height) * 100 + room_width
     
    return str(room_number)

def main():
    T = int(input())
    while T > 0:
        T -= 1
        H, W, N = [int(x) for x in input().split()]
        print(calculateRoomNumber(H, W, N))

main()