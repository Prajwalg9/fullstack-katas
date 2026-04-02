import { useState } from "react";

function App() {
  const [counter, setCounter] = useState(0);



  const [ogMsg, setOgMsg]=useState({
    "name":"prajwal",
    "age":27,
    "phone":9325840474,
    "email":"prajwalgg99@gmail.com"
  })
  // const [draftName,setName]=useState("")
  // const [draftAge,setAge]=useState("")
  // const [draftPhone,setPhone]=useState("")
  // const [draftEmail,setEmail]=useState("")
  // const update=()=>{
  //   // const newdraft={...ogMsg}
  //   // newdraft.name= draftName
  //   // newdraft.age= draftAge
  //   // newdraft.phone= draftPhone
  //   // newdraft.email= draftEmail
  //   // setOgMsg(newdraft)
  //   setOgMsg(prev=>({...prev,name:draftName,age:draftAge,phone:draftPhone,email:draftEmail,}))
  // }

  //optimal:
  const[formData,setformData]=useState({
    "name":"",
    "age":"",
    "phone":"",
    "email":"",
  })
  const eventHandler=(eve)=>{
    const{name,value}=eve.target
    setformData(prev=>({
      ...formData,
      [name]:value
    }))
  }
  const submitHandler=(e)=>{
    e.preventDefault()
    setOgMsg(prev=>({
      ...ogMsg,
      name:formData.name || prev.name,
      age:formData.age || prev.age,
      phone:formData.phone || prev.phone,
      email:formData.email || prev.email,

    }))
  }

  return (
    <>
      <div className="counter">
        <h1>{counter}</h1>
        <div className="flex">
          <button
            onClick={function () {
              setCounter(counter + 1);
            }}
          >
            Increase
          </button>

          <button
            onClick={function () {
              setCounter(counter - 1);
            }}
          >
            Decrease
          </button>

          <button
            onClick={function () {
              setCounter(counter + 5);
            }}
          >
            Increase 5
          </button>

          <button
            onClick={function () {
              setCounter(counter - 5);
            }}
          >
            Decrease 5
          </button>
        </div>
      </div>


      <br /><br />
      <div className="details  ">
            <form onSubmit={submitHandler}>
              <h1>Student Details:</h1>
            <br />
            <ul>
              <li>Name: {ogMsg.name}</li>
              <li>Age: {ogMsg.age}</li>
              <li>Phone: {ogMsg.phone}</li>
              <li>Email: {ogMsg.email}</li>
            </ul>
            <br />
            <label>Name: </label>
            <input type="text" name="name" value={formData.name} onChange={function (ele){
              eventHandler(ele)
            }}/> <br /><br />

            <label>Age: </label>
            <input type="number" name="age" value={formData.age} onChange={function (ele){
              eventHandler(ele)
            }}/> <br /><br />

            <label>Phone: </label>
            <input type="phone" name="phone" value={formData.phone} onChange={function (ele){
              eventHandler(ele)
            }}/> <br /><br />

            <label>Email: </label>
            <input type="email" name="email" value={formData.email} onChange={function (ele){
              eventHandler(ele)
            }}/> <br /><br />
            <button>Update</button>
            </form>
      </div>

    </>
  );
}

export default App;
