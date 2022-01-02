## Nullish coalescing operator (?? 연산자)
  - 왼쪽 피연산자가 null 또는 undefined인 경우, 오른쪽 피연산자를 반환
  - 왼쪽 피연산자가 null 또는 undefined가 아닌 경우, 왼쪽 피연산자를 반환
  
## Optional chaining (?. 연산자)
  - 체인의 각 참조가 유효한지 명시적으로 검사하지 않고, 연결된 객체 체인 내에 위치한 속성 값을 읽을 수 있다.
  - 체이닝 연산자 `.`와 유사하게 작동하지만, 참조가 nullish(null || undefined)라면 에러가 발생하지 않고 undefined로 단락된다.
  - 함수 호출에서 사용될 때, 만약 주어진 함수가 존재하지 않는다면 undefined를 리턴한다.
