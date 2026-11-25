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
### What is key used for
React's identity tracking between renders. when the list changes react compares the old and new elements and needs to know which one is which. With stable keys  it can say `item 3 moved up`, Keeping that item's DOM node and `any state attached to it`. Without them react matches by position.
So if we delete item 1 , every item after it looks `changed`, and state can end up attached to wrong item.
