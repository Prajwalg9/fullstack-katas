import React,{useContext,createContext, useState} from "react";

const ThemeContext=createContext()

function ThemeProvider({children}){
    const [theme,setTheme]=useState('light')
    function toggleTheme(){
        setTheme(prev=>(prev==='light'?'dark':'light'))
    }

    return(
        <ThemeContext.Provider value={{theme,toggleTheme}}>
            {children}
        </ThemeContext.Provider>
    )
}




function Home(){
    const {theme,toggleTheme}=useContext(ThemeContext)
    return (<div className="bg" style={{background:theme==="light"?"#fff":"#000",color:theme==="dark"?"#fff":"#222"}}>
        <h1>{theme} theme</h1>
        <button onClick={toggleTheme}>Change Theme</button>
    </div>)
}

function App() {
    return ( <>
        <ThemeProvider>
            <Home></Home>
        </ThemeProvider>
    </> );
}

export default App;