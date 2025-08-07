async function fetchAPOD() {
    const response = await fetch('/apod-data');
    const data = await response.json();

    document.getElementById('apod-title').innerText = data.title;
    document.getElementById('apod-image').src = data.hdurl; // Use hdurl for high-definition image
    document.getElementById('apod-explanation').innerText = data.explanation;
}

window.onload = fetchAPOD; // Call the function when the window loads