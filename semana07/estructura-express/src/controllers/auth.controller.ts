import { Request, Response } from "express";
import jwt from "jsonwebtoken";

export const login = (_req: Request, res: Response) => {
  try {
    const user = {
      id: 1,
      name: "Juan",
      email: "juan@gmail.com"
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
