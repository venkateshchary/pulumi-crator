import "./App.css";
import { Box, Container, IconButton,Button, Stack, Typography, AppBar, Toolbar } from "@mui/material";
import PostCard from "./components/PostCard";
import { posts } from "./data/post";
import BugReportIcon from '@mui/icons-material/BugReport';

function App() {
  return (
    <Box>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit">
              <BugReportIcon/>
          </IconButton>
          <Typography variant="h6" sx={{flexGrow:1}} component="div">HungryBug</Typography>
          <Button color="inherit">Blogs</Button>
          <Button color="inherit">Contact</Button>
          <Button color="inherit">About</Button>
        </Toolbar>
    </AppBar>
    <Container maxWidth="sm" sx={{ mt: 3, boxShadow: 3, p: 4, border: 2 }}>
      <Stack spacing={2}>
        {posts.map((post) => (
          <PostCard key={post.id} {...post} />
        ))}
      </Stack>
      </Container>
    </Box>

  );
}

export default App;
