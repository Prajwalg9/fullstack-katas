function Navbar() {
    return ( <>
        <nav className="flex items-center justify-around mx-10 **:textwhite">
            <h1 className="flex items-center justify-between text-sm font-bold gap-2"><i className="ri-global-line"></i> Asia</h1>
            <ul className="flex items-center justify-around *:text-xs gap-4 *:px-4 *:py-2 *:border-b-2 *:border-transparent *:hover:border-blue-500 *:transition-all *:duration-300 *:hover:text-sky-600">
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
            <button className="font-bold"><i className="ri-search-line"></i></button>
        </nav>
    </> );
}

export default Navbar;