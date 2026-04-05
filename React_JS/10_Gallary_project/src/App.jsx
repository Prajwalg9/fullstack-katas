import Navbar from "./components/Navbar";
import Body from "./components/Body";
import Buttons from "./components/Buttons";
import { useEffect, useState } from "react";

function App() {

  const [Images, setImages] = useState([])
  const [index, setIndex] = useState(1)

  async function storeImages(){
    const response = await fetch(`https://picsum.photos/v2/list?page=${index}&limit=20`)
    const data = await response.json()
    setImages(data)
  }

  useEffect(() => {
    storeImages()
  }, [index])
  

  return ( <>
    <Navbar></Navbar>
    <Body Images={Images}></Body>
    <Buttons index={index} setIndex={setIndex}></Buttons>
  </> );
}

export default App;