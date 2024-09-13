import { z } from "zod";

export const PostSchema = z.object({
  title: z.string(),
  content: z.string(),
  author_id: z.string(),
});
