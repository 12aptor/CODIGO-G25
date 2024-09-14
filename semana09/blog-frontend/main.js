const getPosts = async () => {
  try {
    const response = await fetch("http://localhost:3000/api/v1/posts/list");

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

const renderPosts = async () => {
  const postList = document.getElementById("post-list");

  const posts = await getPosts();

  if (posts) {
    posts.forEach((post) => {
      const postCart = createPostCard(post);
      postList.appendChild(postCart);
    });
  }
};

document.addEventListener("DOMContentLoaded", renderPosts);
