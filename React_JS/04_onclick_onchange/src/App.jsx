function App() {
  const changeininp=(para)=>{
    console.log(para)
  }
  const vanish=()=>{
    document.getElementById('inp').value=""
  }
  
  function changebg(){
    document.querySelector('body').classList.toggle("bg-blue-500")
    
  }

  return ( <>
    <input type="text" id="inp" className="border-1 border-black" onCopy={vanish} onChange={function (ele){
      changeininp(ele.target.value)
    }}/><br></br>
    <button className="text-white bg-black p-1 rounded" onClick={changebg}>change bg</button>
  </> );
}

export default App;