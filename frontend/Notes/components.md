## Spread Operator
```shell
 ... - It is called spread operator
```
Spread Operator used to pass multiple props cleanly

### without spread operator
```jsx
const postData ={
  id: 1,
  title: "Home",
  name: "venkatesh",
  age: 30,
}
<PostCard title={postCardData.title} name={postCardData.name} age={postCardData.age}  />
```
### With spread operator
```jsx
<PostCard {...postData}  />
```
