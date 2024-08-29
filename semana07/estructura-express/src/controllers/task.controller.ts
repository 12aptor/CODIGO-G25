import { Request, Response } from "express";
import { IApiResponse, ITask } from "../types";
import { TaskSchema } from "../schemas/task.schema";
import { ZodError } from "zod";

let tasks: ITask[] = [
  {
    id: 1,
    name: "Tarea 1",
  },
  {
    id: 2,
    name: "Tarea 2",
  },
];

export const listTasks = (_req: Request, res: Response) => {
  const response: IApiResponse<ITask[]> = {
    message: "Lista de tareas",
    data: tasks,
  };

  return res.status(200).json(response);
};

export const taskById = (req: Request, res: Response) => {
  try {
    const taskId = parseInt(req.params.taskId);

    const task = tasks.find((task) => task.id === taskId);

    if (!task) {
      const response: IApiResponse<ITask> = {
        message: "Tarea no encontrada",
      };
      return res.status(404).json(response);
    }

    const response: IApiResponse<ITask> = {
      message: "Tarea encontrada",
      data: task,
    };
    return res.status(200).json(response);
  } catch (error) {
    if (error instanceof Error) {
      const response: IApiResponse<ITask> = {
        message: error.message,
      };
      return res.status(500).json(response);
    }
  }
};

export const createTask = (req: Request, res: Response) => {
  try {
    const task = TaskSchema.parse(req.body);

    console.log(task);

    return res.status(200).json({ ok: true });
  } catch (error) {
    if (error instanceof ZodError) {
        const response: IApiResponse<ITask> = {
            message: 'Error al validar la tarea',
            error: error.errors
        }
        return res.status(400).json(response);
    }

    if (error instanceof Error) {
      const response: IApiResponse<ITask> = {
        message: "Error al crear la tarea",
        error: error.message,
      };
      return res.status(500).json(response);
    }
  }
};
