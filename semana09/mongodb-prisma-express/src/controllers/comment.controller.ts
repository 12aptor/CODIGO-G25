import { Request, Response } from "express";
import { CommentSchema } from "../schemas/comment.schema";
import { ZodError } from "zod";
import { prisma } from "../config/prisma";

export const createComment = async (req: Request, res: Response) => {
  try {
    const validatedData = CommentSchema.parse(req.body);

    const comment = await prisma.comments.create({
      data: validatedData,
    });

    return res.status(201).json({
      message: "Comentario creado correctamente",
      data: comment,
    });
  } catch (error) {
    if (error instanceof ZodError) {
      return res.status(400).json({
        message: "Error al validar el comentario",
        error: error.issues,
      });
    }

    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error al crear el comentario",
        error: error.message,
      });
    }
  }
};

export const deleteComment = async (req: Request, res: Response) => {
  try {
    const commentId = req.params.commentId;

    await prisma.comments.delete({
      where: {
        id: commentId,
      },
    });

    return res.status(200).json({
      message: "Comentario eliminado correctamente",
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error al crear el comentario",
        error: error.message,
      });
    }
  }
};
