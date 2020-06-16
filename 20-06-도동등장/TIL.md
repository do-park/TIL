`20-06-16`

### CSS: hover시 천천히 커지게

```css
.card:hover {
    transform: scale(1.1);
    -webkit-transition: all 1s ease;
    -moz-transition: all 1s ease;
    -ms-transition: all 1s ease;
    transition: all 1s ease;
}
```

- all ____ ease 없이 시간만 입력할 경우, 그 시간이 지난 뒤 뚱-! 하고 커짐



### CSS: object-fit 속성

- `object-fit` 속성은 대체되는 요소의 내용(img, video, object, svg 등)이 지정된 너비와 높이에 맞게 장착되는 방식을 지정한다.
  - `fill`: 대체되는 요소의 내용이 지정된 높이에 따라 확대, 축소, 늘어나거나 움츠러든다. 요소를 가득 채울 수 있는 크기로 변화되면서 종횡비는 유지되지 않는다.
  - `contain`: 내용이 종횡비를 유지하면서 요소에 정의된 너비와 높이안에서 가능한한 많이 확대시킨다.
  - `cover`: 내용이 종횡비를 유지하면서 정의된 너비와 높이를 가득 채울때까지 확대된다.
  - `none`: 내용의 크기가 요소의 크기와 무관하게 기본 알고리즘에 의해 조정된다. 원본의 크기 가운데 정렬된 형태를 띈다.
  - `scale-down`: 내용의 크기를 아무것도 지정되지 않거나 contain이 지정되어 있는 것처럼 변경한다. 원본 크기보다 작아진다.
- 영화 포스터 이미지가 동일한 크기로 보이기를 원했기 때문에 가장 많은 포스터의 크기에 맞춰, 그보다 작은 포스터들이 종횡비를 맞춘 채 확대 또는 축소되기를 바랐다. 따라서 `object-fit: cover;` 속성을 사용했다.



### css: pre tag의 줄바꿈

```html
<pre style="white-space:pre-wrap"></pre>
```

- pre tag 내 style 속성으로 `white-space:pre-wrap`을 주게 되면 스크롤바 없이 줄바꿈이 일어나게 된다. 부트스트랩의 `class="text-break"`는 p tag에서만 사용이 가능하다.



### 시간대

- 생성한 지 6시간이 지나지 않은 글에 대해서는 new 버튼을 띄우는 기능을 추가하려고 했으나 계속해서 실패했다. 

  ```python
  # views.py
  import datetime
  
  check_now = datetime.datetime.now()
  check_delta = (datetime.datetime.now() + timedelta(hours=-6))
  ```

  - views.py에서 datetime 함수를 활용해 시간을 받아와 Article object에 저장된 `created_at`값과 비교하려고 했으나 비교가 불가능했다.

    - 에러 코드: `can't compare offset-naive and offset-aware datetimes`

  - 스택오버플로우에서 코드를 다음과 같이 수정하라는 조언을 발견했다.

    ```python
    from django.utils import timezone
    now = timezone.now()
    ```

  - 따라서 코드를 다음과 같이 수정했으며 프로그램이 정상 작동하는 것을 확인할 수 있었다.

    ```python
    # articles/views.py
    import datetime
    
    check_now = timezone.now()
    check_delta = timezone.now() - timedelta(hours=6)
    ```

    ```html
    <!-- articles/index.html -->
    {% if check_delta < article.created_at %}
    ```

    





`20-06-15`

### error: Related Field got invalid lookup: contains

- 검색 필드에 FK가 포함되었을 때 발생하는 에러

- 검색 필드에서 FK를 제거하면 정상적으로 검색 결과를 볼 수 있다.

  ```python
  # articles/views.py
  
  articles = Article.objects.filter(movie_title__contains=kwd)
  ```

  - 원했던 결과: 영화 제목에 검색어가 포함된 영화의 후기를 출력
  - 그러나 movie_title이 FK이므로 에러가 발생함







