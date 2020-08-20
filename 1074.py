def check_0to3(n, r, c):
    result = 0
    power_of_2_half = (2 ** n) // 2
    
    if r >= power_of_2_half:
        result = result + 2
    if c >= power_of_2_half:
        result = result + 1
    return result


def position_to_orders(n, r, c):
    orders = []
    while n >= 1:
        position_value = check_0to3(n, r, c)
        orders.append(position_value)
        n = n - 1
        r = r % (2 ** n)
        c = c % (2 ** n)
    #print(orders)
    return orders

def orders_to_nth(orders, n):
    if len(orders) == 1:
        return orders[0]
    first, *rest = orders
    return first * (4 ** n) + orders_to_nth(rest, n - 1)

#assert(orders_to_nth(position_to_orders(2, 3, 1), 1) == 11)
#assert(orders_to_nth(position_to_orders(3, 7, 7), 2) == 63)
#assert(orders_to_nth(position_to_orders(4, 15, 15), 3) == 255)

assert(orders_to_nth(position_to_orders(2, 0, 0), 1) == 0)
assert(orders_to_nth(position_to_orders(2, 0, 1), 1) == 1)
assert(orders_to_nth(position_to_orders(2, 0, 2), 1) == 4)
assert(orders_to_nth(position_to_orders(2, 0, 3), 1) == 5)
assert(orders_to_nth(position_to_orders(2, 1, 0), 1) == 2)
assert(orders_to_nth(position_to_orders(2, 1, 1), 1) == 3)
assert(orders_to_nth(position_to_orders(2, 1, 2), 1) == 6)
assert(orders_to_nth(position_to_orders(2, 1, 3), 1) == 7)
assert(orders_to_nth(position_to_orders(2, 2, 0), 1) == 8)
assert(orders_to_nth(position_to_orders(2, 2, 1), 1) == 9)
assert(orders_to_nth(position_to_orders(2, 2, 2), 1) == 12)
assert(orders_to_nth(position_to_orders(2, 2, 3), 1) == 13)



n, r, c = [int(x) for x in input().split()]
# number = r * 2 ** n + c
orders = position_to_orders(n, r, c)
print(orders_to_nth(orders, n-1))


