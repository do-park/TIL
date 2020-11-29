# 프로그래머스 > 월간 코드 챌린지 시즌1 > 두 개 뽑아서 더하기

def solution(numbers):
    N = len(numbers)
    result = set()
    for i in range(N):
        for j in range(i+1, N):
            result.add(numbers[i]+numbers[j])
    return sorted(list(result))