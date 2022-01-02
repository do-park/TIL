# HTTP/2 multiplexing

multiplexing

- browser가 하나의 connection 상에서 동시에 여러 개의 request를 보내는 기술
- 이 때, 받을 때의 순서는 신경쓰지 않는다.



HTTP/1.1

- request를 순서대로 보냄
- synchronous 하게 작동
- 인터넷이 대중화되며 다른 국가간의 서버 연결 또한 잦아지게 되었고 속도 개선의 필요성을 느낌
  - connection을 여러개 맺어 동시에 파일을 받는 방법을 사용했으나, 커넥션끼리 정보를 주고 받는 문제, 너무 많은 컨텐츠를 소비하는 문제 등이 발생



HTTP/2

- multiplexing
- 여러 개의 컨텐츠를 받는 것은 동일하지만, queue 등을 활용해 하나의 connection 만으로 컨텐츠를 동시에 받을 수 있도록 함