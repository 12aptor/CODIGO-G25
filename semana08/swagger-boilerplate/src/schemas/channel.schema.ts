import { z } from "zod";

export const ChannelSchema = z.object({
  name: z.string(),
  type: z.enum(["TEXT", "VOICE"]),
});
