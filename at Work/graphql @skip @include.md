# graphql @skip @include

### @skip

In the query below, we fetch posts and decide whether to fetch the title for them or not based on the `skipTitle` GraphQL variable.

GraphQL query

```javascript
query ($skipTitle: Boolean!) {
  queryPost {
    id
    title @skip(if: $skipTitle)
    text
  }
}
```

GraphQL variables

```javascript
{
    "skipTitle": true
}
```



### @include

Similarly, the `@include` directive can be used to include a field based on the value of the `if` argument. The query below would only include the authors for a post if `includeAuthor` GraphQL variable has value true.

GraphQL Query

```javascript
query ($includeAuthor: Boolean!) {
  queryPost {
    id
    title
    text
    author @include(if: $includeAuthor) {
        id
        name
    }
  }
}
```

GraphQL variables

```javascript
{
    "includeAuthor": false
}
```

- https://dgraph.io/docs/graphql/queries/skip-include/



### Inline Fragment

Fragments can be defined inline within a selection set. This is done to conditionally include fields based on their runtime type. This feature of standard fragment inclusion was demonstrated in the `query FragmentTyping` example. We could accomplish the same thing using inline fragments.

```javascript
query inlineFragmentTyping {
  profiles(handles: ["zuck", "cocacola"]) {
    handle
    ... on User {
      friends {
        count
      }
    }
    ... on Page {
      likers {
        count
      }
    }
  }
}
```

Inline fragments may also be used to apply a directive to a group of fields. If the TypeCondition is omitted, an inline fragment is considered to be of the same type as the enclosing context.

```javascript
query inlineFragmentNoType($expandedInfo: Boolean) {
  user(handle: "zuck") {
    id
    name
    ... @include(if: $expandedInfo) {
      firstName
      lastName
      birthday
    }
  }
}
```

- https://spec.graphql.org/June2018/#sec-Inline-Fragments



:rabbit: 꽤 많은 스키마에 `@skip(if:$check)`를 붙이며 내가 옳게 하고 있는지에 대해 심각하게 고민했었는데, skip, include와 inline fragment를 함께 쓰면 좀 더 깔끔한 코드를 작성할 수 있다.