document.querySelector("#user-date").addEventListener("submit", (evt) => {
  evt.preventDefault();
  // hiding top section, show bottom section--> display=None
  const formObject = {
    date: document.querySelector("#date").value,
    message: document.querySelector("#message").value,
  };

  const queryString = new URLSearchParams(formObject).toString();

  const url = `/api/generate-playlist?${queryString}`;

  fetch(url)
    // fetching msg data from Playlist table to display
    .then((res) => res.json())
    .then((json) => {
      // set top div to None, set bottom div to block
      console.log(json);
      //have url open in new tab with target=blank --> figure out where to put that syntax
      document.querySelector("#finished-playlist").href = json.spotify_url;
      // revealing href with finished playlist happens here
    });
});

//   <!-- style.display set to None (to hide)-->
// <!-- default style set to None, appear when JS happens-->
