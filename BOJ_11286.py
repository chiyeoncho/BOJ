import sys
import heapq
input = sys.stdin.readline

N = int(input())
nump = []
numn = []

for _ in range(N):
    command = int(input())
    if command == 0:
        if len(nump) == 0 and len(numn) == 0:
            print(0)
        else:
            if len(nump) == 0:
                print(-heapq.heappop(numn))
            elif len(numn) == 0:
                print(heapq.heappop(nump))
            else:
                if numn[0] <= nump[0]:
                    print(-heapq.heappop(numn))
                else:
                    print(heapq.heappop(nump))
    else:
        if command > 0:
            heapq.heappush(nump,command)
        else:
            heapq.heappush(numn,-command)

