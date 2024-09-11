"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ChannelSchema = void 0;
const zod_1 = require("zod");
exports.ChannelSchema = zod_1.z.object({
    name: zod_1.z.string(),
    type: zod_1.z.enum(["TEXT", "VOICE"]),
});
