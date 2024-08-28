import express, { Request, Response } from "express";
import morgan from "morgan";
import fs from "fs";

const app = express();

const accessLogStream = fs.createWriteStream("logs.txt", { flags: "a" });

app.use(morgan("combined", { stream: accessLogStream }));
app.use(morgan("dev"));

const home = (req: Request, res: Response) => {
  res.send("Hello World");
};

app.get("/", home);

app.get("/hacker", (req, res) => {
  res.sendFile(__dirname + "/public/hacker.html");
});

app.listen(4545, () => {
  console.log(`Running app: http://localhost:4545`);
});
