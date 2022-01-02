# select box에서 특정 옵션 선택 시 div show/hide

```javascript
$(document).ready(function() {
  $('#selectBox').change(function() {
    var result = $('#selectBox option:selected').val();
    if (result == 'option2') {
      $('.div1').show();
    } else {
      $('.div1').hide();
    }
  }); 
}); 
```

출처: https://truecode-95.tistory.com/47