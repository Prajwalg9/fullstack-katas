import Home from "./components/home/home";
import About from "./components/about/About";
import Contact from "./components/contact/Contact";

function App() {
  const data=[
      "https://images.unsplash.com/photo-1595521624992-48a59aef95e3?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8YmVhdXRpZnVsJTIwcGxhY2VzfGVufDB8fDB8fHww",
      "https://images.unsplash.com/photo-1645551519404-ffbef68bf4be?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8YmVhdXRpZnVsJTIwcGxhY2VzfGVufDB8fDB8fHww",
      "https://images.unsplash.com/photo-1609109238958-eb5130c99873?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8YmVhdXRpZnVsJTIwcGxhY2VzfGVufDB8fDB8fHww",
      "https://images.unsplash.com/photo-1596306499317-8490232098fa?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGJlYXV0aWZ1bCUyMHBsYWNlc3xlbnwwfHwwfHx8MA%3D%3D",
      "https://images.unsplash.com/photo-1533104816931-20fa691ff6ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjR8fGJlYXV0aWZ1bCUyMHBsYWNlc3xlbnwwfHwwfHx8MA%3D%3D",
      "https://plus.unsplash.com/premium_photo-1661962288202-9f04aed88875?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjV8fGJlYXV0aWZ1bCUyMHBsYWNlc3xlbnwwfHwwfHx8MA%3D%3D"
    
  ]
 
  return (
    <>
      <Home info={data}></Home>
      <About></About>
      <Contact></Contact>
    </>
  );
}

export default App;
