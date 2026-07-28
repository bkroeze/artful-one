document.addEventListener("DOMContentLoaded", () => {
  const root = document.getElementById("contact-retro-futurism");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (!root || reducedMotion.matches) return;

  let timer;
  const play = () => {
    root.classList.remove("is-playing");
    void root.offsetWidth;
    root.classList.add("is-playing");
  };
  const start = () => {
    window.clearInterval(timer);
    play();
    timer = window.setInterval(play, 7000);
  };
  const handleVisibility = () => {
    if (document.hidden) {
      window.clearInterval(timer);
      return;
    }
    start();
  };

  document.addEventListener("visibilitychange", handleVisibility);
  start();
});
