import Card from "./Cards";
import Content from "./Content";

function Body(props) {
    console.log(props.info)
    return ( <div className="flex w-full h-screen">
        <Content />
        <Card />
    </div> );
}

export default Body;