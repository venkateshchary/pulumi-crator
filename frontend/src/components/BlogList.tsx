
export default function BlogList() {
  const blogs = import.meta.glob("../data/blogs/*.md", {
    eager: true,
    query: '?raw',
    import: 'default',
    caseSensitive:false,
  });
  return (
    <div>
      <h1><strong>Blog list</strong> </h1>
      <ul className="flex flex-col gap-2">
        {Object.entries(blogs).map(([fullFileName,]) => {
          const fileName = fullFileName.split('/').at(-1)?.split('.').at(0);
          // 2. Explicitly return your JSX element
          return (<div>
            <li key={fileName}>{fileName}</li>
            <p>
              <a href="" className="text-blue-600 underline">For more details</a>
            </p>

          </div>);
        })}
      </ul>
    </div>
  );
}
