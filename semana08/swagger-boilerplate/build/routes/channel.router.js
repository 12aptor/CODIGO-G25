"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.channelRouter = void 0;
const express_1 = require("express");
const channelController = __importStar(require("../controllers/channel.controller"));
exports.channelRouter = (0, express_1.Router)();
/**
 * @swagger
 * /api/v1/channels/create:
 *   post:
 *     summary: Ruta para crear canal
 *     description: Crear un canal
 *     tags: [Channels]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             $ref: '#/components/schemas/Channel'
 *     responses:
 *       201:
 *         description: Canal creado exitosamente
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/CreateChannelResponse'
 */
exports.channelRouter.post("/create", channelController.createChannel);
/**
 * @swagger
 * /api/v1/channels/list:
 *   get:
 *     summary: Ruta para listar canales
 *     description: Listar canales
 *     tags: [Channels]
 *     responses:
 *       200:
 *         description: Lista de canales
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/ListChannelResponse'
 */
exports.channelRouter.get("/list", channelController.listChannels);
