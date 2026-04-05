function App() {
  /* clear all local storage */
  localStorage.clear()

  // Add Items to the localstorage
  localStorage.setItem("User","prajwal")

  // Retrive Items from localStorage
  let data=localStorage.getItem("User")
  console.log(data)

  // Remove Items from localStorage
  localStorage.removeItem("User")

  // Add multiple Items 
  let multidata={
    "name":"prajwal",
    "age":19,
    "subjects":["Eng","Marathi","Hindi"]
  }
  localStorage.setItem("Data",JSON.stringify(multidata))
  let info = JSON.parse(localStorage.getItem("Data"))
  console.log(info)

  return ( <>
    
  </> );
}

export default App;