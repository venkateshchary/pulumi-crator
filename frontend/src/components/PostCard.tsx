import { Card, CardContent, Typography } from "@mui/material";


interface PostCardProps {
  title: string;
  excerpt: string;
  date: string;
}
export default function PostCard({title, excerpt, date}: PostCardProps) {

  return (
    <Card variant="outlined">
      <CardContent>
        <Typography variant="h5">{title}</Typography>
        <Typography variant="body1">{excerpt}</Typography>
        <Typography variant="caption" color="text.secondary">{date}</Typography>
      </CardContent>
    </Card>
  );
}
