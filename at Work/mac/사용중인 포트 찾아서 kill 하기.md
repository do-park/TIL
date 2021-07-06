# 사용중인 포트 찾아서 kill 하기

사용중인 포트 찾기

```
lsof -i :포트번호
```

​	ex. `lsof -i :8000`



kill 하기

```
kill -9 PID
```

​	ex.`kill -9 1234`

