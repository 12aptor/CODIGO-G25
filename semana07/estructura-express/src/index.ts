import express from "express";
import morgan from "morgan";
import cors from "cors";
import { authMiddleware } from "./config/middleware";
import { taskRouter } from "./routes/task.router";
import { authRouter } from "./routes/auth.router";
import { swaggerSpec } from "./config/swagger";
import swaggerUi from "swagger-ui-express";

const app = express();
const port = 8000;

app.use(express.json());
app.use(morgan("dev"));
// app.use(cors({
// origin: "http://localhost:3000",
// origin: ["http://localhost:3000", "http://localhost:3001"],
// }));
app.use(cors());

app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerSpec));
app.use("/api/v1/task", authMiddleware, taskRouter);
app.use("/api/v1/auth", authRouter);

app.listen(port, () => {
  console.log(`Running app: http://localhost:${port}`);
});
