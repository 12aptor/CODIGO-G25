import { Request, Response } from "express";
import jwt from "jsonwebtoken";
import { prisma } from "../config/prisma";
import { LoginSchema, UserSchema } from "../schemas/user.schema";
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
      select: {
        id: true,
        name: true,
        email: true,
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

export const login = async (req: Request, res: Response) => {
  try {
    const validatedCredentials = LoginSchema.parse(req.body);

    const user = await prisma.users.findUnique({
      where: {
        email: validatedCredentials.email,
      },
    });

    if (!user) {
      return res.status(401).json({
        message: "No tienes autorización",
      });
    }

    const isPasswordCorrect = await bcrypt.compare(
      validatedCredentials.password,
      user.password
    );

    if (!isPasswordCorrect) {
      return res.status(401).json({
        message: "No tienes autorización",
      });
    }

    const token = jwt.sign(
      {
        id: user.id,
        name: user.name,
        email: user.email,
      },
      "secret"
    );

    return res.status(200).json({
      message: "Sesión iniciada",
      data: {
        access: token,
      },
    });
  } catch (error) {
    if (error instanceof ZodError) {
      return res.status(400).json({
        message: "Error al validar las credenciales",
        error: error.errors,
      });
    }

    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error al iniciar sesión",
      });
    }
  }
};
