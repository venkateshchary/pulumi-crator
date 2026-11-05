
export default function BlogList() {
  const blogs = import.meta.glob("../data/blogs/*.md", {
    eager: true,
    query: '?raw',
    import: 'default',
    caseSensitive:false,
  });
  return (
    <div>
      <h1>Blog list </h1>
      <ul>
        {Object.entries(blogs).map(([fullFileName,]) => {
          const fileName = fullFileName.split('/').at(-1)?.split('.').at(0);
          // 2. Explicitly return your JSX element
          return (<li key={fileName}>{fileName}</li>);
        })}
      </ul>
    </div>
  );
}
