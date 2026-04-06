import { useParams } from "react-router-dom";

function Details() {
    const params=useParams()
    return ( <>
        <h1>{params.id} Course Details</h1>
    </> );
}

export default Details;