import Navbar from "./components/Navbar";
import { Route,Routes } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import Contact from "./pages/Contact";
import NotFound from "./pages/404";
import Products from "./pages/Products";
import Men from "./components/men";
import Women from "./components/women";
import Kids from "./components/kids";
import Courses from "./pages/Courses";
import Details from "./components/Details";
import Navbar2 from "./components/Navbar2";

function App() {
    return ( <>
        <Navbar></Navbar>
        <Navbar2></Navbar2>
        <Routes>
            <Route path="/" element={<Home></Home>} />
            <Route path="/about" element={<About></About>} />
            <Route path="/contact" element={<Contact></Contact>} />
            <Route path="/products" element={<Products></Products>}>
                {/* Nested Routes  */}
                <Route path="men" element={<Men></Men>}></Route>
                <Route path="women" element={<Women></Women>}></Route>
                <Route path="kids" element={<Kids></Kids>}></Route>
            </Route>
            <Route path="/courses" element={<Courses></Courses>}></Route>
            <Route path="/courses/:id" element={<Details></Details>}/>
            <Route path="/*" element={<NotFound></NotFound>}></Route>
        </Routes>
    </> );
}

export default App;