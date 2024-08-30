import { Router } from "express";
import * as authController from "../controllers/auth.controller";

export const authRouter = Router();

authRouter.post("/login", authController.login);
authRouter.post("/register", authController.register);
