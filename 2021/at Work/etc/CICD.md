# CI/CD

- 애플리케이션 개발 단계를 자동화하여 애플리케이션을 보다 짧은 주기로 고객에게 제공하는 방법
- 지속적인 통합, 지속적인 서비스 제공, 지속적인 배포
- 새로운 코드 통합으로 인해 개발 및 운영팀에 발생하는 문제(인테그레이션 헬, integration hell)을 해결하기 위한 솔루션



### CI (Continuous Integration)

- 개발자를 위한 자동화 프로세스인 지속적인 통합
- 어플리케이션의 새로운 코드 변경 사항이 정기적으로 빌드 및 테스트되어 공유 repository에 통합하는 것
- CI가 필요한 환경
  - 다수의 개발자가 형상관리 툴을 공유하여 사용하는 환경
  - MSA(Micro Service Architecture) 환경
    - MSA: 작은 기능별로 서비스를 잘게 쪼개어 개발
    - 대부분 Agile(소규모 기능 단위로 빠르게 개발&적용을 반복하는 개발방법론) 방법론이 적용되므로 기능 추가가 매우 빈번
- CI의 핵심 목표
  - 버그를 신속하게 찾아 해결
  - 소프트웨어의 품질 개설
  - 새로운 업데이트의 검증 및 릴리즈 시간 단축



#### CD (Continuous Delivery & Continuous Deployment)

- 지속적인 서비스 또는 지속적인 배포
- Continuous Delivery: 공유 Repository로 자동 릴리즈
- Continuous Deployment: Production 레벨까지 자동으로 deploy
- 개발자의 변경 사항이 repository를 넘어, 고객의 프로덕션(Production) 환경까지 릴리즈



대표적인 CI/CD 툴: Jenkins, Travis CI, Bamboo