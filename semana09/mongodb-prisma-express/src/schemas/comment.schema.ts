import { z } from "zod";

export const CommentSchema = z.object({
  content: z.string(),
  post_id: z.string(),
  author_id: z.string(),
});
