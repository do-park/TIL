# 32. String
- 표준 빌트인 객체인 String은 원시 타입인 문자열을 다룰 때 유용한 프로퍼티와 메서드를 제공한다.

### 32.1 String 생성자 함수
- 표준 빌트인 객체인 String 객체는 생성자 함수 객체다. 따라서 new 연산자와 함께 호출해 String 인스턴스를 생성할 수 있다.
- String 생성자 함수에 인수를 전달하지 않고 new 연산자와 함께 호출하면 [[StringData]] 내부 슬롯에 빈 문자열을 할당한 String fovj rorcpfmf todtjdgksek.
  - ES5에서는 [[StringData]]를 [[PrimitiveValue]]라 불렀다.
- String 래퍼 객체는 배열과 마찬가지로 length 프로퍼티와 인덱스를 나타내는 숫자 형식의 문자열을 프로퍼티 키로, 각 문자를 프로퍼티 값으로 갖는 유사 배열 객체이면서 이터러블이다. 따라서 배열과 유사하게 인덱스를 사용해 각 문자에 접근할 수 있다.
  - 단, 문자열은 원시 값이므로 변경할 수 없다.
- String 생성자 함수의 인수로 문자열이 아닌 값을 전달하면 인수를 문자열로 강제 변환한 후, [[StringData]] 내부 슬롯에 변환된 문자열을 할당한 String 래퍼 객체를 생성한다.
- new 연산자를 사용하지 않고 String 생성자 함수를 호출하면 String 인스턴스가 아닌 문자열을 반환한다. 이를 이용해 명시적으로 타입을 변환하기도 한다.

### 32.2 length 프로퍼티
- 문자열의 문자 개수를 반환한다.

### 32.3 String 메서드
- String 객체의 메서드는 언제나 새로운 문자열을 반환한다. 문자열은 변경 불가능한 원시 값이기 때문에 **String 래퍼 객체도 읽기 전용 객체로 제공된다.**
1. String.prototype.indexOf
2. String.prototype.search
3. String.prototype.includes
4. String.prototype.startsWith
5. String.prototype.endsWith
6. String.prototype.charAt
7. String.prototype.substring
8. String.prototype.slice
9. String.prototype.toUpperCase
10. String.prototype.toLowerCase
11. String.prototype.trim
12. String.prototype.repeat
13. String.prototype.replace
14. String.prototype.split