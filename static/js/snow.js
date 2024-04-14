document.addEventListener("DOMContentLoaded", function () {
  const snowflakesContainer = document.querySelector(".snowflakes");
  const numberOfSnowflakes = 100; // Adjust the number of snowflakes

  for (let i = 0; i < numberOfSnowflakes; i++) {
    createSnowflake();
  }

  function createSnowflake() {
    const snowflake = document.createElement("div");
    snowflake.classList.add("snowflake");
    snowflake.style.left = `${Math.random() * 100}vw`;
    snowflake.style.animationDuration = `${Math.random() * 10 + 5}s`;
    snowflake.style.animationDelay = `${Math.random() * 5}s`;
    snowflake.style.fontSize = `${Math.random() * 10 + 5}px`;
    snowflake.style.opacity = `${Math.random() * 0.5 + 0.5}`;
    snowflakesContainer.appendChild(snowflake);
  }
});
