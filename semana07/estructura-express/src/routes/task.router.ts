import { Router } from "express";
import * as taskController from "../controllers/task.controller";

export const taskRouter = Router();

taskRouter.get("/list", taskController.listTasks);
taskRouter.get("/by-id/:taskId", taskController.taskById);
taskRouter.post("/create", taskController.createTask);
