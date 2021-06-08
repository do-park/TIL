# Ajax 에러 코드

```javascript
$.ajax({  
     type: "POST", 
     url: "/region/regionCityChange",  
     data: param,   //&a=xxx 식으로 뒤에 더 붙이면 됨
     dataType: "text",
     success: siguResult,
     error:function(request,status,error){
        alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
       }
     }
 );
```

- 출처: https://shonm.tistory.com/m/454