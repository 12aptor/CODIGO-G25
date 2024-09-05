import express from "express";
import morgan from "morgan";
import cors from "cors";
import dotenv from "dotenv";
import http from "http"; // Modulo nativo de node para crear y manejar servidores
import { Server } from "socket.io";
import swaggerUi from "swagger-ui-express";
import { swaggerSpec } from "./config/swagger";
import { authRouter } from "./routes/auth.router";
import { channelRouter } from "./routes/channel.router";
import { messageRouter } from "./routes/message.router";
import { prisma } from "./config/prisma";

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
app.use("/api/v1/channels", channelRouter);
app.use("/api/v1/messages", messageRouter);

io.on("connection", (socket) => {
  socket.on("join", (channel_id: string) => {
    socket.join(channel_id);
  });

  socket.on("message", async (msg: ISocketMsg) => {
    try {
      const message = await prisma.messages.create({
        data: msg,
        include: {
          author: {
            select: {
              username: true,
            },
          },
        },
      });

      io.to(msg.channel_id).emit("message", message);
    } catch (error) {
      if (error instanceof Error) {
        socket.emit("error", {
          message: "Ocurrio un error al enviar el mensaje",
        });
      }
    }
  });

  socket.on("disconnect", () => {
    console.log("User diconnected");
  });
});

httpServer.listen(port, () => {
  console.log(`Server is running on: http://localhost:${port}`);
});
