document.querySelector("#user-date").addEventListener("submit", (evt) => {
  evt.preventDefault();
  document.querySelector("#user-date").style.display = "none";
  document.querySelector("#header-text").style.display = "none";
  document.querySelector("#musical-messages").style.display = "block";

  const formObject = {
    date: document.querySelector("#date").value,
    message: document.querySelector("#message").value,
  };

  const queryString = new URLSearchParams(formObject).toString();

  const url = `/api/generate-playlist?${queryString}`;

  fetch(url)
    .then((res) => res.json())
    .then((json) => {
      console.log(json);
      document.querySelector("#finished-playlist").href = json.spotify_url;
      document.querySelector("#finished-playlist").style.display = "block";
    });
});
