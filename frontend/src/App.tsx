import "./App.css";
import { Box, Container, Stack, Typography } from "@mui/material";
import PostCard from "./components/PostCard";
import { posts } from "./data/post";

function App() {
  return (
    <Container maxWidth="sm" sx={{ mt: 3, boxShadow: 3, p: 4, border: 2 }}>
      <Box sx={{ bgcolor: "red", mb: 3, p: 2, textAlign: "center" }}>
        <Typography variant="h5"> Blogs </Typography>
      </Box>
      <Stack spacing={2}>
        {posts.map((post) => (
          <PostCard key={post.id} {...post} />
        ))}
      </Stack>
    </Container>
  );
}

export default App;
