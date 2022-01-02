# Select박스 option 값 선택하기

- option value로 선택

  ```javascript
  $("#id").val("1").prop("selected", true); //값이 1인 option 선택
  ```

- option 순서로 선택

  ```javascript
  $("#id option:eq(0)").prop("selected", true); //첫번째 option 선택
  ```



출처: https://yjcorp.tistory.com/11