"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const morgan_1 = __importDefault(require("morgan"));
const cors_1 = __importDefault(require("cors"));
const dotenv_1 = __importDefault(require("dotenv"));
const http_1 = __importDefault(require("http")); // Modulo nativo de node para crear y manejar servidores
const socket_io_1 = require("socket.io");
const swagger_ui_express_1 = __importDefault(require("swagger-ui-express"));
const swagger_1 = require("./config/swagger");
const auth_router_1 = require("./routes/auth.router");
const channel_router_1 = require("./routes/channel.router");
const message_router_1 = require("./routes/message.router");
const prisma_1 = require("./config/prisma");
const storage_1 = require("firebase/storage");
const firebase_1 = require("./config/firebase");
dotenv_1.default.config();
const app = (0, express_1.default)();
const port = process.env.PORT || 8000;
const httpServer = http_1.default.createServer(app); // Crear un servidor
const io = new socket_io_1.Server(httpServer, {
    cors: {
        origin: "*",
    },
});
app.use((0, morgan_1.default)("dev"));
app.use(express_1.default.json());
app.use((0, cors_1.default)());
app.use("/swagger", swagger_ui_express_1.default.serve, swagger_ui_express_1.default.setup(swagger_1.swaggerSpec));
app.use("/api/v1/auth", auth_router_1.authRouter);
app.use("/api/v1/channels", channel_router_1.channelRouter);
app.use("/api/v1/messages", message_router_1.messageRouter);
io.on("connection", (socket) => {
    socket.on("join", (channel_id) => {
        socket.join(channel_id);
    });
    socket.on("message", (msg) => __awaiter(void 0, void 0, void 0, function* () {
        try {
            const storage = (0, storage_1.getStorage)(firebase_1.firebaseApp);
            const message = yield prisma_1.prisma.messages.create({
                data: msg,
                include: {
                    author: {
                        select: {
                            avatar: true,
                            username: true,
                        },
                    },
                },
            });
            const storageRef = (0, storage_1.ref)(storage, `users/avatars/${message.author.avatar}`);
            const avatarUrl = yield (0, storage_1.getDownloadURL)(storageRef);
            io.to(msg.channel_id).emit("message", Object.assign(Object.assign({}, message), { author: Object.assign(Object.assign({}, message.author), { avatar: avatarUrl }) }));
        }
        catch (error) {
            if (error instanceof Error) {
                socket.emit("error", {
                    message: "Ocurrio un error al enviar el mensaje",
                });
            }
        }
    }));
    socket.on("disconnect", () => {
        console.log("User diconnected");
    });
});
httpServer.listen(port, () => {
    console.log(`Server is running on: http://localhost:${port}`);
});
