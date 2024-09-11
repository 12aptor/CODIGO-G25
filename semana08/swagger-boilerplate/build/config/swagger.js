"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.swaggerSpec = void 0;
const swagger_jsdoc_1 = __importDefault(require("swagger-jsdoc"));
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
                        readOnly: true,
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
                        readOnly: true,
                    },
                    updated_at: {
                        type: "string",
                        format: "date-time",
                        description: "Fecha y hora de creación",
                        example: "2024-01-01T00:00:00Z",
                        readOnly: true,
                    },
                },
            },
            CreateChannelResponse: {
                type: "object",
                properties: {
                    message: {
                        type: "string",
                        description: "Mensaje del servidor",
                        example: "Canal creado exitosamente",
                    },
                    data: {
                        type: "object",
                        $ref: "#/components/schemas/Channel",
                    },
                },
            },
            ListChannelResponse: {
                type: "object",
                properties: {
                    message: {
                        type: "string",
                        description: "Mensaje del servidor",
                        example: "Canales obtenidos exitosamente",
                    },
                    data: {
                        type: "array",
                        items: {
                            $ref: "#/components/schemas/Channel",
                        },
                    },
                },
            },
            Message: {
                type: "object",
                required: ["name", "type"],
                properties: {
                    id: {
                        type: "integer",
                        format: "int64",
                        description: "ID único del canal",
                        example: 1,
                        readOnly: true,
                    },
                    content: {
                        type: "string",
                        description: "Contenido del mensaje",
                        example: "Hola",
                    },
                    author_id: {
                        type: "integer",
                        format: "int64",
                        description: "Id único del autor",
                        example: 1,
                    },
                    author: {
                        type: "object",
                        properties: {
                            username: {
                                type: "string",
                                description: "Username del autor",
                                example: "pepito",
                            },
                        },
                    },
                    created_at: {
                        type: "string",
                        format: "date-time",
                        description: "Fecha y hora de creación",
                        example: "2024-01-01T00:00:00Z",
                        readOnly: true,
                    },
                    updated_at: {
                        type: "string",
                        format: "date-time",
                        description: "Fecha y hora de creación",
                        example: "2024-01-01T00:00:00Z",
                        readOnly: true,
                    },
                },
            },
            ListMessagesResponse: {
                type: "object",
                properties: {
                    message: {
                        type: "string",
                        description: "Mensaje del servidor",
                        example: "Mensajes obtenidos exitosamente",
                    },
                    data: {
                        type: "array",
                        items: {
                            $ref: "#/components/schemas/Message",
                        },
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
exports.swaggerSpec = (0, swagger_jsdoc_1.default)(options);
