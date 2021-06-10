`2021-01-21`

# graphQL

> SQL처럼 데이터의 집합에서 특정 데이터를 불러오는 데이터 질의 언어(data query language)

**graphQL이 해결할 수 있는 문제**

1. Over-fetching
   - 요청한 영역의 정보보다 많은 정보를 서버에서 받게 됨
2. Under-fetching
   - 어떤 하나의 기능을 위해 많은 요청을 해야할 때 발생

**graphQL은 한 query에 정확하게 원하는 정보만을 받을 수 있게 해 문제 해결**

 - NO URL, ONLY ONE END POINT

   

# OAuth 2.0

**승인 방식의 종류**

- Authorization Code Grant Type: 권한 부여 코드 승인 타입
- 클라이언트가 다른 사용자 대신 특정 리소스에 접근을 요청할 때 사용. 리소스 접근을 위한 사용자 명과 비밀번호, 권한 서버에 요청해서 받은 권한 코드를 함께 활용하여 리소스에 대한 액세스 토큰을 받는 방식
- Implicit Grant Type: 암시적 승인
  - 권한 부여 코드 승인 타입과 다르게 권한 코드 교환 단계 없이 액세서 토큰을 즉시 반환받아 이를 인증에 이용하는 방식
- Resource Owner Password Credentials Grant Type: 리소스 소유자 암호 자격 증명 타입
  - 클라이언트가 암호를 사용하여 액세스 토큰에 대한 사용자의 자격 증명을 교환
- Client Credentials Grant Type: 클라이언트 자격 증명 타입
  - 클라이언트가 컨텍스트 외부에서 액세스 토큰을 얻어 특정 리소스에 접근을 요청할 때 사용하는 방식



[출처] https://cheese10yun.github.io/spring-oauth2-provider/
