import express from "express";
import { taskRouter } from "./routes/task.router";
import morgan from "morgan";

const app = express();
const port = 8000;

app.use(express.json());
app.use(morgan("dev"));

app.use("/api/v1/task", taskRouter);

app.listen(port, () => {
  console.log(`Running app: http://localhost:${port}`);
});
