import { Request, Response } from "express";
import { prisma } from "../config/prisma";
import { getDownloadURL, ref, getStorage } from "firebase/storage";
import { firebaseApp } from "../config/firebase";

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
            avatar: true,
            username: true,
          },
        },
      },
    });

    let newMessages = [];
    const storage = getStorage(firebaseApp);

    for (let i = 0; i < messages.length; i++) {
      const message = messages[i];
      const storageRef = ref(storage, `users/avatars/${message.author.avatar}`);
      const avatarUrl = await getDownloadURL(storageRef);

      newMessages.push({
        ...message,
        author: {
          ...message.author,
          avatar: avatarUrl,
        },
      });
    }

    return res.status(200).json({
      message: "Mensajes obtenidos exitosamente",
      data: newMessages,
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
