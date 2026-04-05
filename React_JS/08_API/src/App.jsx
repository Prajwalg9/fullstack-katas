import {useState} from 'react';

function App() {


  const url="https://dog.ceo/api/breeds/image/random"
  const [img, setimg] = useState("")
  const [loading, setloading] = useState(false)

  async function fetchApi(){
    setloading(true)
    try{
      const response= await fetch(url)
      const data = await response.json()
      await setimg(data.message)
      setTimeout(()=>{
        setloading(false)
      },600)
    }catch(err){
      alert("Fetch Error :"+err)
      setloading(false)
    }

  }


  return ( <>
  <button onClick={function(){
    fetchApi()
  }} style={{backgroundColor:"limegreen",border:"None",borderRadius:"10px",padding:"10px"}}>
    {loading?"Fetching...":"Fetch Dog Image"}
  </button>
  <img src={img} style={{width:"200px", height:"200px", borderRadius:"15px",display:"block"}} />
  </> );
}

export default App;