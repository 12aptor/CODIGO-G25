import { Request, Response } from "express";
import { ZodError } from "zod";
import { LoginSchema, RegisterSchema } from "../schemas/user.schema";
import { getStorage, ref, uploadBytes } from "firebase/storage";
import { firebaseApp } from "../config/firebase";
import { prisma } from "../config/prisma";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";

export const register = async (req: Request, res: Response) => {
  try {
    const avatar = req.file;

    if (!avatar) {
      throw new ZodError([
        {
          code: "invalid_type",
          expected: "object",
          received: "undefined",
          path: ["avatar"],
          message: "Required",
        },
      ]);
    }

    const validatedData = RegisterSchema.parse(req.body);

    const storage = getStorage(firebaseApp);
    const storageRef = ref(storage, `users/avatars/${avatar.originalname}`);
    const firebaseResponse = await uploadBytes(storageRef, avatar.buffer);

    if (!firebaseResponse.metadata) {
      throw new Error("Error al cargar la imagen al servidor");
    }

    const user = await prisma.users.create({
      data: {
        ...validatedData,
        password: await bcrypt.hash(validatedData.password, 10),
        avatar: avatar.originalname,
      },
      select: {
        id: true,
        username: true,
        email: true,
      },
    });

    return res.status(201).json({
      message: "Usuario creado exitosamente",
      data: user,
    });
  } catch (error) {
    if (error instanceof ZodError) {
      return res.status(400).json({
        message: "Error en la validación de datos",
        error: error.errors,
      });
    }

    if (error instanceof Error) {
      return res.status(500).json({
        message: "Ha ocurrido un error",
        error: error.message,
      });
    }
  }
};

export const login = async (req: Request, res: Response) => {
  try {
    const validatedData = LoginSchema.parse(req.body);

    const user = await prisma.users.findUnique({
      where: {
        email: validatedData.email,
      },
    });

    if (!user) {
      throw new Error("Credenciales incorrectas");
    }

    const isPasswordCorrect = await bcrypt.compare(
      validatedData.password,
      user.password
    );

    if (!isPasswordCorrect) {
      throw new Error("Credenciales incorrectas");
    }

    const secret = process.env.SECRET_KEY;

    if (!secret) {
      throw new Error("Se necesita la secret key");
    }

    const access = jwt.sign(
      {
        id: user.id,
        username: user.username,
        email: user.email,
      },
      secret,
      {
        expiresIn: "7d",
      }
    );

    return res.status(200).json({
      message: "Sesión iniciada exitosamente",
      data: {
        access,
      },
    });
  } catch (error) {
    if (error instanceof ZodError) {
      return res.status(400).json({
        message: "Error en la validación de datos",
        error: error.errors,
      });
    }

    if (error instanceof Error) {
      return res.status(500).json({
        message: "Ha ocurrido un error",
        error: error.message,
      });
    }
  }
};
