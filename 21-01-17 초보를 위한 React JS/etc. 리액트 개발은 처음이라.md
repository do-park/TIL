# JSX (Javascript XML)

- 자바스크립트에 XML 문법을 추가한 자바스크립트 확장형 문법

- 자바스크립트 코드(프로그래밍 코드)와 HTML 코드를 동일 컴포넌트 상에서 제어 가능

- #### 주요 규칙

  - 닫는 태그가 반드시 필요

  - 최상위 태그는 하나로 구성된다. 그렇지 않으면 Fragment 요소로 감싼다.

  - JSX내 자바스크립트 코딩 추가는 {} 블록 안에 표시한다

  - 삼항연산자 사용가능 `true? result1 : result2`

  - JSX내 인라인 스타일 제공 가능

    ```javascript
    <div style={ style }></div>
    <div style={{ backgroundColor: black }}></div>
    ```

  - Class 속성 대신 className

  - 코드정리 코드 포맷터 적극 활용

    - ```javascript
      // .prettierrc  파일 생성 후 내용
      {
          "singleQuote":true,
          "semi":true,
          "useTabs":false,
          "tabWidth":2
      }
      ```

    - ctrl + shift + p > format document > 프리티어 포맷터 설정

    - File > Preferences > Settings > Text Editor > Formatting > Format On Save 체크