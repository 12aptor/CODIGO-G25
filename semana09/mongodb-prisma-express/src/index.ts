import express from "express";
import { postRouter } from "./routes/post.router";
import { userRouter } from "./routes/user.router";

const app = express();
const port = 3000;

app.use(express.json());

app.use("/api/v1/posts", postRouter);
app.use("/api/v1/users", userRouter);

app.listen(port, () => {
  console.log(`Running app: http://localhost:${port}`);
});
