# JSON.stringify()

JSON.stringify( )는 자바스크립트의 값을 JSON 문자열로 변환한다.

	- JSON: JavaScript Object Notation의 약자로, 브라우저와 서버사이에서 오고가는 데이터의 형식이다.



`JSON.stringify(value, replacer, space)`

**value(필수)**: JSON 문자열로 변환할 값이다.(배열, 객체, 또는 숫자, 문자 등이 될 수 있다.)

**replacer(선택)**: 함수 또는 배열이 될 수 있다. 이 값이 null 이거나 제공되지 않으면, 객체의 모든 속성들이 JSON 문자열 결과에 포함된다.