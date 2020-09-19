`2020-09-19`

# 섬의 개수

https://www.acmicpc.net/problem/4963



- BFS
- while문을 활용해 입력받는 width와 height가 0, 0인 경우 종료
- 맵 전체에서 for문을 순회하면서 맵의 값이 1인 경우를 찾는다.
- 맵의 값이 1인 경우, answer값을 1 증가하고 visited에 answer를 할당한뒤 q에 해당 좌표를 넣는다. 해당 위치를 기준으로 8방향을 순회하며 맵의 값이 1인 경우가 있는지 찾는다. 있을 경우 visited에 answer값을 할당하고 q에 해당 좌표를 넣는다. 
- 순회가 끝났을 경우 visited에는 연결된 섬끼리 같은 번호로 매칭되어 있음을 확인할 수 있다. 현재 answer의 값(가장 마지막에 발견된 섬의 visited 값)을 반환한다.