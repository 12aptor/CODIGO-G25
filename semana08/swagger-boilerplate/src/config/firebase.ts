import dotenv from "dotenv";
import { initializeApp } from "firebase/app";

dotenv.config();

const firebaseConfig = {
  apiKey: process.env.FIREBASE_APIKEY,
  authDomain: "express-chat-a0353.firebaseapp.com",
  projectId: "express-chat-a0353",
  storageBucket: "express-chat-a0353.appspot.com",
  messagingSenderId: "571322368688",
  appId: "1:571322368688:web:ee5e22378192e265bef175",
};

export const firebaseApp = initializeApp(firebaseConfig);
