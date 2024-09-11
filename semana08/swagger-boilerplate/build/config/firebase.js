"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.firebaseApp = void 0;
const dotenv_1 = __importDefault(require("dotenv"));
const app_1 = require("firebase/app");
dotenv_1.default.config();
const firebaseConfig = {
    apiKey: process.env.FIREBASE_APIKEY,
    authDomain: "express-chat-a0353.firebaseapp.com",
    projectId: "express-chat-a0353",
    storageBucket: "express-chat-a0353.appspot.com",
    messagingSenderId: "571322368688",
    appId: "1:571322368688:web:ee5e22378192e265bef175",
};
exports.firebaseApp = (0, app_1.initializeApp)(firebaseConfig);
