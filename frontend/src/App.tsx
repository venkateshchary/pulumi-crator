import './App.css'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import BlogList from './components/BlogList';
import BlogDetail from './components/BlogDetail';

function Home() {
  return <h1>Home Page</h1>;
}

function About() {
  return <h1>About Page</h1>;
}

function Contact() {
  return <h1>Contact Page</h1>;
}


function App() {

  return (
    <BrowserRouter>
      { /* Navigation */}
      <nav className='space-x-6 border-t-amber-300 shadow-2xl p-2 text-center'>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/blog">Blogs</Link>
        <Link to="/contact">Contact</Link>
      </nav>

      {/* Routes */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/blog" element={<BlogList />} />
        <Route path="/blog/:slug" element={<BlogDetail />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
      {/*<section className='bg-slate-900 text-white max-w-4xl text-center space-y-2 border-cyan-900 shadow-2xl mx-auto p-2'>
        <h1 className='font-bold text-3xl'> Lets learn Tailwind!</h1>
        <p className="loren">
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Corrupti saepe dolore tenetur, perspiciatis explicabo, temporibus cupiditate minima veniam ad adipisci laudantium enim numquam amet velit repellendus pariatur quod? Beatae, perspiciatis.
        </p>
        <button className='border-amber-300 text-red-400 p-1'>submit</button>
      </section>*/}
    </BrowserRouter>
  )
}

export default App
