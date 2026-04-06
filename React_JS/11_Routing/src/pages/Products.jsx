import { Link, Outlet } from "react-router-dom";

function Products() {
    return ( <>
        <div className="links">
            <Link to={'/products/men'}>Men</Link>
            <Link to={'/products/women'}>Women</Link>
            <Link to={'/products/kids'}>Kids</Link>
            <Outlet></Outlet>
        </div>
    
    </> );
}

export default Products;