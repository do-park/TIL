# 44. REST API
- 웹이 HTTP를 제대로 사용하지 못하고 있는 상황을 보고 HTTP의 장점을 최대한 활용할 수 있는 아키텍처로서 REST를 소개
- HTTP 프로토콜을 의도에 맞게 디자인하도록 유도
- REST의 기본 원칙을 성실히 지킨 서비스 디자인을 `RESTful` 이라고 표현한다.
  - REST는 HTTP 기반으로 클라이언트가 서버의 리소스에 접근하는 방식을 규정한 아키텍처
  - REST API는 REST를 기반으로 서비스 API를 구현한 것을 의미한다.

1. REST API의 구성
  - REST는 자체 표현 구조로 구성되어 REST API만으로 HTTP 요청의 내용을 이해할 수 있다.
  - 구성 요소
    - 자원(resource): 자원, URI(엔드포인트)로 표현
    - 행위(verb): 자원에 대한 행위, HTTP 요청 메서드로 표현
    - 표현(representations): 자원에 대한 행위의 구체적 내용, 페이로드로 표현
2. REST API 설계 원칙
  1. URI는 리소스를 표현해야 한다.
    - 리소스 표현에 중점. 리소스를 식별할 수 있는 이름은 동사보다는 명사를 사용.
  2. 리소스에 대한 행위는 HTTP 요청 메서드로 표현한다.
    - 클라이언트가 서버에게 요청의 종류와 목적(리소스에 대한 행위)을 알리는 방법
    - 주로 5가지 요청 메서드(GET, POST, PUT, PATCH, DELETE 등)를 사용해 CRUD를 구현한다.
3. JSON server를 이용한 REST API 실습
  1. JSON Server 설치
  2. db.json 파일 생성
  3. JSON Server 실행
  4. GET 요청
  5. POST 요청
  6. PUT 요청
  7. PATCH 요청
  8. DELETE 요청
