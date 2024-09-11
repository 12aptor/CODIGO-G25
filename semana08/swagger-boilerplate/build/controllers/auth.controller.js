"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.login = exports.register = void 0;
const zod_1 = require("zod");
const user_schema_1 = require("../schemas/user.schema");
const storage_1 = require("firebase/storage");
const firebase_1 = require("../config/firebase");
const prisma_1 = require("../config/prisma");
const bcrypt_1 = __importDefault(require("bcrypt"));
const jsonwebtoken_1 = __importDefault(require("jsonwebtoken"));
const register = (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const avatar = req.file;
        if (!avatar) {
            throw new zod_1.ZodError([
                {
                    code: "invalid_type",
                    expected: "object",
                    received: "undefined",
                    path: ["avatar"],
                    message: "Required",
                },
            ]);
        }
        const validatedData = user_schema_1.RegisterSchema.parse(req.body);
        const storage = (0, storage_1.getStorage)(firebase_1.firebaseApp);
        const storageRef = (0, storage_1.ref)(storage, `users/avatars/${avatar.originalname}`);
        const firebaseResponse = yield (0, storage_1.uploadBytes)(storageRef, avatar.buffer);
        if (!firebaseResponse.metadata) {
            throw new Error("Error al cargar la imagen al servidor");
        }
        const user = yield prisma_1.prisma.users.create({
            data: Object.assign(Object.assign({}, validatedData), { password: yield bcrypt_1.default.hash(validatedData.password, 10), avatar: avatar.originalname }),
            select: {
                id: true,
                username: true,
                email: true,
            },
        });
        return res.status(201).json({
            message: "Usuario creado exitosamente",
            data: user,
        });
    }
    catch (error) {
        if (error instanceof zod_1.ZodError) {
            return res.status(400).json({
                message: "Error en la validación de datos",
                error: error.errors,
            });
        }
        if (error instanceof Error) {
            return res.status(500).json({
                message: "Ha ocurrido un error",
                error: error.message,
            });
        }
    }
});
exports.register = register;
const login = (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const validatedData = user_schema_1.LoginSchema.parse(req.body);
        const user = yield prisma_1.prisma.users.findUnique({
            where: {
                email: validatedData.email,
            },
        });
        if (!user) {
            throw new Error("Credenciales incorrectas");
        }
        const isPasswordCorrect = yield bcrypt_1.default.compare(validatedData.password, user.password);
        if (!isPasswordCorrect) {
            throw new Error("Credenciales incorrectas");
        }
        const secret = process.env.SECRET_KEY;
        if (!secret) {
            throw new Error("Se necesita la secret key");
        }
        const access = jsonwebtoken_1.default.sign({
            id: user.id,
            username: user.username,
            email: user.email,
        }, secret, {
            expiresIn: "7d",
        });
        return res.status(200).json({
            message: "Sesión iniciada exitosamente",
            data: {
                access,
            },
        });
    }
    catch (error) {
        if (error instanceof zod_1.ZodError) {
            return res.status(400).json({
                message: "Error en la validación de datos",
                error: error.errors,
            });
        }
        if (error instanceof Error) {
            return res.status(500).json({
                message: "Ha ocurrido un error",
                error: error.message,
            });
        }
    }
});
exports.login = login;
