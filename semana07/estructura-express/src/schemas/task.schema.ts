import { z } from "zod";

export const TaskSchema = z.object({
  name: z.string({
    required_error: "El campo name es obligatorio",
    invalid_type_error: "El campo name debe ser una cadena de caracteres",
  }),
  description: z
    .string({
      invalid_type_error:
        "El campo description debe ser una cadena de caracteres",
    })
    .optional(),
  user_id: z.number({
    required_error: "El campo user_id es obligatorio",
    invalid_type_error: "El campo user_id debe ser un número",
  }),
});
