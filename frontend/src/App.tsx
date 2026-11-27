import "./App.css";
import {
  Box,
  Container,
  IconButton,
  Button,
  Stack,
  Typography,
  AppBar,
  Toolbar,
  TextField,
} from "@mui/material";
import PostCard from "./components/PostCard";
import { posts } from "./data/post";
import BugReportIcon from "@mui/icons-material/BugReport";
import { useState, type ChangeEvent } from "react";

function App() {
  const [query, setQuery] = useState("");


  const handleChange = (e:ChangeEvent<HTMLInputElement>) => {
    console.log("e:", e.target.value);
    setQuery(e.target.value);
  };

  const visiblePosts = posts.filter(post =>
    post.title.toLowerCase().includes(query.toLowerCase())
  );
  console.log("visible Posts: ", visiblePosts.length);
  return (
    <Box>
      <AppBar position="static">
        <Toolbar>
          <IconButton size="large" edge="start" color="inherit">
            <BugReportIcon />
          </IconButton>
          <Typography variant="h6" sx={{ flexGrow: 1 }} component="div">
            HungryBug
          </Typography>
          <Button color="inherit">Blogs</Button>
          <Button color="inherit">Contact</Button>
          <Button color="inherit">About</Button>
        </Toolbar>
      </AppBar>
      <Container maxWidth="sm" sx={{ mt: 3, boxShadow: 3, p: 4, border: 2 }}>
        <Box>
          <TextField
            fullWidth
            label="search"
            variant="filled"
            value={query}
            placeholder="Article name"
            onChange={handleChange}
            sx={{mb:2}}
          />
        </Box>
        <Stack spacing={2}>
          {visiblePosts.length>0 ?(visiblePosts.map((post) => (
            <PostCard key={post.id} {...post} />
          ))) : (
              <Typography variant="body1" color="textSecondary">No posts found</Typography>
          )}

        </Stack>
      </Container>
    </Box>
  );
}

export default App;
