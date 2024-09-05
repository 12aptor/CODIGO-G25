import { Request, Response } from "express";
import { ZodError } from "zod";
import { ChannelSchema } from "../schemas/channel.schema";
import { prisma } from "../config/prisma";

export const createChannel = async (req: Request, res: Response) => {
  try {
    const validatedData = ChannelSchema.parse(req.body);

    const channel = await prisma.channels.create({
      data: validatedData,
    });

    return res.status(201).json({
      message: "Canal creado exitosamente",
      data: channel,
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

export const listChannels = async (_req: Request, res: Response) => {
  try {
    const channels = await prisma.channels.findMany();

    return res.status(200).json({
      message: "Canales obtenidos exitosamente",
      data: channels,
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        message: "Ha ocurrido un error",
        error: error.message,
      });
    }
  }
};
