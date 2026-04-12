const dropdowns = document.querySelectorAll(".dropdown select");
const message = document.querySelector(".message");
const convertBtn = document.querySelector("#convert-btn");
const amountInput = document.querySelector("#amount");
const fromSelect = document.querySelector("#from");
const toSelect = document.querySelector("#to");

const updateFlag = (element) => {
    const countryCode = countryList[element.value];
    const flagImg = element.parentElement.querySelector("img");
    flagImg.src = `https://flagsapi.com/${countryCode}/flat/64.png`;
};

dropdowns.forEach((dropdown) => {
    for (let code in countryList) {
        let newOption = document.createElement("option");
        newOption.value = code;
        newOption.innerText = code;
        
        if (dropdown.id === "from" && code === "USD") {
            newOption.selected = "selected";
        } else if (dropdown.id === "to" && code === "INR") {
            newOption.selected = "selected";
        }
        
        dropdown.appendChild(newOption);
    }

    updateFlag(dropdown);
    
    dropdown.addEventListener("change", (evt) => {
        updateFlag(evt.target);
    });
});

convertBtn.addEventListener("click", (evt) => {
    evt.preventDefault();
    let amount = amountInput.value;
    const from = fromSelect.value;
    const to = toSelect.value;

    if (amount === "" || amount <= 0) {
        alert("Please enter a valid amount greater than zero.");
        amountInput.value = "1";
        amount = 1;
    }

    if (from === to) {
        message.innerText = `${amount} ${from} = ${amount} ${to}`;
        return;
    }
    
    convertCurrency(amount, from, to);
});

async function convertCurrency(amount, from, to) {
    try {
        message.innerText = "Fetching real-time data... ⏳";
        const response = await fetch(`https://api.frankfurter.dev/v1/latest?base=${from}&symbols=${to}`);
        
        if (!response.ok) {
            throw new Error(`HTTP Error! Status: ${response.status}`);
        }
        if (response.status === 404) {
            throw new Error("UNSUPPORTED_CURRENCY");
        }
        const data = await response.json();
        const conversion = amount * data.rates[to];
        message.innerText = `${amount} ${from} = ${conversion.toFixed(2)} ${to}`;
        
    } catch (error) {
        message.innerText = "🚨 Error: Unable to fetch exchange rates. Please try again later.";
    }
}