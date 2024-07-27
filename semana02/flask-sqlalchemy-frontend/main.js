const getMoviesService = async () => {
  const response = await fetch("http://localhost:5000/movies");
  const json = await response.json();
  const status = response.status;
  return { json, status };
};

const postMovieService = async (movie) => {
  const response = await fetch("http://localhost:5000/movies/create", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(movie),
  });
  const json = await response.json();
  const status = response.status;
  return { json, status };
};

const addMovieToList = (moviesList, movie) => {
  const li = document.createElement("li");
  li.appendChild(document.createTextNode(movie.title));
  moviesList.appendChild(li);
};

const handleCreateMovie = (moviesList) => {
  const createMovie = document.getElementById("createMovie");

  createMovie.addEventListener("click", async () => {
    const movie = {
      title: "The Matrix",
      director: "Lana Wachowski",
      year: 1999,
      length_minutes: 136,
    };

    const { json, status } = await postMovieService(movie);

    if (status === 201) {
      alert(json.message);
      addMovieToList(moviesList, movie);
    }
  });
};

const main = async () => {
  const moviesList = document.getElementById("moviesList");

  const { json, status } = await getMoviesService();

  if (status === 200) {
    json.data.forEach((movie) => {
      addMovieToList(moviesList, movie);
    });
  }

  handleCreateMovie(moviesList);
};

main();
