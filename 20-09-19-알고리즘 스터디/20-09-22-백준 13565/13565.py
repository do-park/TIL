from collections import deque

DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
M, N = map(int, input().split())
maps = [list(map(int, input())) for _ in range(M)]
q = deque()
for n in range(N):
    if not maps[0][n]:
        maps[0][n] = 2
        q.append((0, n))
while q:
    y, x = q.popleft()
    for dy, dx in DELTAS:
        ny, nx = y + dy, x + dx
        if 0 <= ny < M and 0 <= nx < N and not maps[ny][nx]:
            maps[ny][nx] = 2
            q.append((ny, nx))
print("YES" if maps[-1].count(2) else "NO")