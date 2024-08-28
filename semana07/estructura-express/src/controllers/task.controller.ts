import { Request, Response } from "express";

export const listTasks = (req: Request, res: Response) => {
    return res.send("Listar tareas");
};
