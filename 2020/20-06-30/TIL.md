`2020-06-30`

# 프로세서와 프로세스

### 프로세서(processor)

- **하드웨어**
  - 하드웨어적인 측면에서 '컴퓨터 내에서 프로그램을 수행하는 하드웨어 유닛'
  - 중앙처리장치(Central Processing Unit), 폰노이만 아키텍처에 의해 만들어졌다면 적어도 하나 이상의 ALU(Arithmetic Logic Unit)와 처리 레지스터(Register)를 내장하고 있어야 한다.
- **소프트웨어**
  - 데이터 포맷을 변환하는 역할을 수행하는 데이터 프로세싱 시스템(데이터 처리 시스템), 출력 가능한 인쇄물을 생성하는 워드 프로세서도 프로세서라 부른다.



### 프로세스(Process)

- 절차, 과정. 특정 목적을 수행하기 위해 나열된 작업의 목록 (프로그램)
- 메모리에 적재되어 프로세서에 의해 실행중인 프로그램

- 프로그램과의 차이
  - 작업의 과정이 파일로 저장되어 있다면 프로그램
  - 메모리에 적재되어 실행 중이거나 실행 대기중일 땐 프로세스



#### 컴퓨터가 프로그램을 실행하는 과정

1. 사용자가 단축 아이콘 혹은 명령행에서 프로그램을 실행한다.
2. 파일로 저장되어 있던 프로그램은 메모리(램)에 로더(Loader)에 의해 적재(load)되고 처음으로 실행해야 할 기계어 코드가 저장된 메모리의 주소를 CPU의 명령주소(IP: Instruction Pointer) 레지스터에 저장한다.
3. 프로세서(CPU)는 IP 레지스터가 가리키는 메모리의 주소에서 (처음으로) 실행할 명령어를 인출(메모리에서 CPU로 가져와)하여 명령 레지스터(IR: Instruction Register)에 저장한다.
4. IR에 저장된 명령을 실행하고 IP에 다음번에 실행할 명령어가 있는 주소를 저장한다.
5. 3~4를 프로그램의 끝까지 반복한다.



출처: https://blogger.pe.kr/422




# 프로세스와 스레드

> 프로세스: 프로그램을 메모리 상에서 실행중인 작업
>
> 스레드: 프로세스 안에서 실행되는 여러 흐름 단위



기본적으로 프로세스마다 최초 1개의 스레드 소유(메인 스레드 포함)

프로세스는 각각 별도의 주소공간을 할당 (독립적)

- Code: 코드 자체를 구성하는 메모리 영역(프로그램 명령)
- Data: 전역변수, 정적변수, 배열 등(초기화된 데이터)
- Heap: 동적 할당 시 사용(new(), malloc() 등) 
- Stack: 지역 변수, 매개 변수, 리턴 값(임시 메모리 영역)

스레드는 Stack만 따로 할당 받고, 나머지 영역은 서로 공유한다.

하나의 프로세스가 생성될 때, 기본적으로 하나의 스레드도 생성

**프로세스는 자신만의 고유 공간과 자원을 할당받아 사용**하지만, **스레드는 다른 스레드와 공간, 자원을 공유하면서 사용**하는 차이점이 있다.



### 멀티 프로세스

> 하나의 컴퓨터에 여러 CPU 장착해 하나 이상의 프로세스를 병렬로 처리

- 장점: 안전성(메모리 침범 문제를 OS 차원에서 해결)
- 단점: 각각 독립된 메모리 영역을 갖고 있어, 작업량 많을수록 오버헤드가 발생. Context Switching으로 인한 성능 저하
  - **Context Switching**
    - 프로세스의 상태 정보를 저장하고 복원하는 일련의 과정
    - 즉, 동작 중인 프로세스가 대기하면서 해당 프로세스의 상태를 보관하고, 대기하고 있던 다음 순번의 프로세스가 동작하면서 이전에 보관했던 프로세스 상태를 복구하는 과정을 말한다.
      - 프로세스는 각 독립된 메모리 영역을 할당받아 사용되므로, 캐시 메모리 초기화와 같은 무거운 작업이 진행되었을 때 오버헤드가 발생할 문제가 존재함.



### 멀티 스레드

> 하나의 응용 프로그램에서 여러 스레드를 구성해 각 스레드가 하나의 작업을 처리하는 것

스레드들이 공유 메모리를 통해 다수의 작업을 처리하도록 함

- 장점: 독립적인 프로세스에 비해 공유 메모리만큼의 시간, 자원 손실이 감소. 전역 변수와 정적 변수에 대한 자료 공유 가능
- 단점: 안전성 문제. 하나의 스레드가 데이터 공간을 망가뜨리게 되면 모든 스레드가 작동 불능 상태.
  - 멀티 스레드의 안전성에 대한 단점은 **Critical Section**기법을 통해 대비
    - 하나의 스레드가 공유 데이터 값을 변경하는 시점에 다른 스레드가 그 값을 읽으려할 때 발생하는 문제를 해결하기 위한 동기화 과정
    - 상호 배제, 진행, 한정된 대기를 충족해야 한다.



출처: [https://github.com/gyoogle/tech-interview-for-developer/blob/master/Computer%20Science/Operation%20System/Process%20vs%20Thread.md](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Computer Science/Operation System/Process vs Thread.md)



# 파이썬 Generator

>   A function which returns an iterator. It looks like a normal function except that it contains yield statements for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function. Each yield temporarily suspends processing, remembering the location execution state (including local variables and pending try-statements). When the generator resumes, it picks-up where it left-off (in contrast to functions which start fresh on every invocation).

- iterator를 생성해주는 function
  - iterator: next()메소드를 이용해 데이터에 순차적으로 접근이 가능한 object
- 사용하는 이유
  - memory의 효율적인 사용
  - Lazy evaluation: 계산 결과 값이 필요할 때까지 계산을 늦추는 효과



출처: https://bluese05.tistory.com/56