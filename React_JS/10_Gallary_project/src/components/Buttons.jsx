function Buttons({ index, setIndex }) {
  return (
    <>
      <div className="flex items-center justify-center gap-10 mb-10">
        <button
          style={{opacity:index==1?0.5:1}}
          className="bg-sky-500/75 px-3 py-1 rounded text-white cursor-pointer"
          onClick={() => {
            {
              if (index > 1) {
                setIndex(index - 1);
              }
            }
          }}
        >
          Previous
        </button>
        <button
          className="bg-sky-500/75 px-3 py-1 rounded text-white cursor-pointer"
          onClick={() => setIndex((prev) => prev + 1)}
        >
          Next
        </button>
      </div>
    </>
  );
}

export default Buttons;
