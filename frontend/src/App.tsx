// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from './assets/vite.svg'
// import heroImg from './assets/hero.png'
import './App.css'

function App() {

  return (
    <>
    <head>
      <ul>
        <li>Home</li>
        <li>Blogs</li>
        <li>Contact</li>
        <li>Starts Here</li>
      </ul>
    </head>
      <section className='bg-slate-900 text-white max-w-4xl text-center space-y-2 border-cyan-900 shadow-2xl mx-auto p-2'>
        <h1 className='font-bold text-3xl'> Lets learn Tailwind!</h1>
        <p className="loren">
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Corrupti saepe dolore tenetur, perspiciatis explicabo, temporibus cupiditate minima veniam ad adipisci laudantium enim numquam amet velit repellendus pariatur quod? Beatae, perspiciatis.
        </p>
        <a href="" className='inline-block bg-fuchsia-400 px-2 py-1 rounded-full hover:bg-fuchsia-700 transition-colors'>Click Here</a>
      </section>
    </>
  )
}

export default App
