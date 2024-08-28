import express, { Request, Response } from "express";

const app = express();

const home = (req: Request, res: Response) => {
    res.send("Hello World");
};

app.get("/", home);

app.listen(4545, () => {
  console.log(`Running app: http://localhost:4545`);
});
