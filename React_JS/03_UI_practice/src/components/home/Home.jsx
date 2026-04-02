import Navbar from "./main/navbar/Navbar";
import Body from "./main/Body/Body";
import london from "../../assets/london.png";

function Home(props) {
    return ( <div>
        <Navbar></Navbar>
        <Body data={props.info}></Body>
    </div> );
}

export default Home;