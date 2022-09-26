document.querySelector("#user-date").addEventListener("submit", (evt) => {
  evt.preventDefault();

  const date = evt.target.querySelector("input").value;

  fetch("/api/generate-playlist?" + "date=" + date)
    .then((res) => {
      res.json();
    })
    .then((json) => {
      // where updating DOM would happen / next steps
      console.log(json);
    });
});
