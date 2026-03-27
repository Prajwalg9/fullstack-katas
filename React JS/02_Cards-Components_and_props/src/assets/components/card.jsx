const Card = ({info}) => {
  const { 
    profileImage = "https://via.placeholder.com/150",
    firstName = "Anonymous", 
    lastName = "", 
    age = "??",
    jobTitle = "Professional",
    company = "N/A",
    rating = 0,
    projectsCompleted = 0,
    experience = 0,
    bio = "No bio provided.",
    email = "N/A",
    phone = "N/A",
    location = "N/A",
    education = "N/A",
    languages = [], // Default to empty array to prevent .join() crash
    hobbies = [],   // Default to empty array to prevent .join() crash
    skills = [],    // Default to empty array to prevent .map() crash
    linkedin = "#",
    github = "#",
    website = "#"
  } = info;


  return (
    <div className="relative mt-10 bg-gray-800 text-gray-300 w-full max-w-[280px] rounded-xl border border-gray-700 flex flex-col p-5 pt-12 shadow-2xl shadow-black">
      
      <div className="absolute -top-10 left-1/2 -translate-x-1/2">
        <img 
          src={profileImage}
          className="w-20 h-20 rounded-full border-4 border-gray-800 bg-gray-800 p-1 object-cover" 
          alt="User" 
        />
      </div>

      <div className="flex flex-col items-center text-center mb-6">
        <h2 className="capitalize font-bold text-white text-lg">{firstName} {lastName}- {age}</h2>
        <p className="capitalize text-sm text-gray-400">{jobTitle}</p>
        <p className="capitalize text-xs text-gray-500">{company}</p>
      </div>

      <div className="grid grid-cols-3 gap-2 text-center border-y border-gray-700 py-4 mb-4">
        <div>
          <div className="flex items-center justify-center gap-1 text-white">
            <i className="fa-solid fa-star text-xs text-yellow-500"></i> 
            <span className="font-bold">{rating}</span>
          </div>
          <p className="text-[10px] uppercase tracking-wider">Rating</p>
        </div>
        <div>
          <div className="flex items-center justify-center gap-1 text-white">
            <i className="fa-solid fa-check text-xs text-green-500"></i>
            <span className="font-bold">{projectsCompleted}</span>
          </div>
          <p className="text-[10px] uppercase tracking-wider">Projects</p>
        </div>
        <div>
          <div className="flex items-center justify-center gap-1 text-white">
            <i className="fa-solid fa-toolbox text-xs text-blue-500"></i> 
            <span className="font-bold">{experience} yrs</span>
          </div>
          <p className="text-[10px] uppercase tracking-wider">Experience</p>
        </div>
      </div>

      {/* ABOUT SECTION */}
      <div className="mb-4">
        <h3 className="font-bold text-xs text-white uppercase mb-1">About</h3>
        <p className="text-xs leading-relaxed text-gray-400">
          {bio}
        </p>
      </div>

      {/* 5. 6-ITEM CONTACT GRID */}
      <div className="grid grid-cols-2 gap-y-3 px-4 pb-4 border-b border-gray-800">
        <div className="flex items-center gap-2">
          <i className="fa-solid fa-at text-blue-500 text-xs w-4"></i>
          <span className="text-[10px] truncate max-w-[100px]">{email}</span>
        </div>
        <div className="flex items-center gap-2">
          <i className="fa-solid fa-phone text-green-500 text-xs w-4"></i>
          <span className="text-[10px]">{phone}</span>
        </div>
        <div className="flex items-center gap-2">
          <i className="fa-solid fa-location-dot text-red-500 text-xs w-4"></i>
          <span className="text-[10px]">{location}</span>
        </div>
        <div className="flex items-center gap-2">
          <i className="fa-solid fa-graduation-cap text-purple-500 text-xs w-4"></i>
          <span className="text-[10px]">{education}</span>
        </div>
        <div className="flex items-center gap-2">
          <i className="fa-solid fa-language text-yellow-500 text-xs w-4"></i>
          <span className="text-[10px]">{languages.join(', ')}</span>
        </div>
        <div className="flex items-center gap-2">
          <i className="fa-solid fa-heart text-pink-500 text-xs w-4"></i>
          <span className="text-[10px]">{hobbies.join(', ')}</span>
        </div>
      </div>

      {/* SKILLS */}
      <div className="mb-6">
        <h3 className="font-bold text-xs text-white uppercase mb-2">Skills</h3>
        <div className="flex flex-wrap gap-2">
          {skills.map(skill => (
            <span key={skill} className="bg-gray-700 px-2 py-1 rounded text-[10px] text-gray-200">
              {skill}
            </span>
          ))}
        </div>
      </div>

      {/* FOOTER LINKS */}
      <div className="flex justify-between gap-1 items-center pt-4 border-t border-gray-700">
        <a href={linkedin} className="hover:text-white transition-colors text-xs"><i className="fa-brands fa-linkedin text-lg"></i> LinkedIn</a>
        <a href={github} className="hover:text-white transition-colors text-xs"><i className="fa-brands fa-github text-lg"></i> Github</a>
        <a href={website} className="hover:text-white transition-colors text-xs"><i className="fa-solid fa-globe text-lg"></i> Portfolio</a>
      </div>
    </div>
  );
};
export default Card;