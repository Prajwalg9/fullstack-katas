import { useEffect, useState } from "react";

function App() {
    const [data, setdata] = useState(null)
    const API=import.meta.env.VITE_API_URL
    useEffect(()=>{
        async function fetchData() {
            try{
                const response= await fetch(API)
                if(!response.ok){
                    throw new Error("Network response was not ok!")
                }
                const result= await response.json()
                setdata(result)
                console.log(result)
            }catch(err){
                console.log("Error fetching the data: ",err)
            }
        }
        fetchData()
    },[])
    return ( <>
    hello
    </> );
}

export default App;