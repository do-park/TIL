# 30. Date
- 표준 빌트인 객체인 Date는 날짜와 시간(연, 월, 일, 시, 분, 초, 밀리초)을 위한 메서드를 제공하는 빌트인 객체이면서 생성자 함수
- 현재 날짜와 시간은 자바스크립트 코드가 실행된 시스템의 시계에 의해 결정된다.

### 30.1 Date 생성자 함수
- Date는 생성자 함수다. Date 생성자 함수로 생성한 Date 객체는 내부적으로 날짜와 시간을 나타내는 정수값을 갖는다.
  - 1970년 1월 1일 00:00:00(UTC) 기점으로 Date 객체가 나타내는 날짜와 시간까지의 밀리초
- Date 객체는 기본적으로 현재 날짜와 시간을 나타내는 정수값을 가진다. 현재 날짜와 시간이 아닌 다른 날짜와 시간을 다루고 싶은 경우 Date 생성자 함수에 명시적으로 해당 날짜와 시간 정보를 인수로 지정한다.
- Date 생성자 함수로 객체를 생성하는 방법
  1. new Date()
  2. new Date(milliseconds)
  3. new Date(dateString)
  4. new Date(year, month[, day, hour, minute, second, millisecond])

### 30.2 Date 메서드
1. Date.now
2. Date.parse
3. Date.UTC
4. Date.prototype.getFullYear
5. Date.prototype.setFullYear
6. Date.prototype.getMonth
7. Date.prototype.setMonth
8. Date.prototype.getDate
9. Date.prototype.setDate
10. Date.prototype.getDay
11. Date.prototype.getHours
12. Date.prototype.setHours
13. Date.prototype.getMinutes
14. Date.prototype.setMinutes
15. Date.prototype.getSeconds
16. Date.prototype.setSeconds
17. Date.prototype.getMilliSeconds
18. Date.prototype.setMilliSeconds
19. Date.prototype.getTime
20. Date.prototype.setTime
21. Date.prototype.getTimezoneOffset
22. Date.prototype.toDateString
23. Date.prototype.toTimeString
24. Date.prototype.toISOString
25. Date.prototype.toLocaleString
    - 로캘(Locale): 사용자 인터페이스에서 사용되는 언어, 지역 설정, 출력 형식 등을 정의하는 문자열(ko-KR.UTF-8)
26. Date.prototype.toLocaleTimeString