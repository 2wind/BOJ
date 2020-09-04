import sys
from operator import itemgetter, attrgetter

n = int(input())
slots = []
while n > 0:
    slot = tuple([int(x) for x in sys.stdin.readline().split()])
    slots.append(slot)
    n = n-1

slots.sort(key=itemgetter(1, 0))

result = []
earlist = 0
for slot in slots:
    if(earlist <= slot[0]):
        earlist = slot[1]
        result.append(slot)

print(len(result))