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
import { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const handleChange = (e) => {
    console.log("e:", e.target.value);
    setQuery(e.target.value);
  };

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
        <Box sx={{ display: "flex" }}>
          <TextField
            fullWidth
            label="search"
            variant="filled"
            placeholder="Article name"
            onChange={handleChange}
            helperText="search for article name"
          />
        </Box>
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
