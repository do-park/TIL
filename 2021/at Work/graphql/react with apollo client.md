# Apollo Client로 React 앱 개발하기

1. 패키지 설치

    `$ npm i apollo-boost graphql react-apollo`

    - apollo-boost: Apollo에서 제공하는 GraphQL 클라이언트 패키지
    - graphql: Facebook에서 정의한 GraphQL 스펙을 JS로 구현한 패키지
    - react-apollo: React 앱에 Apollo Client를 연결해주는 패키지

2. Apollo Client 생성
    - Apollo Client 생성을 위해 호출할 GraphQL API의 접속 정보 설정이 필요
    - `apollo-boost` 패키지에서 임포트한 `ApolloClient` 생성자 함수의 인자로 url 속성이 포함된 설정 객체를 넘김
        - 우리 프로젝트의 url 정보는 `.env.local` 내 위치
        - `REACT_APP_GRAPHQL_URL=http://localhost:8081/graphql`

3. React에 Apollo Client 연결
    - 2에서 생성한 ApolloClient 객체를 React에 연결
    - 모든 컴포넌트에서 ApolloClient를 사용할 수 있도록 설정하는 것이 일반적
    - `react-apollo` 패키지에서 임포트한 `ApolloProvider` 컴포넌트로 앱의 최상위 컴포넌트를 감싸준다. 이 때, `client` prop에 2에서 생성한 `ApolloClient` 객체를 넘겨줘야 함

    ```jsx
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { ApolloProvider } from '@apollo/client';
    import { BrowserRouter as Router } from 'react-router-dom';
    import { apolloClient } from './graphql/client';
    import App from './App';
    import 'tailwindcss/dist/base.min.css';
    import 'assets/index.css';
    import 'react-dates/lib/css/_datepicker.css';

    ReactDOM.render(
      <React.StrictMode>
        <ApolloProvider client={ apolloClient }>
          <Router>
            <App />
          </Router>
        </ApolloProvider>
      </React.StrictMode>,
      document.getElementById('root'),
    );
    ```

4. GraphQL API 호출
    - `Query`와 `Mutation` 컴포넌트를 활용
    1. apollo-boost 패키지에서 제공하는 `gql`이라는 template literal tag를 사용해서 일반 자바스크립트 문자열을 GraphQL 구문으로 바꿈
    2. GraphQL 구문을 react-apollo 패키지에서 임포트한 Query 컴포넌트의 `query` prop으로 넘김
        - Query 컴포넌트는 GraphQL API 호출 상태에 따라 렌더링할 내용을 리턴하는 함수를 자식으로 가져야 함
    3.  GraphQL API 호출 시
        - GraphQL 서버로부터 응답을 기다리는 동안 `Query` 컴포넌트의 `loading` 파라미터에 `true` 값을 할당
        - `error` 파라미터에 GraphQL API 호출이 실패된 경우, 오류 데이터가 할당
        - `data` 파라미터는 GraphQL API 호출이 성공한 경우, 정상 데이터가 할당

참고 자료

[[GraphQL] Apollo Client로 React 앱 개발하기](https://www.daleseo.com/graphql-react-apollo-client/)
