# React .env

- CRA(create-react-app)으로 생성된 프로젝트는 env 파일을 활용해 환경 변수를 사용할 수 있다.-

### env 파일 우선순위

- NODE_ENV 환경 변수는 script에 따라 자동으로 값이 지정되는데, `npm start`는 development, `npm run build`는 production, `npm test`는 test로 매핑된다.
  - `npm start`: .env.development.local, env.development, .env.local, .env
  - `npm run build`: .env.production.local, .env.production, .env.local, .env
  - `npm test`: .env.test.local, .env.test, .env
- 각 스크립트에 따라 왼쪽 파일의 우선순위가 높다.

### 파일 생성

- env 파일은 프로젝트 루트 폴더에 추가하면 된다.
- **변수명은 반드시 `REACT_APP_`으로 시작되어야 한다.** 보안이 필요한 환경 변수의 유출을 방지하기 위해 `REACT_APP_`으로 시작하지 않는 환경 변수는 무시된다.
  - :rabbit: 이 부분을 몰라서 내가 어제부터 오늘까지... 그 고생을 했었구나...