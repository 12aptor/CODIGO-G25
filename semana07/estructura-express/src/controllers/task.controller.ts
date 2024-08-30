import { Request, Response } from "express";
import { IApiResponse } from "../types";
import { TaskSchema } from "../schemas/task.schema";
import { ZodError } from "zod";
import { prisma } from "../config/prisma";

export const listTasks = async (_req: Request, res: Response) => {
  try {
    let tasks = await prisma.tasks.findMany();

    const response: IApiResponse = {
      message: "Lista de tareas",
      data: tasks,
    };
    return res.status(200).json(response);
  } catch (error) {
    if (error instanceof Error) {
      const response: IApiResponse = {
        message: "Error al obtener la lista de tareas",
        error: error.message,
      };
      return res.status(500).json(response);
    }
  }
};

export const taskById = async (req: Request, res: Response) => {
  try {
    const taskId = parseInt(req.params.taskId);

    let task = await prisma.tasks.findUnique({
      where: {
        id: taskId,
      },
    });

    const response: IApiResponse = {
      message: "Tarea encontrada",
      data: task,
    };
    return res.status(200).json(response);
  } catch (error) {
    if (error instanceof Error) {
      const response: IApiResponse = {
        message: error.message,
      };
      return res.status(500).json(response);
    }
  }
};

export const createTask = async (req: Request, res: Response) => {
  try {
    const validatedTask = TaskSchema.parse(req.body);

    let task = await prisma.tasks.create({
      data: validatedTask,
    });

    const response: IApiResponse = {
      message: "Tarea creada",
      data: task,
    };
    return res.status(200).json(response);
  } catch (error) {
    if (error instanceof ZodError) {
      const response: IApiResponse = {
        message: "Error al validar la tarea",
        error: error.errors,
      };
      return res.status(400).json(response);
    }

    if (error instanceof Error) {
      const response: IApiResponse = {
        message: "Error al crear la tarea",
        error: error.message,
      };
      return res.status(500).json(response);
    }
  }
};
