## escape(), encodeURI(), encodeURIComponent()

> url을 통째로 인코딩할 때는 encodeURI, url의 파라미터만 인코딩할 때는 encodeURIComponent

1. escape() / unescape()

   - ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890 @*-_+./

   - 위에서 열거된 문자가 아니면 모두 변환. 1바이트문자는 %XX 형태로 2바이트 문자는 %uXXXX 식으로 변환.

2. encodeURI() / decodeURI()

   - 인터넷 주소에서 쓰는 특수 문자 : ; / = ? & 는 변환을 하지 않음

3. encodeURIComponent() / decodeURIComponent()

   - 인터넷 주소에서 쓰는 특수 문자 : ; / = ? & 까지 변환. 인터넷 주소를 하나의 변수에 넣을때 사용
   - **encodeURIComponent() 는 UTF-8 로 인코딩 하는 것과 같음**



출처: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kim87838&logNo=110153927463

