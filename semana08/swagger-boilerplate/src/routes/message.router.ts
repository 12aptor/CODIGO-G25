import { Router } from "express";
import * as messageController from "../controllers/message.controller";

export const messageRouter = Router();

messageRouter.get("/list/:channelId", messageController.listMessages);
