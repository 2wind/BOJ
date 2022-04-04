from collections import deque

class Building:
    def __init__(self, h, w, raw_building):
        # 빌딩 한 층의 가로, 세로, 구조를 저장
        self.h = h
        self.w = w
        self.building = raw_building


    def get_tile(self, i, j):
        # 갈 수 없는 곳에 대한 예외처리
        if i < 0 or j < 0 or i >= self.h or j >= self.w:
            return None
        else:
            return self.building[i][j]

    def get_interesting_tiles(self):
        pois = set()
        for i in range(self.h):
            for j in range(self.w):
                if 0 < i < self.h-1 and 0 < j < self.w-1:
                    continue
                tile = self.get_tile(i, j)
                # 갈 수 있는 곳이나 열쇠로 열 수 있는 곳이면
                # 일단 갈 수 없어도 후보로는 넣어 둔다.
                if tile != "*":
                    pois.add((i, j))

        return pois

    def set_tile(self, i, j, item):
        self.building[i][j] = item

class Player:
    def __init__(self, building: Building, keys: set):
        self.keys = keys
        self.starting_points = set()
        self.building = building
        self.documents = 0
        self.visited_new = False

    def BFS(self):
        # starting point들에서 시작한다.
        self.DQ = deque(self.starting_points)
        self.visited_new = False
        # Deque가 차 있는 동안, 방문하지 않은 노드라면 방문을 시도한다.
        while self.DQ:
            node = self.DQ.popleft()
            i, j = node
            traversable, poi = self.traverse(i, j)
            # 갈 수 있는 곳이라면, 주위도 방문 시도를 해 본다.
            if traversable:
                nearbys = ((i+1, j), (i, j+1), (i-1, j), (i, j-1))
                self.DQ.extend(nearbys)
                self.visited_new = True
            # 만약 나중에 열 수도 있는 곳이라면, starting point에 넣는다.
            if poi:
                self.starting_points.add((i, j))

        # 만약 추가로 방문한 곳이 없다면, False.
        return self.visited_new

                
    def traverse(self, i, j):
        tile = self.building.get_tile(i, j)
        if tile is not None:
            if tile == "1" or tile == "*":
                # 이동 불가
                return False, False
            if tile == "$":
                # 이동한다. 문서를 회수한다.
                self.documents += 1
                # 해당 타일을 .으로 바꾼다.
                self.building.set_tile(i, j, "1")
                return True, False
            if "A" <= tile <= "Z":
                # 가진 키 중에 열 수 있는 것이 있다면,
                if (tile.lower() in self.keys):
                    # 이동한다. .으로 바꾼다.
                    if (i, j) in self.starting_points:
                        self.starting_points.remove((i, j))
                    self.building.set_tile(i, j, "1")
                    return True, False
                # 그렇지 않다면 이동 불가
                return False, True
            if "a" <= tile <= "z":
                self.keys.add(tile)
                # 해당 타일을 .으로 바꾼다.
                self.building.set_tile(i, j, "1")
                return True, False    
            # .이므로, 이동한다.
            self.building.set_tile(i, j, "1")
            return True, False
        return False, False


test_cases = int(input())
for _ in range(test_cases):
    # 맵 초기화
    h, w = [int(x) for x in input().split()]
    raw_building = []
    for _ in range(h):
        raw_building.append(list(input()))
    building = Building(h, w, raw_building)    

    # 초기 열쇠 세팅
    key_input = input()
    keys = set() if key_input == "0" else set(key_input)
    player = Player(building, keys)

    # 적절한 입구 찾기
    player.starting_points = building.get_interesting_tiles()

    # 반복적으로 입구에서부터 DFS 혹은 BFS를 실시한다.
    while True:
        if not player.BFS():
            break
   
    # 맵의 변화가 없다면 현재까지 모은 문서 갯수를 출력한다.
    print(player.documents)
