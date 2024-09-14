import { Router } from "express";
import * as postController from "../controllers/post.controller";

export const postRouter = Router();

postRouter.post("/create", postController.createPost);
postRouter.get("/list", postController.getPosts);
