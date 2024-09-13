import express from "express";
import { prisma } from "./config/prisma";

const app = express();
const port = 3000;

app.get("/", async (_req, res) => {
  const posts = await prisma.posts.findMany();

  return res.status(200).json(posts);
});

app.listen(port, () => {
  console.log(`Running app: http://localhost:${port}`);
});
