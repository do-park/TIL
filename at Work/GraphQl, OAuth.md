`2021-01-21`

# graphQL

**graphQL이 해결할 수 있는 문제**

1. Over-fetching
   - 요청한 영역의 정보보다 많은 정보를 서버에서 받게 됨
2. Under-fetching
   - 어떤 하나의 기능을 위해 많은 요청을 해야할 때 발생

**graphQL은 한 query에 정확하게 원하는 정보만을 받을 수 있게 해 문제 해결**

 - NO URL, ONLY ONE END POINT

   

# OAuth 2.0

- 다양한 플랫폼 환경에서 권한 부여를 위한 산업 표준 프로토콜

  - AccessToken을 발급받아, 그 토큰을 기반으로 원하는 기능을 구현

- 용어 설명

  - Resource Owner: 개인정보의 소유자
  - Client: 제3의 서비스
  - Resource Server: API서버, Resource Owner 관련 정보를 제공하는 서버
  - Authorization Server: 권한 부여 서버, 로그인을 통해 인증 후 권한을 부여
  - Authentication Server: 실제로 로그인 서비스를 제공하는 서버

- AccessToken 발급을 위해 발급받고자하는 사이트에 우리의 서버를 등록

  - 등록하는 과정은 사이트마다 다르지만 Client ID, Client Secert, Authorized redirect urls는 반드시 필요

  - Client ID, Client Secert는 Resource Server에서 발급
  - Authorized redirect url은 Client에서 등록, 이 url이 아닌 다른 url로부터 요청이 들어온다면 Resource Server는 해당 요청을 무시



[출처] https://meetup.toast.com/posts/105