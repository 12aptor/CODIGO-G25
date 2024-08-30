import { ZodIssue } from "zod";

export interface IApiResponse {
  message: string;
  data?: any;
  error?: string | ZodIssue[];
}