`20-06-14`

### ManyToManyField 에서 값 꺼내쓰기 (@python)

```python
# movies/views.py

movie = get_object_or_404(Movie, pk=article.movie_title.pk)
for genre in movie.genres.all():
    gdict[genre.pk] += article.rank
```

- 해당 영화의 장르를 모두 가져오기 위해 movie.genres.all()을 사용한다.
- html에서도 같은 방법(`movie.genres.all`)을 통해 ManyToManyField 값을 꺼내올 수 있다.







`20-06-13`

### render와 redirect

#### [render]

```html
render(request, template_name, context=None, content_type=None, status=None, using=None)
```

- render의 파라미터, 이 중 `request`와 `template_name`은 필수요소
- `context`를 통해 원하는 인자, views.py에서 사용하던 파이썬 변수,를 html 템플릿으로 넘길 수 있다. 딕셔너리형
- 템플릿을 불러온다.

#### [redirect]

```html
redirect(to, permanent=False, *args, **kwargs)
```

- redirect의 파라미터, `to`는 이동할 URL, 단지 URL로 이동만 하기 때문에 render처럼 context값을 전달할 수 없다.

- URL로 이동한다.

- redirect에서 URL이 필요로 하는 값을 전달하기 위해서는 인자를 넘겨주어야 한다.

  - ```python
    context = {
        'movie_pk': movie_pk,
        'article_pk': article_pk,
    }
    return redirect('movies:movie_articles_detail', context)
    ```

  - 위와 같이 작성한 코드는 오류가 발생한다. redirect는 context를 전달할 수 없기 때문이다. 

  - 해당 인자(movie_pk, article_pk)를 URL로 전달하고 싶다면 다음과 같이 코드를 수정해야 한다.

    - ```Python
      return redirect('movies:movie_articles_detail', movie_pk, article_pk)
      ```




### _set.all()

- ManyToManyField에서 ManyToManyField가 아닌 다른 모델 기준으로(reverse) 가져올 때는 `소문자 original model name + _set`을 사용한다. 현재는 Genre 모델이 Movie 모델에 `ManyToManyField`로 들어가 있으므로 다음과 같은 방법으로 해당 장르의 모든 영화를 가져올 수 있다.

- ```python
  genre = get_opject_or_404(Genre, pk=genre_pk)
  movies = genre.movie_set.all()
  ```

- `_set`은 all 외에도 다양한 쿼리 메서드를 사용할 수 있다. 실제 코드에서는 인기가 많고, 최신순인 영화를(popularity 내림차순, releas_date 내림차순) 먼저 보여줄 수 있도록 했다.

- ```python
  movies = genre.movie_set.order_by('-popularity', '-release_date')
  ```







`20-06-12`

### 원하는 값을 모델폼 생성할 때 넘겨주기

```python
# movies/views.py

def movie_articles_create(request, movie_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
      article = form.save(commit=False)
      article.user = request.user
      article.save()
      return redirect('movies:movie_articles', movie_pk)
  else:
    form = ArticleForm(initial={'movie_title':movie})	# 폼 생성시 initial값 지정
  context = {
    'form': form,
  }
  return render(request, 'articles/form.html', context)
```

- form을 생성할 때, `initial={'필드값':넣고자 하는 값}`을 넣는다.



### ManyToManyField 에서 값 꺼내쓰기 (@html)

```html
<!-- movies/index.html -->
{% for genre in movie.genres.all %} <!-- 필드의 값을 전부 가져와 하나씩 꺼내야 하므로 모델.필드명.all로 불러온다 -->
<a type="button" class="btn btn-warning btn-sm mx-1"
   href="{% url 'movies:movie_genre' genre.pk %}">{{ genre }}</a>
{% empty %}
{% endfor %}
```

- movie.genres의 형태가 아니라 `movie.genres.all`의 형태로 필드 내 모든 값을 가져올 수 있다.