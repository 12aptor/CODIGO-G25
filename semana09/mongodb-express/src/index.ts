import express from "express";
import { customerRouter } from "./routes/customer.router";

const app = express();
const port = 3000;

app.use(express.json())

app.use("/api/v1/customers", customerRouter);

app.listen(port, () => {
  console.log(`Running app: http://localhost:${port}`);
});
