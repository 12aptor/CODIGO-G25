import { Request, Response } from "express";
import { prisma } from "../config/prisma";
import { PostSchema } from "../schemas/post.schema";
import { ZodError } from "zod";

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
    if (error instanceof ZodError) {
      return res.status(400).json({
        message: "Error al validar los datos",
        error: error.issues,
      });
    }

    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error al crear el post",
        error: error.message,
      });
    }
  }
};

export const getPosts = async (_req: Request, res: Response) => {
  try {
    const posts = await prisma.posts.findMany({
      include: {
        author: true,
        comments: {
          include: {
            author: true
          }
        },
      },
    });

    return res.status(200).json({
      message: "Posts obtenidos correctamente",
      data: posts,
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error al obtener los posts",
        error: error.message,
      });
    }
  }
};
