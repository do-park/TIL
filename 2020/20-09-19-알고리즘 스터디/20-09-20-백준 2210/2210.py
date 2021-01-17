LIMIT = 5
DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

maps = [list(map(int, input().split())) for _ in range(LIMIT)]
answer = set()

def dfs(y, x, result=0, cnt=0):
    result = result * 10 + maps[y][x]
    cnt += 1
    if cnt == 6:
        answer.add(result)
        return
    for dy, dx in DELTAS:
        ny, nx = y + dy, x + dx
        if 0 <= ny < LIMIT and 0 <= nx < LIMIT:
            dfs(ny, nx, result, cnt)


for i in range(LIMIT):
    for j in range(LIMIT):
        dfs(i, j)

print(len(answer))