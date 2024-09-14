import express from "express";
import cors from "cors";
import { postRouter } from "./routes/post.router";
import { userRouter } from "./routes/user.router";
import { commentRouter } from "./routes/comment.router";

const app = express();
const port = 3000;

app.use(express.json());
app.use(cors());

app.use("/api/v1/posts", postRouter);
app.use("/api/v1/users", userRouter);
app.use("/api/v1/comments", commentRouter);

app.listen(port, () => {
  console.log(`Running app: http://localhost:${port}`);
});
