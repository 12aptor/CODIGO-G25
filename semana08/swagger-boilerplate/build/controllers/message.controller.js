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
Object.defineProperty(exports, "__esModule", { value: true });
exports.listMessages = void 0;
const prisma_1 = require("../config/prisma");
const storage_1 = require("firebase/storage");
const firebase_1 = require("../config/firebase");
const listMessages = (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const channelId = req.params.channelId;
        const messages = yield prisma_1.prisma.messages.findMany({
            where: {
                channel_id: channelId,
            },
            include: {
                author: {
                    select: {
                        avatar: true,
                        username: true,
                    },
                },
            },
        });
        let newMessages = [];
        const storage = (0, storage_1.getStorage)(firebase_1.firebaseApp);
        for (let i = 0; i < messages.length; i++) {
            const message = messages[i];
            const storageRef = (0, storage_1.ref)(storage, `users/avatars/${message.author.avatar}`);
            const avatarUrl = yield (0, storage_1.getDownloadURL)(storageRef);
            newMessages.push(Object.assign(Object.assign({}, message), { author: Object.assign(Object.assign({}, message.author), { avatar: avatarUrl }) }));
        }
        return res.status(200).json({
            message: "Mensajes obtenidos exitosamente",
            data: newMessages,
        });
    }
    catch (error) {
        if (error instanceof Error) {
            return res.status(500).json({
                message: "Ha ocurrido un error",
                error: error.message,
            });
        }
    }
});
exports.listMessages = listMessages;
