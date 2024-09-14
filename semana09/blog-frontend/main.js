const getPosts = async (page) => {
  try {
    const response = await fetch(
      `http://localhost:3000/api/v1/posts/list?page=${page}&limit=3`
    );

    if (!response.ok) {
      return null;
    }

    const posts = await response.json();
    return posts.data;
  } catch (error) {
    return null;
  }
};

const createPostCard = (post) => {
  const card = document.createElement("div");
  card.className = "post-card";

  const title = document.createElement("h2");
  title.textContent = post.title;

  const content = document.createElement("p");
  content.textContent = post.content;

  card.appendChild(title);
  card.appendChild(content);

  return card;
};

const postList = document.getElementById("post-list");
const renderPosts = async () => {
  const posts = await getPosts(1);

  if (posts) {
    posts.forEach((post) => {
      const postCart = createPostCard(post);
      postList.appendChild(postCart);
    });
  }
};

const nextPageButton = document.getElementById("next-page");
const nextPage = async () => {
  const posts = await getPosts(2);
  postList.innerHTML = "";

  if (posts) {
    posts.forEach((post) => {
      const postCart = createPostCard(post);
      postList.appendChild(postCart);
    });
  }
};

const prevPageButton = document.getElementById("prev-page");
const prevPage = async () => {
  const posts = await getPosts(1);
  postList.innerHTML = "";

  if (posts) {
    posts.forEach((post) => {
      const postCart = createPostCard(post);
      postList.appendChild(postCart);
    });
  }
};

nextPageButton.addEventListener("click", nextPage);
prevPageButton.addEventListener("click", prevPage);

document.addEventListener("DOMContentLoaded", renderPosts);
