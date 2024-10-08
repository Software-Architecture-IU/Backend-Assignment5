Posts
GET /posts
```typescript
Query: 
{
    offset: number;
    username: string;
}
```

```typescript
Response:
200: {
    results: [Post, Post, ...]
}
404: { error: "ERR_NOT_FOUND" }
400: { error: "ERR_INVALID_OFFSET" }
400: { error: "ERR_INVALID_USERNAME" }
401: { error: "ERR_UNAUTHORIZED" }
```
Примечание: эндпоинт всегда возвращает 10 постов. Offset это id поста, от которого идёт отсчёт 10 постов.
Если offset не задан, то просто вернуть последние 10 постов.


POST /posts
```typescript
Query: 
{
    username: string;
}
Body: 
{
    content: string;
}
Response:
201: Post
400: { error: "ERR_INVALID_CONTENT" }
401: { error: "ERR_UNAUTHORIZED" }
```

GET /posts/{id}
```typescript
PathParams: 
{
    id: number;
}
Query: 
{
    username: string;
}
Response: 
200: Post
404: { error: "ERR_NOT_FOUND" }
401: { error: "ERR_UNAUTHORIZED" }
```
