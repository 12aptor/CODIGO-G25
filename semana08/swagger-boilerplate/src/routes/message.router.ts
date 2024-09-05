import { Router } from "express";
import * as messageController from "../controllers/message.controller";

export const messageRouter = Router();

/**
 * @swagger
 * /api/v1/messages/list/{channelId}:
 *   get:
 *     summary: Ruta para listar los mensajes de un canal
 *     description: Listar mensajes de un canal
 *     tags: [Messages]
 *     parameters:
 *       - name: channelId
 *         in: path
 *         description: ID único del canal
 *         required: true
 *         schema:
 *           type: string
 *     responses:
 *       200:
 *         description: Lista de mensajes
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/ListMessagesResponse'
 */
messageRouter.get("/list/:channelId", messageController.listMessages);
