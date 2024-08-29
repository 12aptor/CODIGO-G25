import { ZodIssue } from "zod";

export interface ITask {
  id: number;
  name: string;
}

export interface IApiResponse<T> {
  message: string;
  data?: T;
  error?: string | ZodIssue[];
}
