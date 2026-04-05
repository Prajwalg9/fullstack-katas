function Body(props) {
  return (
    <>
      <div className="grid grid-cols-4 gap-6 m-7">
        {props.Images.map((img)=>(
            <a href={img.url} key={img.id}>
                <div className="bg-slate-900 h-[220px] p-2 rounded-xl flex flex-col items-center justify-between">
                    <img src={img.download_url} className="w-full h-3/4 rounded-xl" />
                    <h3 className="mb-2 text-white font-bold">{img.author}</h3>
                </div>
            </a>
        ))}
      </div>
    </>
  );
}

export default Body;
