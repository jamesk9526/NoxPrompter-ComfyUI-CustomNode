// This file contains the JavaScript code for the prompt generator.
// It handles user interactions, generates prompts based on user input, and updates the webpage dynamically.

document.addEventListener("DOMContentLoaded", function() {
    const promptButton = document.getElementById("generate-prompt");
    const promptOutput = document.getElementById("prompt-output");

    const prompts = [
        "What inspires you today?",
        "Describe your ideal day.",
        "What is a challenge you want to overcome?",
        "Write about a memorable experience.",
        "What are your goals for the next month?"
    ];

    promptButton.addEventListener("click", function() {
        const randomIndex = Math.floor(Math.random() * prompts.length);
        promptOutput.textContent = prompts[randomIndex];
    });
});