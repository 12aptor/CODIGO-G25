import { Request, Response } from "express";
import { ZodError } from "zod";
import { UserSchema } from "../schemas/user.schema";
import { prisma } from "../config/prisma";

export const createUser = async (req: Request, res: Response) => {
  try {
    const validatedData = UserSchema.parse(req.body);

    const user = await prisma.users.create({
      data: validatedData,
    });

    return res.status(201).json({
      message: "Usuario creado correctamente",
      data: user,
    });
  } catch (error) {
    if (error instanceof ZodError) {
      return res.status(400).json({
        message: "Error al validar el usuario",
        error: error.issues,
      });
    }

    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error al crear el usuario",
        error: error.message,
      });
    }
  }
};
