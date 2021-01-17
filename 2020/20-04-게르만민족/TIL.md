`2020-06-07`

# Django form label 설정

- ModelForm을 사용할 경우, label을 지정하지 않으면 필드 이름의 첫번째 문자를 대문자로, 밑줄을 공백으로 변환한 label을 생성한다. (ex. store_name >> Store name)
- label을 설정하기 위해서는 `forms.py` >> `class Meta:` 하위에 `labels = {'필드명': '라벨명'}`의 방식으로 설정하면 된다.



# Javascript - onclick과 addEventListener

- addEventListener가 더 모던한 방식
  1. 여러 개의 이벤트를 overwrite할 수 있다.
  2. 작성 중 bubbling, capturing을 설정할 수 있다.
     - `addEventListener('type', 리스너(작동될 함수), 캡쳐링을 쓸지)`
     - 세번째 파라미터가 true일 경우 capturing을, false일 경우 bubbling을 사용한다.
  3. 여러개의 이벤트 타입을 쉽게 바인딩할 수 있다.







`2020-06-06`

# Django - media 파일 업로드

- settings.py

  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```

  - 각 media 파일에 대한 URL의 고정값 설정과, 실제 파일이 저장될 ROOT 경로의 설정

- 파일 업로드

  ```PYTHON
  # models.py
  
  class clsname(models.Model):
      name = models.CharField(max_length=10)
      photo = models.ImageField(upload_to='')
  ```

  - 모델의 upload_to 옵션을 통해, 한 디렉토리에 모든 파일이 들어가지 않도록 함

  - `upload_to`의 경로 지정

    - 문자열: 중간 디렉토리 경로를 지정

      ```python
      # media/image/ 아래 저장
      photo = models.ImageField(upload_to="image")
      # 이미지 업로드 날짜에 따라 디렉토리에 저장
      photo = models.ImageField(upload_t="%Y/%m/^d")
      ```

      

    - 함수: 중간 디렉토리 및 파일명까지 지정

      ```python
      import os
      from uuid import uuid4
      from django.utils import timezone
      
      def date_upload_to(instance, filename):
        # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        # 길이 32 인 uuid 값
        uuid_name = uuid4().hex
        # 확장자 추출
        extension = os.path.splitext(filename)[-1].lower()
        # 결합 후 return
        return '/'.join([
          ymd_path,
          uuid_name + extension,
        ])
      
      photo = models.ImageField(upload_to=date_upload_to)
      ```

  ```html
  <!-- index.html -->
  
  <form action="" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
    <!-- 생략 -->
  </form>
  ```

  - method의 enctype을 설정하지 않으면, 파일은 넘어오지 않고 파일 이름만 넘어오게 된다.

  ```python
  # views.py
  
  store_form = StoreForm(request.POST, request.FILES)
  ```

  - request.FILES로 파일을 받는다.

  ```PYTHON
  # urls.py
  
  urlpatterns = += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```







`2020-06-03`

# 세션 간 통신에 대한 Q&A

도희: 강사님, 개인적으로 공부하다가 궁금한 부분이 생겼는데, javascript 에서 사용하는 세션(sessionStorage)이랑 django views.py  에서 사용하는 세션(request.session)은 다른 세션인가요? javascript에서 필요한 값을 세션에 저장한 뒤에, views.py에서 세션 값을 불러오려고 했는데 잘 안되어서요..

도영: 장고 서버에서 사용하는 세션과 브라우저에서 사용하는 세션은 다르다고 보시면 됩니다. https://docs.djangoproject.com/en/3.0/topics/http/sessions/#using-database-backed-sessions 해당 문서를 보시면 장고에서 사용하는 세션은 database-backed session/ cached session/ file-based session / cookie-based session 이 있습니다. 브라우져 내에 저장되는게 아니라 서버에 저장하면서 확인을 하죠. 

 서버와 브라우져는 통신을 할 때 쿠키를 주고 받으면서 권한을 확인하고 쿠키안에 들어있는 세션id 를 통해 세션 정보를 확인을 합니다. 

 sessionstorage 에 있는 데이터를 서버로 넘기려면 해당 값을 쿠키에 담아서 넘기거나 (get/post)요청에 담아서 전달을 해줘야 합니다.  django와 vue 를 연동하는 수업은 다음주에 진행될 예정이니 조금만 기다려주세요~

```html
<button onclick="getSession()">button</button>

