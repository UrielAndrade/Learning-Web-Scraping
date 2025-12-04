async function runPython() {
  const res = await fetch("/run-python");
  const data = await res.text();

  const out = document.getElementById("resultado");
  out.textContent = data;  
}

document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("scraping");
  btn.addEventListener("click", () => runPython());
});
