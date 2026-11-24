import './App.css'
import { Box, Button, Container, Stack, Typography } from '@mui/material';
import PostCard from './components/PostCard';
import { posts } from './data/post';

function App() {
  const postCardData = {
    title: "Hello",
    excerpt: "install",
    date: "2026-10-22",
  }
  return (
    <Container maxWidth="sm"
      sx={{mt:3, boxShadow:3, p:4, border:2}}>
      <Box sx={{bgcolor:"red"}}>
        <Typography variant='body1'> Hello </Typography>
      </Box>
      <Stack spacing={2}>
        {posts.map((post) => (
          <PostCard {...post} />
        )
        )}
      <PostCard title='How to install ubuntu' excerpt='install it from' date='2026-10-20' />
        <PostCard {...postCardData} />
      </Stack>
    </Container>
  )
}

export default App
