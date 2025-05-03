function addToLog(message) {
    const infoBlock = _cloneAnswerBlock();
    
    if (!infoBlock) {
        console.error("Échec de la création du bloc d'information");
        return null;
    }
    
    infoBlock.innerText = message;
    return infoBlock;
}

function _cloneAnswerBlock() {
    const output = document.querySelector("#gpt-output");
    const template = document.querySelector('#chat-template');
    const clone = template.cloneNode(true);
    clone.id = "";
    output.prepend(clone);
    clone.classList.remove("hidden")
    return clone.querySelector(".message");
}

async function fetchPromptResponse(prompt) {
    const response = await fetch("/prompt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt }),
    });

    // Si la réponse est au format JSON, on utilise response.json()
    if (response.ok) {
        const data = await response.json();  // Récupérer directement l'objet JSON
        return data;  // Renvoie l'objet JSON
    } else {
        throw new Error("Une erreur est survenue lors de la requête");
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("#prompt-form");
    const spinnerIcon = document.querySelector("#spinner-icon");
    const sendIcon = document.querySelector("#send-icon");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        spinnerIcon.classList.remove("hidden");
        sendIcon.classList.add("hidden");
    
        const prompt = form.elements.prompt.value;
    
        try {
            const data = await fetchPromptResponse(prompt);  // Nous attendons maintenant directement l'objet JSON
            
            // Ici, `data` est déjà un objet JSON, donc pas besoin de vérifier `response.ok` ni d'utiliser `response.json()`
            addToLog(data.message);  // Affiche la clé `messages` dans le log

        } catch (error) {
            console.error('Une erreur est survenue lors de la requête:', error);  // Capture les erreurs de type fetch ou de réseau
        } finally {
            spinnerIcon.classList.add("hidden");
            sendIcon.classList.remove("hidden");
            hljs.highlightAll();
        }
    });    
});
