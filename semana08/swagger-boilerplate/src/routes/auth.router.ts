import { Router } from "express";

export const authRouter = Router();

/**
 * @swagger
 * /api/v1/auth/login:
 *   post:
 *     summary: Log in a user
 *     description: Log in a user
 *     tags: [Auth]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required:
 *               - email
 *               - password
 *             properties:
 *               email:
 *                 type: string
 *                 description: User email
 *                 example: john@email.com
 *               password:
 *                 type: string
 *                 description: User password
 *                 example: password123
*/
authRouter.post("/login", (_req, res) => {
  res.send("Login Successful");
});
