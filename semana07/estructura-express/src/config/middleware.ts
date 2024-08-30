import { Request, Response, NextFunction } from "express";
import jwt from "jsonwebtoken";

declare module "jsonwebtoken" {
  export interface JwtPayload {
    id: number;
    name: string;
    email: string;
  }
}

export const authMiddleware = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const bearerToken = req.headers.authorization;

  if (!bearerToken) {
    return res.status(401).json({
      message: "No tienes autorización",
    });
  }

  const token = bearerToken.split(" ")[1];

  try {
    // const decoded = jwt.verify(token, "secret") as JwtPayload;
    jwt.verify(token, "secret");
    
    // if (decoded.id !== 1) {
    //   return res.status(401).json({
    //     message: "No tienes autorización",
    //   });
    // }

    return next();
  } catch (error) {
    return res.status(401).json({
      message: "No tienes autorización",
    });
  }
};
