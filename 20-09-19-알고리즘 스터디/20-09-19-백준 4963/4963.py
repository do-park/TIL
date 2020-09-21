from collections import deque
DELTA = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

while True:
    width, heigth = map(int, input().split())
    if not width and not heigth:
        break
    maps = [list(map(int, input().split())) for _ in range(heigth)]
    visited = [[0] * width for _ in range(heigth)]
    answer = 0
    q = deque()
    for h in range(heigth):
        for w in range(width):
            if maps[h][w] and not visited[h][w]:
                answer += 1
                visited[h][w] = answer
                q.append((h, w))
                while q:
                    y, x = q.pop()
                    for dy, dx in DELTA:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < heigth and 0 <= nx < width and maps[ny][nx] and not visited[ny][nx]:
                            visited[ny][nx] = answer
                            q.append((ny, nx))
    print(answer)