import swaggerJSDoc from "swagger-jsdoc";

const swaggerDefinition = {
  openapi: "3.0.0",
  info: {
    title: "Swagger Boilerplate",
    version: "1.0.0",
    description: "This is a boilerplate for real time chat application",
  },
  servers: [
    {
      url: "http://localhost:8000",
      description: "Localhost",
    },
  ],
};

const options = {
  swaggerDefinition,
  apis: ["./src/routes/*.ts"],
};

export const swaggerSpec = swaggerJSDoc(options);
