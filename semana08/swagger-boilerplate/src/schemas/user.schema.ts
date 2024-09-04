import { z } from "zod";

export const RegisterSchema = z.object({
  username: z.string(),
  email: z.string().email(),
  password: z.string(),
});

export const LoginSchema = z.object({
  email: z.string().email(),
  password: z.string(),
});
