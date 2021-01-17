# 기타리스트

https://www.acmicpc.net/problem/1495

- DP
- 메모리 제한이 있어 list와 set을 함께 사용해 풀었다.
- 현재 곡을 연주 가능한 볼륨의 크기를 volumes 리스트에 넣고(default=S), 다음에 연주 가능한 볼륨의 크기를 저장하기 위한 temp set을 생성한다. 이후 volumes를 순회하며 volume에 diff를 더하거나 뺀 값이 0 이상 M 이하인 경우 temp에 추가한다. 한 곡에서 연주 가능한 볼륨의 크기를 모두 구했다면 volumes에 temp의 값을 list로 바꾸어 저장한다.
- 모든 곡을 순회한 뒤, 현재 volumes에 저장된 값이 있다면 max값을, 그렇지 않다면 -1을 반환한다.