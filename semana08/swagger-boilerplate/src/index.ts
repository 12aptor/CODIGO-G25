import express from "express";
import morgan from "morgan";
import cors from "cors";
import swaggerUi from "swagger-ui-express";
import { swaggerSpec } from "./config/swagger";
import { authRouter } from "./routes/auth.router";

const app = express();
const port = process.env.PORT || 8000;

app.use(morgan("dev"));
app.use(express.json());
app.use(cors());

app.use("/", swaggerUi.serve, swaggerUi.setup(swaggerSpec));
app.use("/api/v1/auth", authRouter);

app.listen(port, () => {
  console.log(`Server is running on: http://localhost:${port}`);
});
