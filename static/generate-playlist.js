document.querySelector("#top-div").addEventListener("submit", (evt) => {
  evt.preventDefault();

  // const date = evt.target.querySelector("input").value;

  fetch("/api/generate-playlist?")
    // fetching msg data from Playlist table to display
    .then((res) => {
      res.json();
    })
    .then((json) => {
      // set top div to None, set bottom div to block
      // update DOM with info retrieved from fetch
      console.log(json);
    });
});
