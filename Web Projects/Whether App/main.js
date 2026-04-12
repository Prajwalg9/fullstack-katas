function updateTime() {
    const now = new Date();
    const timeString = now.toLocaleTimeString();
    document.getElementById("timenow").textContent = timeString;
}

setInterval(updateTime, 1000);
updateTime(); // run immediately



const getWhetherBtn = document.querySelector("#getWhetherBtn");

getWhetherBtn.addEventListener("click", async () => {
    try {
        const city = document.getElementById("cityInput").value;
        const response = await fetch(`https://api.weatherapi.com/v1/current.json?key=a2248a36abb2466aa0f104214261603&q=${city}`);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        const impData = {
            location: data.location.name+",",
            whetherimg: data.current.condition.icon,
            region: data.location.region+",",
            country: data.location.country,
            temp: data.current.temp_c+" °C",
            condition: data.current.condition.text,
            humidity: data.current.humidity,
            feelslike: data.current.feelslike_c+" °C",
            heatindex: data.current.heatindex_c+" °C",
            dewpoint: data.current.dewpoint_c+" °C",
            windspeed: data.current.wind_kph+" kph",
            pressure: data.current.pressure_mb+" mb"
        };

        const uiElements = {
            location: document.querySelector("#location"),
            whetherimg: document.querySelector("#whetherimg"),
            temp: document.querySelector("#temp"),
            condition: document.querySelector("#condition"),
            region: document.querySelector("#region"),
            country: document.querySelector("#country"),
            humidity: document.querySelector("#humidity"),
            windspeed: document.querySelector("#windspeed"),
            feelslike: document.querySelector("#feelslike"),
            heatindex: document.querySelector("#heatindex"),
            dewpoint: document.querySelector("#dewpoint"),
            pressure: document.querySelector("#pressure")
        };
        document.querySelector('.whetherContainer').classList.add('active');
        for (const key in uiElements) {
            if(uiElements[key]){
                uiElements[key].innerText=impData[key]
            }
        }
    } catch (error) {
        console.error("Fetch failed:", error);
    }
});

