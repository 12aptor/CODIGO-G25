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
exports.listChannels = exports.createChannel = void 0;
const zod_1 = require("zod");
const channel_schema_1 = require("../schemas/channel.schema");
const prisma_1 = require("../config/prisma");
const createChannel = (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const validatedData = channel_schema_1.ChannelSchema.parse(req.body);
        const channel = yield prisma_1.prisma.channels.create({
            data: validatedData,
        });
        return res.status(201).json({
            message: "Canal creado exitosamente",
            data: channel,
        });
    }
    catch (error) {
        if (error instanceof zod_1.ZodError) {
            return res.status(400).json({
                message: "Error en la validación de datos",
                error: error.errors,
            });
        }
        if (error instanceof Error) {
            return res.status(500).json({
                message: "Ha ocurrido un error",
                error: error.message,
            });
        }
    }
});
exports.createChannel = createChannel;
const listChannels = (_req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const channels = yield prisma_1.prisma.channels.findMany();
        return res.status(200).json({
            message: "Canales obtenidos exitosamente",
            data: channels,
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
exports.listChannels = listChannels;
