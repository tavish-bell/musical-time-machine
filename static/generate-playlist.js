document.querySelector("#user-date").addEventListener("submit", (evt) => {
  evt.preventDefault();
  document.querySelector("#user-date").style.display = "none";
  console.log(evt);
  document.querySelector("#header-text").style.display = "none";
  document.querySelector("#musical-messages").style.display = "block";
  document.querySelector("#top-div-heading").style.display = "none";
  document.querySelector("#loading-gif").style.display = "block";
  document.querySelector("#top-section").style.display = "none";

  const formObject = {
    date: document.querySelector("#date").value,
    message: document.querySelector("#message").value,
  };

  console.log(formObject);

  const queryString = new URLSearchParams(formObject).toString();

  const url = `/api/generate-playlist?${queryString}`;

  console.log(url);

  fetch(url)
    .then((res) => res.json())
    .then((json) => {
      console.log(json);
      document.querySelector("#finished-playlist").href = json.spotify_url;
      document.querySelector("#finished-playlist").style.display = "block";
      document.querySelector("#loading-gif").style.display = "none";
    });
});
