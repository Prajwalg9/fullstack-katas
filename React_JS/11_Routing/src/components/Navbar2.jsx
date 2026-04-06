import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

function Navbar() {

    const navigate=useNavigate()

    return ( <>
        <div className="ul" style={{background:"limegreen"}}>
            <button onClick={()=>{navigate('/')}}>Home</button>
            <button onClick={()=>{navigate(-1)}}>Back</button>
            <button onClick={()=>{navigate(+1)}}>Next</button>
        </div>
    </> );
}

export default Navbar;