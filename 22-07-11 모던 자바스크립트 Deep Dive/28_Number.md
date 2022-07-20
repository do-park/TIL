# 28. Number
- 원시 타입인 숫자를 다룰 때 유용한 프로퍼티와 메서드를 제공

### 28.1 Number 생성자 함수
- 표준 빌트인 객체인 Number 객체는 생성자 함수 객체다. 따라서 new 연산자와 함께 호출해 Number 인스턴스를 생성할 수 있다.
- Number 생성자 함수에 인수를 전달하지 않고 new 연산자와 함께 호출하면 [[NumberData]] 내부 슬롯에 0을 할당한 Number 래퍼 객체를 생성한다.

### 28.2 Number 프로퍼티
1. Number.EPSILON
2. Number.MAX_VALUE
3. Number.MIN_VALUE
4. Number.MAX_SAFE_INTEGER
5. Number.MIN_SAFE_INTEGER
6. Number.POSITIVE_INFINITY
7. Number.NEGATIVE_INFINITY
8. Number.NaN

### 28.3 Number 메서드
1. Number.isFinite
2. Number.isInteger
3. Number.isNaN
4. Number.isSafeInteger
5. Number.prototype.toExponential
6. Number.prototype.toFixed
7. Number.prototype.toPrecision
8. Number.prototype.toString