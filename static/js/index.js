document.addEventListener("DOMContentLoaded", (event) => {
  setTimeout(() => {
    const alertDiv = document.querySelector(".animate-slide-in-right");
    if (alertDiv) {
      alertDiv.classList.add("animate-fade-out-bottom");

      // Listen for the end of the fade-out animation
      alertDiv.addEventListener(
        "animationend",
        () => {
          alertDiv.classList.add("hidden");
          console.log("hidden ho gaya");
        },
        { once: true }
      );
    }
  }, 3000);
});

function getRandomColor() {
  let hexCode = "123456789ABCDEF";
  let color = "#";
  for (let i = 0; i < 6; i++) {
    color += hexCode.charAt(Math.floor(Math.random() * 16));
  }
  return color;
}

function changeBackgroundColor() {
  document.body.style.backgroundColor = getRandomColor();
}
