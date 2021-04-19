# export named / export default

- **named**
    - 하나의 모듈(파일)에서 여러 변수 또는 클래스 등을 export 할 수 있다.
    - import 시 export된 이름과 동일한 이름을 사용
        - 다른 이름으로 import할 경우 `as`를 활용

            ```jsx
            import {Pagination as myPagination} from '../component/Pagination';
            ```

    - `* as`를 사용해 한 파일의 클래스/변수 들을 한 번에 import 할 수 있다.

        ```jsx
        import * as myPagination from '../component/Pagination';
        // 위와 같이 import할 경우 myPagination.Pagination 의 방식으로 사용 가능
        ```

- **default**
    - 모듈을 이름없이 export
    - 하나의 모듈(파일)에서 하나의 변수 또는 클래스 등만 default export만 가능
    - import 시 원하는 이름으로 import 가능

        ```jsx
        const Pagination: React.FC<any> = ({ pages = 1, currentPage = 0, goToPage }) => (
          <PaginationContainer>
            <ReactPaginate
              forcePage={ currentPage }
              pageCount={ pages || 1 }
              pageRangeDisplayed={ 10 }
              marginPagesDisplayed={ 1 }
              previousLabel={ <ChevronLeftIcon tw="w-4 h-6" /> }
              nextLabel={ <ChevronRightIcon tw="w-4 h-6" /> }
              onPageChange={ ({ selected }) => goToPage(selected) }
            />
          </PaginationContainer>
        );
        export default Pagination;
        ```

        ```jsx
        import Pagination from '../component/Pagination'; // O
        import Hello from '../component/Pagination';      // O
        ```

    - var, let, const를 바로 export default 할 수 없다.

        ```jsx
        // this code is not work
        export default const Pagination: React.FC<any> = ({ pages = 1, currentPage = 0, goToPage }) => (
          <PaginationContainer>
            <ReactPaginate
              forcePage={ currentPage }
              pageCount={ pages || 1 }
              pageRangeDisplayed={ 10 }
              marginPagesDisplayed={ 1 }
              previousLabel={ <ChevronLeftIcon tw="w-4 h-6" /> }
              nextLabel={ <ChevronRightIcon tw="w-4 h-6" /> }
              onPageChange={ ({ selected }) => goToPage(selected) }
            />
          </PaginationContainer>
        );
        export default Pagination;
        ```

- Airbnb JavaScript Style Guide는 하나만 export 하는 모듈은 default export를 사용하기를 권장
