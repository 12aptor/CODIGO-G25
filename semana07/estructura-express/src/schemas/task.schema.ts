import { z } from "zod";

export const TaskSchema = z.object({
  id: z.number({
    required_error: "El campo id es obligatorio",
    invalid_type_error: "El campo id debe ser un número",
  }),
  name: z.string({
    required_error: "El campo name es obligatorio",
    invalid_type_error: "El campo name debe ser una cadena de caracteres",
  }),
});
