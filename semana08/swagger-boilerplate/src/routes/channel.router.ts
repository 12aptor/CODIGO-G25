import { Router } from "express";
import * as channelController from "../controllers/channel.controller";

export const channelRouter = Router();

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
channelRouter.post("/create", channelController.createChannel);

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
channelRouter.get("/list", channelController.listChannels);
