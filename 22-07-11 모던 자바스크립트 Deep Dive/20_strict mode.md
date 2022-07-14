# 20. strict mode

### 20.1 strict mode란?
- 자바스크립트 언어의 문법을 좀 더 엄격히 적용해 오류를 발생시킬 가능성이 높거나 자바스크립트 엔진의 최적화 작업에 문제를 일으킬 수 있는 코드에 대해 명시적인 에러를 발생시킨다.

### 20.2 strict mode의 적용
- 전역의 선두 또는 함수 몸체의 선두에 'use strict';를 추가한다.

### 20.3 전역에 strict mode를 적용하는 것은 피하자
- 전역에 전용한 strict mode는 스크립트 단위로 적용된다.
- 외부 서드파티 라이브러리를 사용하는 경우 라이브러리가 non-strict mode인 경우도 있기 때문에 전역에 strict mode를 적용하는 것은 바람직하지 않다.
- 즉시 실행 함수로 스크립트 전체를 감싸서 스코프를 구분하고, 즉시 실행 함수의 선두에 strict mode를 적용하는 것을 권장

### 20.4 함수 단위로 strict mode를 적용하는 것도 피하자
- 어떤 함수는 strict mode를 적용하고 어떤 함수는 strict mode를 적용하지 않는 것은 바람직하지 않으며 모든 함수에 일일이 strict mode를 적용하는 것은 번거로운 일이다.
- 따라서 strict mode는 즉시 실행 함수로 감싼 스크립트 단위로 적용하는 것이 바람직하다.

### 20.5 strict mode가 발생시키는 에러
1. 암묵적 전역
   - 선언하지 않은 변수를 참조하면 ReferenceError
2. 변수, 함수, 매개변수의 삭제
   - delete 연산자로 변수, 함수, 매개변수를 삭제하면 SyntaxError
3. 매개변수 이름의 중복
   - 중복된 매개변수 이름을 사용하면 SyntaxError
4. with 문의 사용
   - with 문을 사용하면 SyntaxError

### 20.6 strict mode 적용에 의한 변화
1. 일반 함수의 this
   - strict mode에서 함수를 일반 함수로서 호출하면 this에 undefined가 바인딩된다. 생성자 함수가 아닌 일반 함수 내부에서는 this를 사용할 필요가 없기 때문이다. 이때 에러는 발생하지 않는다.
2. arguments 객체
   - strict mode에서는 매개변수에 전달된 인수를 재할당하여 변경해도 arguments 객체에 반영되지 않는다.