import { useState } from "react";

function App() {
  const [inputs, setInputs] = useState([]);
  const [draftInputs, setDraftInputs] = useState({
    title: "",
    description: "",
  });

  function submitHandler(e) {
    e.preventDefault();
    setInputs((prev) => [...inputs, draftInputs]);
    setDraftInputs({
      title: "",
      description: "",
    });
  }
  function inputhandler(e) {
    const { name, value } = e.target;
    setDraftInputs((prev) => ({
      ...draftInputs,
      [name]: value,
    }));
    console.log(value);
  }
  function deleteItem(idx) {
    const tasks = [...inputs];
    tasks.splice(idx, 1);
    setInputs(tasks);
  }

  return (
    <>
      <div className="md:flex items-center justify-between h-screen w-screen gap-15 overflow-hidden p-10">
        <form
          className="flex flex-col items-center md:w-1/2 justify-center"
          onSubmit={function (e) {
            submitHandler(e);
          }}
        >
          <input
            className="border-2 text-white border-white p-2 outline-0 rounded-xs w-full md:w-full"
            name="title"
            required
            type="text"
            value={draftInputs.title}
            placeholder="Enter Title of task"
            onChange={function (e) {
              inputhandler(e);
            }}
          />
          <br />

          <textarea
            className="border-2 text-white border-white p-2 outline-0 rounded-xs w-full w-full"
            name="description"
            required
            type="textarea"
            value={draftInputs.description}
            placeholder="Enter Details"
            rows="5"
            onChange={function (e) {
              inputhandler(e);
            }}
          />
          <br />
          <button className="bg-white rounded-2xl text-black px-4 p-2 w-full">
            + Add Task
          </button>
        </form>
        <div className="w-full h-full md:border-l-2 md:border-l-white overflow-y-auto ">
          <h1 className="text-white text-4xl p-5 font-bold sticky top-0 bg-slate-950">
            Tasks{" "}
          </h1>
          <ul className="flex flex-col gap-5">
            {inputs.length === 0 ? (
              <h1 className="text-white p-10">No tasks avalible.</h1>
            ) : (
              inputs.map((task, index) => {
                return (
                  <li
                    key={index}
                    className="bg-[#25a6af] flex items-center justify-around mx-7 rounded-xs"
                  >
                    <div className="flex justify-between gap-10 p-2">
                      <h1 className="ml-4">{index + 1}</h1>
                      <input
                        type="checkbox"
                        className="accent-pink-600 p-2"
                        name="status"
                      />
                    </div>
                    <div className="p-2 w-[70%]">
                      <h1 className="font-bold capitalize">{task.title}</h1>
                      <p className="text-gray-900 capitalize">
                        {task.description}
                      </p>
                    </div>
                    <button
                      onClick={() => {
                        deleteItem(index);
                      }}
                      className="bg-red-600 text-white px-3 py-1 mr-4 rounded-2xl"
                    >
                      Delete
                    </button>
                  </li>
                );
              })
            )}
          </ul>
        </div>
      </div>
    </>
  );
}

export default App;
