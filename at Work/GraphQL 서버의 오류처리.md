# GraphQL 서버의 오류처리

Apollo Server Error handling



- GraphQL 서버에서 오류가 발생할 경우, Apollo Server는 HTTP 응답 body의 `errors` 배열에 해당 오류에 대한 정보를 담아 준다.
  - 배열? REST API와 달리 한 번의 요청에 여러 개의 리소스에 대한 쿼리가 가능
- errors 객체
  - message: 오류 메시지
  - location: 클라이언트가 전송한 쿼리문 내에서 오류가 발생한 줄과 열
  - path: 쿼리 경로
  - extensions: 에러 코드 및 그 외 부가적인 오류 정보
    - code: 기본적으로 `INTERNAL_SERVER_ERROR`로 고정 
    - extensions에 오류 관련 정보를 추가하고 싶다면 `ApolloError 클래스`를 사용해야 함
- ApolloError 클래스
  - 인자
    - message
    - code: 오류 코드로 사용할 문자열
    - properties: 그 밖에 오류 관련 정보(객체)
  - formatError 속성을 이용해 서버 내부 에러 로그를 남기는 함수 생성
    - 인자로 받은 에러 객체를 다시 리턴해야 클라이언트까지 에러 정보가 전달