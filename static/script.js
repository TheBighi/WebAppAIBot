document.getElementById("chatForm").addEventListener("submit", function(event) {
    event.preventDefault();
    let message = document.getElementById("message").value.trim();
    
    if (!message) return;

    let chatBox = document.getElementById("chatBox");

    function appendMessage(text, className) {
        let msgDiv = document.createElement("div");
        msgDiv.textContent = text;
        msgDiv.classList.add("message", className);
        chatBox.appendChild(msgDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    appendMessage("You: " + message, "user");

    document.getElementById("message").value = "";

    // Send message to Flask backend
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => appendMessage("Bot: " + data.reply, "bot"))
    .catch(error => console.error("Error:", error));
});