import { useEffect, useState } from "react";

function App() {
  // useEffect is react hook used to handle side effects in functional components

  // Ex 1. Fetch API 
  useEffect(()=>{
    console.log("Component Mounted!")
    fetch("https://jsonplaceholder.typicode.com/posts")
    .then(res=>res.json())
    .then(data=>console.log(data))
  },[])

  // Ex 2. Change on count 
  const [count, setcount] = useState(0)
  useEffect(() => {
    console.log("count changed: ",count)
  },[count])
  

  // Ex 3. Run on every render 
  useEffect(() => {
    console.log("Runs on every Render!")
  })
  
  // Ex 4. Setting interval 
    useEffect(() => {
      const interval=setInterval(()=>{
        console.log("Running..")
      },1000)

      return ()=>{
        clearInterval(interval)
        console.log("cleanup!")
      }
    }, [])
    
  // Ex 5. Api input 
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  useEffect(() => {
    if (query === "") return;

    fetch(`https://api.github.com/users/${query}`)
      .then(res => res.json())
      .then(data => setResults(data));
  }, [query]);

  return ( <>
    <div className="ex1">
      <h1>check console</h1>
    </div>

    <br />

    <div className="ex2">
      <h1>{count}</h1>
      <button onClick={()=>{setcount(count+1)}}>Add 1</button>
    </div>

    <div className="ex3">
      <input 
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search GitHub user"
      />

      <pre>{JSON.stringify(results, null, 2)}</pre>
    </div>

  </> );
}

export default App;