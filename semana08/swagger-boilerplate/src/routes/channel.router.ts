import { Router } from "express";
import * as channelController from "../controllers/channel.controller";

export const channelRouter = Router();

channelRouter.post("/create", channelController.createChannel);
channelRouter.get("/list", channelController.listChannels);
