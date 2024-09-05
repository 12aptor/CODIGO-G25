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
 *               $ref: '#/components/schemas/Channel'   
*/
channelRouter.post("/create", channelController.createChannel);
channelRouter.get("/list", channelController.listChannels);
