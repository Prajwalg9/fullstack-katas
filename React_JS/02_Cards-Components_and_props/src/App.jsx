import Card from "./assets/components/card";
import data from "./assets/data/dataset.json"

function App() {
  const dataset=data
  return <div className="grid grid-cols-1 md:grid-cols-3 sm:grid-cols-2 gap-y-15 gap-x-5 justify-items-center m-5 ">
    {dataset.map((element)=>(
      <Card key={element.id} info={element} />
    ))}
  </div>
}

export default App;