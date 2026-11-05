import { useParams } from "react-router-dom";

export default function BlogDetail() {
  const { slug } = useParams<{slug: string}>(); // grabs the id from the route path structure
  console.log("slug:", slug);
  return (
    <div>
      <h1>Blog Details </h1>
    </div>
  );
}
