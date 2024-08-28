import express from "express";
import { taskRouter } from "./routes/task.router";

const app = express();
const port = 8000;

app.use("/task", taskRouter);

app.listen(3000, () => {
  console.log(`Running app: http://localhost:${port}`);
});
