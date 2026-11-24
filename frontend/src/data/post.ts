export interface Post{
  id: number;
  title: string;
  excerpt: string;
  date: string;
}

export const posts: Post[] = [
  { id: 1, title: "Rust Variables", excerpt: "int bool string", date: "2026-10-11" },
  { id: 2, title: "Rust Loops", excerpt: "loops", date: "2026-10-12" },
  { id: 3, title: "Rust Conditions", excerpt: "if else if", date: "2026-10-13" },
  { id: 4, title: "Rust Barrowing", excerpt: "barrowing", date: "2026-10-14" },
  {id: 5, title: "Rust Life times", excerpt:"static life times", date: "2026-10-15"},
]
