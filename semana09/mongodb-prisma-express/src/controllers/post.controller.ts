import { Request, Response } from "express";
import { prisma } from "../config/prisma";
import { PostSchema } from "../schemas/post.schema";

export const createPost = async (req: Request, res: Response) => {
  try {
    const validatedData = PostSchema.parse(req.body);

    const post = await prisma.posts.create({
      data: validatedData,
    });

    return res.status(201).json({
      message: "Post creado correctamente",
      data: post,
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error al crear el post",
        error: error.message,
      });
    }
  }
};
