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
  components: {
    schemas: {
      Channel: {
        type: "object",
        required: ["name", "type"],
        properties: {
          id: {
            type: "string",
            description: "ID único del canal (uuid)",
            example: "e2a4-t68t-9y7i",
            readOnly: true
          },
          name: {
            type: "string",
            description: "Nombre del canal",
            example: "backend",
          },
          type: {
            type: "string",
            description: "Tipo de canal",
            enum: ["TEXT", "VOICE"],
            example: "TEXT",
          },
          created_at: {
            type: "string",
            format: "date-time",
            description: "Fecha y hora de creación",
            example: "2024-01-01T00:00:00Z",
            readOnly: true
          },
          updated_at: {
            type: "string",
            format: "date-time",
            description: "Fecha y hora de creación",
            example: "2024-01-01T00:00:00Z",
            readOnly: true
          },
        },
      },
    },
  },
};

const options = {
  swaggerDefinition,
  apis: ["./src/routes/*.ts"],
};

export const swaggerSpec = swaggerJSDoc(options);
