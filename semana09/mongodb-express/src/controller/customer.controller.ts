import { Request, Response } from "express";
import { db } from "../config/mongodb";
import { ObjectId } from "mongodb";

export const getAllCustomers = async (_req: Request, res: Response) => {
  try {
    const customers = db.collection("customers");

    const result = await customers.find({}).toArray();

    return res.status(200).json({
      message: "Customers fetched successfully",
      data: result,
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error fetching customers",
        error: error.message,
      });
    }
  }
};

export const createCustomer = async (req: Request, res: Response) => {
  try {
    const customers = db.collection("customers");

    const doc = {
      name: req.body.name,
      age: req.body.age,
    };

    const result = await customers.insertOne(doc);

    if (!result.acknowledged) {
      throw new Error("Failed to create customer");
    }

    return res.status(201).json({
      message: "Customer created successfully",
      data: {
        _id: result.insertedId,
        ...doc,
      },
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error fetching customers",
        error: error.message,
      });
    }
  }
};

export const updateCustomer = async (req: Request, res: Response) => {
  try {
    const customers = db.collection("customers");
    const customerId = req.params.customerId;

    const updatedData = {
      $set: {
        name: req.body.name,
        age: req.body.age,
      },
    };

    const result = await customers.updateOne(
      { _id: new ObjectId(customerId) },
      updatedData
    );

    if (result.matchedCount === 0) {
      throw new Error("Customer not found");
    }

    if (!result.acknowledged) {
      throw new Error("Failed to update customer");
    }

    return res.status(200).json({
      message: "Customer updated successfully",
      data: {
        _id: customerId,
        name: req.body.name,
        age: req.body.age,
      },
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error fetching customers",
        error: error.message,
      });
    }
  }
};

export const getByName = async (req: Request, res: Response) => {
  try {
    const customerName = req.params.customerName;
    const customers = db.collection("customers");

    const query = {
      name: customerName,
    };

    const result = await customers.find(query).toArray();

    return res.status(200).json({
      message: "Customers fetched successfully",
      data: result,
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error fetching customers",
        error: error.message,
      });
    }
  }
};

export const deleteCustomer = async (req: Request, res: Response) => {
  try {
    const customerId = req.params.customerId;
    const customers = db.collection("customers");

    const result = await customers.deleteOne({
      _id: new ObjectId(customerId),
    });

    if (!result.acknowledged) {
      throw new Error("Failed delete customer");
    }

    return res.status(200).json({
      message: "Customer deleted successfully",
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        message: "Error fetching customers",
        error: error.message,
      });
    }
  }
};
