console.log("script.js loaded");

const container = document.getElementById("drawflow");
const editor = new Drawflow(container);

// Enable plugins & start editor
editor.reroute = true;
editor.start();


// ---------------------------------------------------
// LOAD DIAGRAM FROM FASTAPI
// ---------------------------------------------------
async function loadDiagram() {
    try {
        const response = await fetch("/diagram");
        const data = await response.json();

        console.log("Loaded diagram:", data);

        if (Object.keys(data).length === 0) {
            console.log("Empty diagram.json → starting with an empty editor");
            return;
        }

        editor.import(data);

    } catch (err) {
        console.error("Error loading diagram:", err);
    }
}


// ---------------------------------------------------
// SAVE DIAGRAM TO FASTAPI
// -----
