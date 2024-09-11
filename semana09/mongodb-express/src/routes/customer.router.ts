import { Router } from "express";
import * as customerController from "../controller/customer.controller";

export const customerRouter = Router();

customerRouter.get("/all", customerController.getAllCustomers);
customerRouter.post("/create", customerController.createCustomer);
customerRouter.put("/update/:customerId", customerController.updateCustomer);
customerRouter.get("/get/by-name/:customerName", customerController.getByName);
customerRouter.delete("/delete/:customerId", customerController.deleteCustomer);
