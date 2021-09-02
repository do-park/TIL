# location state w/ typescript

- `history.push()`로 페이지 이동 시 state를 활용해 props를 넘겨줄 수 있다.

```typescript
import {useHistory} from "react-router";

const history = useHistory();

<button onClick={() => {history.push({
  pathname: "/products/create",
  state: {productId: p.id}
})}} />
```

- 타입스크립트: 이동한 페이지에서 props를 불러올 때 타입을 명시해줘야 한다.

```typescript
import {useLocation} from "react-router";

interface LocationState {
  productId?: string
}

const productId = useLocation<LocationState>().state?.productId;
```

