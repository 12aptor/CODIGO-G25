import { Request, Response } from "express";
import jwt from "jsonwebtoken";
import { prisma } from "../config/prisma";
import { UserSchema } from "../schemas/user.schema";
import { ZodError } from "zod";
import bcrypt from "bcrypt";

export const register = async (req: Request, res: Response) => {
  try {
    const validatedUser = UserSchema.parse(req.body);

    const user = await prisma.users.create({
      data: {
        ...validatedUser,
        password: await bcrypt.hash(validatedUser.password, 10),
      },
    });

    return res.status(200).json({
      message: "Usuario creado",
      data: user,
    });
  } catch (error) {
    if (error instanceof ZodError) {
      return res.status(400).json({
        message: "Error al validar el usuario",
        error: error.errors,
      });
    }

    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error al registrar usuario",
      });
    }
  }
};

export const login = (_req: Request, res: Response) => {
  try {
    const user = {
      id: 1,
      name: "Juan",
      email: "juan@gmail.com",
    };

    const token = jwt.sign(user, "secret");

    return res.status(200).json({
      message: "Sesión iniciada",
      data: {
        access: token,
      },
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error al iniciar sesión",
      });
    }
  }
};
