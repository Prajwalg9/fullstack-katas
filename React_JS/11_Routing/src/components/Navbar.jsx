import { Link } from "react-router-dom";
function Navbar() {
    return ( <>
        <div className="ul">
            <h2>My App</h2>
            <ul>
                <li><Link to={'/'}>Home</Link></li>
                <li><Link to={'/about'}>About</Link></li>
                <li><Link to={'/courses'}>Courses</Link></li>
                <li><Link to={'/contact'}>Contact</Link></li>
                <li><Link to={'/products'}>Products</Link></li>
            </ul>
        </div>
    </> );
}

export default Navbar;