import { z } from "zod";

export const UserSchema = z.object({
  name: z.string({
    required_error: "El campo name es obligatorio",
    invalid_type_error: "El campo name debe ser un string",
  }),
  email: z
    .string({
      required_error: "El campo email es obligatorio",
      invalid_type_error: "El campo email debe ser un string",
    })
    .email({
      message: "El campo email debe ser un email válido",
    }),
  password: z.string({
    required_error: "El campo password es obligatorio",
    invalid_type_error: "El campo password debe ser un string",
  }),
});

export const LoginSchema = z.object({
  email: z
    .string({
      required_error: "El campo email es obligatorio",
      invalid_type_error: "El campo email debe ser un string",
    })
    .email({
      message: "El campo email debe ser un email válido",
    }),
  password: z.string({
    required_error: "El campo password es obligatorio",
    invalid_type_error: "El campo password debe ser un string",
  }),
});