<script>
  function getSession() {
      var adr = sessionStorage.getItem('adr');
      var dadr = sessionStorage.getItem('dadr');
      // console.log(adr);
      // console.log(dadr);
      // console.log(type(adr));
      // cookie
      // var cookie_adr = document.cookie.match('(^|;) ?' + adr + '=([^;]*)(;|$)');
      var c_adr = /adr=([^;]*)/.test(document.cookie) ? unescape(RegExp.$1) : '';
      var c_dadr = /dadr=([^;]*)/.test(document.cookie) ? unescape(RegExp.$1) : '';
      // console.log(c_adr);
      // console.log(c_dadr);
      // console.log(document.cookie)
      //
  }
</script>
```





# 쿠키와 세션

https://jeong-pro.tistory.com/80

https://medium.com/@chrisjune_13837/web-%EC%BF%A0%ED%82%A4-%EC%84%B8%EC%85%98%EC%9D%B4%EB%9E%80-aa6bcb327582



# 쿠키

- javascript: https://cofs.tistory.com/363
- django: https://www.hooni.net/xe/study/101108







`2020-06-02`

# branch 생성과 삭제

- 브랜치 생성
  - `git checkout -b (브랜치명)`
- 브랜치 삭제
  - `git checkout master`
  - `git branch -D (브랜치명)`



`2020-05-30`

# 전역 콜백 함수

javascript에서 페이지가 로드되면 자동으로 실행되는 함수를 구현할 때는 전역 콜백 함수인 window.onload 함수를 사용한다.

```javascript
window.onload = function () {
    
}
```





`2020-05-27`

# 세션에 정보 저장하기

- 한 페이지(HTML)에서 다른 페이지(HTML)으로 정보를 넘겨 주기위해 javascript 활용
  1. main 페이지
     - 해당 메뉴의 버튼을 클릭하면 javascript - setSession() 함수를 활성화
     - setSession() 함수에서 `sessionStorage.setItem()`을 통해 세션에 주소 값을 저장
  2. menu 페이지
     - 해당 메뉴 페이지에서 javascript - getSession() 함수를 활성화할 수 있는 버튼 생성
     - getSession()함수에서 `sessionStorage.getItem()`을 통해 세션에서 주소 값을 불러 옴

- javascript 단에서 session을 사용하기 위해서는 **sessionStorage**를 사용해야 한다.

- 기본적으로 지원하는 메서드

  - | 메서드              | 설명                                               |
    | ------------------- | -------------------------------------------------- |
    | setItem(key, value) | 세션에 value(데이터)를 key 이름으로 저장한다.      |
    | getItem(key)        | 세션에 key 이름으로 저장된 데이터를 가져온다.      |
    | removeItem(key)     | 세션에 있는 특정한 key 값의 데이터를 삭제한다.     |
    | clear()             | 세션에 저장된 모든 데이터를 전부 삭제한다.         |
    | key(number)         | 세션의 특정 순서(index)의 데이터를 가져온다. (0 ~) |
    | length              | sessionStorage에 저장된 데이터의 개수를 가져온다.  |

- https://developer.mozilla.org/ko/docs/Web/API/Window/sessionStorage







`2020-05-25`

# 다음 우편번호 서비스(API)

- http://postcode.map.daum.net/guide
- iframe을 이용하여 페이지에 끼워 넣기 방식을 활용
- 필요한 정보(주소, 상세주소)만 가져올 수 있도록 필요없는 부분은 주석 처리







`2020-04-14`

### git branch의 이해

- https://learngitbranching.js.org/?locale=ko



### git 원격 저장소 초기화

1. 로컬 저장소의 .git 디렉토리를 삭제한다.

2. 로컬 저장소에서 git init을 다시 수행하여 초기화 시킨다.

3. 초기화에 등록될 파일을 추가 및 커밋한다.

   ```bash
   $ git add .
   $ git commit -m 'Initial commit'
   ```

4. 초기화 시킬 원격 저장소를 추가시킨다.

   ```bash
   $ git remote add origin <url>
   ```

5. 현재 상태를 원격저장소에 적용시킨다.

   ```bash
   $ git --force --set-upstream origin master
   ```

- 참고: https://niees.tistory.com/25
- 참고: http://stackoverflow.com/questions/2006172/how-to-reset-a-remote-git-repository-to-remove-all-commits

