import express from "express";
import morgan from "morgan";
import cors from "cors";
import dotenv from "dotenv";
import http from "http"; // Modulo nativo de node para crear y manejar servidores
import { Server } from "socket.io";
import swaggerUi from "swagger-ui-express";
import { swaggerSpec } from "./config/swagger";
import { authRouter } from "./routes/auth.router";

dotenv.config();

const app = express();
const port = process.env.PORT || 8000;

const httpServer = http.createServer(app); // Crear un servidor
const io = new Server(httpServer, {
  cors: {
    origin: "*",
  },
});

app.use(morgan("dev"));
app.use(express.json());
app.use(cors());

app.use("/swagger", swaggerUi.serve, swaggerUi.setup(swaggerSpec));
app.use("/api/v1/auth", authRouter);

io.on("connection", (socket) => {
  socket.on("message", (msg) => {
    console.log(msg);
  });

  socket.on("disconnect", () => {
    console.log("User diconnected");
  });
});

httpServer.listen(port, () => {
  console.log(`Server is running on: http://localhost:${port}`);
});
