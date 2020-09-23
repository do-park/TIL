# BOJ 1495 기타리스트
N, S, M = map(int, input().split())
diffs = list(map(int, input().split()))
volumes = [S]
for diff in diffs:
    temp = set()
    for volume in volumes:
        if volume + diff <= M:
            temp.add(volume + diff)
        if volume - diff >= 0:
            temp.add(volume - diff)
    volumes = list(temp)
print(max(volumes) if volumes else -1)