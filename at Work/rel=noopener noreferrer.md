# rel="noopener noreferrer"

- <a> 태그에서 href 속성에 명시한 웹 페이지(URL)를 새 탭에서 열 경우 추가하는 `target="_blank"` 속성
- `target="_blank"`속성만 사용하게 되면 보안상 취약점이 생기고 퍼포먼스가 떨어질 수 있음



1. target 속성의 값
   - href 속성의 URL에 해당하는 웹 페이지를 어디에서 열 것인가
   - `_self`: (default) 현재의 탭에서 열기
   - `_blank`: 새로운 탭에서 열기
2. `target="_blank"`의 문제점
   1. 보안상 취약점이 생긴다.
      - 개인 정보 유출을 유도하는 가짜 페이지로 부적절한 리디렉션을 하는 등의 문제가 발생할 수 있음
   2. 퍼포먼스가 떨어질 수 있다.
      - 링크된 페이지는 링크를 건 페이지와 같은 프로세스를 통해 실행되므로, 링크된 페이지에서 높은 부하를 유발하는 JavaScript가 실행되고 있다면 링크를 건 페이지에서도 그 영향을 받음



3. 해결 방법

   1. `noopener` 지정

      - 링크된 페이지에서 window.opner을 사용해 링크를 건 페이지를 참조(reference)할 수 없게 됨. 링크된 페이지와 링크를 건 페이지가 별개의 프로세스로 취급되므로 서로 연결되어 퍼포먼스가 떨어지지 않음.

   2. `noreferrer` 지정

      - 다른 페이지로 이동할 때, 링크를 건 페이지의 주소 등의 정보를 브라우저가 Referer로서 송신하지 않음

   3. 사용 방법

      ```html
      <a href="연결할 페이지" target="_blank" rel="noopener noreferrer">Click</a>
      ```



참조: https://joshua-dev-story.blogspot.com/2020/12/html-rel-noopener-noreferrer.html