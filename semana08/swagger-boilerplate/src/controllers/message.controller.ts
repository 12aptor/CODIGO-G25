import { Request, Response } from "express";
import { prisma } from "../config/prisma";

export const listMessages = async (req: Request, res: Response) => {
  try {
    const channelId = req.params.channelId;
    const messages = await prisma.messages.findMany({
      where: {
        channel_id: channelId,
      },
      include: {
        author: {
          select: {
            username: true,
          },
        },
      },
    });

    return res.status(200).json({
      message: "Mensajes obtenidos exitosamente",
      data: messages,
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
