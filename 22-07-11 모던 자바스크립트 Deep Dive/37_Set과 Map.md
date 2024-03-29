# 37. Set과 Map

### 37.1 Set
- **Set 객체는 중복되지 않는 유일한 값들의 집합이다.**
- Set 객체는 **배열과 유사**하지만 차이가 있다.
  - 동일한 값을 중복해서 포함할 수 없다.
  - 요소 순서에 의미가 없다.
  - 인덱스로 요소에 접근할 수 없다.
- Set은 수학적 집합을 구현하기 위한 자료구조로, 교집합, 합집합, 차집합, 여집합 등을 구현할 수 있다.
1. Set 객체의 생성
   - Set 생성자 함수로 생성한다. 인수를 전달하지 않으면 빈 Set 객체가 생성된다.
   - **Set 생성자 함수는 이터러블을 인수로 전달받아 Set 객체를 생성한다. 이때 이터러블의 중복된 값은 Set 객체에 요소로 저장되지 않는다.**
2. 요소 개수 확인
   - Set.prototype.size 프로퍼티
     - setter 함수 없이 getter 함수만 존재하는 접근자 프로퍼티다. 따라서 size 프로퍼티에 숫자를 할당해 Set 객체의 요소 개수를 변경할 수 없다.
3. 요소 추가
   - Set.prototype.add 메서드
     - 새로운 요소가 추가된 Set 객체를 반환한다. 따라서 add 메서드를 호출한 후에 add 메서드를 연속적으로 호출(메서드 체이닝)할 수 있다.
4. 요소 존재 여부 확인
   - Set.prototype.has 메서드
5. 요소 삭제
   - Set.prototype.delete 메서드
     - 삭제 성공 여부를 나타내는 불리언 값을 반환하기 때문에, 연속적으로 호출할 수 없다.
6. 요소 일괄 삭제
   - Set.prototype.clear 메서드
     - 언제나 undefined를 반환
7. 요소 순회
   - Set.prototype.forEach 메서드
   - Set 객체는 요소의 순서에 의미를 갖지 않지만 Set 객체를 순회하는 순서는 요소가 추가된 순서를 따른다. 이는 다른 이터러블 순회와 호환성을 유지하기 위함이다.
8. 집합 연산

### 37.2 Map
- **Map 객체는 키와 값의 쌍으로 이루어진 컬렉션이다.** Map 객체는 **객체와 유사**하지만 다음과 같은 차이가 있다.
  - 객체를 포함한 모든 값을 키로 사용할 수 있다.
  - 이터러블하다.
  - 요소 개수 확인 시 map.size
1. Map 객체의 생성
   - Map 생성자 함수로 생성한다. 인수를 전달하지 않으면 빈 Map 객체가 생성된다.
   - **Map 생성자 함수는 이터러블을 인수로 전달받아 Map 객체를 생성한다. 이때 인수로 전달되는 이터러블은 키와 값의 쌍으로 이루어진 요소로 구성되어야 한다.**
     - 인수로 전달한 이터러블에 중복된 키를 갖는 요소가 존재하면 값이 덮어써진다. 따라서 Map 객체에는 중복된 키를 갖는 요소가 존재할 수 없다.
2. 요소 개수 확인
   - Map.prototype.size 프로퍼티
     - setter 함수 없이 getter 함수만 존재하는 접근자 프로퍼티다. 따라서 size 프로퍼티에 숫자를 할당해 Map 객체의 요소 개수를 변경할 수 없다.
3. 요소 추가
   - Map.prototype.set 메서드
     - 새로운 요소가 추가된 Map 객체를 반환한다. 따라서 set 메서드를 호출한 후에 set 메서드를 연속적으로 호출할 수 있다.
   - 객체는 문자열 또는 심벌 값만 키로 사용할 수 있지만, Map 객체는 키 타입에 제한이 없다. 따라서 객체를 포함한 모든 값을 키로 사용할 수 있다.
4. 요소 취득
   - Map.prototype.get 메서드
5. 요소 존재 여부 확인
   - Map.prototype.has 메서드
6. 요소 삭제
   - Map.prototype.delete 메서드
     - 삭제 성공 여부를 나타내는 불리언 값을 반환하기 때문에, 연속적으로 호출할 수 없다.
7. 요소 일괄 삭제
   - Map.prototype.clear 메서드
     - 언제나 undefined를 반환
8. 요소 순회
   - Map.prototype.forEach
   - Map.prototype.keys
   - Map.prototype.values
   - Map.prototype.entries