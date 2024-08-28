import { Router } from "express";
import { listTasks } from "../controllers/task.controller";

export const taskRouter = Router();

taskRouter.get("/list", listTasks);
taskRouter.post("/create", (req, res) => {});
taskRouter.put("/update", (req, res) => {});
taskRouter.delete("/delete", (req, res) => {});
