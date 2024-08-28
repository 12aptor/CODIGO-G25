# Crear API con Express y Typescript

## Inicializar proyecto

```bash
npm init -y
```

## Instalar dependencias

```bash
npm install --save express
npm install --save-dev @types/express
npm install --save-dev typescript
npm install --save-dev ts-node-dev # Para ejecutar el servidor en modo desarrollo (incluye hot reload)
```

## Crear archivo `index.ts`

```typescript
console.log("Hello World");
```

## Crear archivo `package.json`

```json
{
  "name": "express-typescript",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "tsc", 
    "dev": "ts-node-dev index.ts"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.19.2"
  },
  "devDependencies": {
    "ts-node-dev": "^2.0.0",
    "typescript": "^5.5.4"
  }
}
```

## Inicializar typescript => `tsconfig.json`

```bash
npx tsc --init
```

```json
{
  "compilerOptions": {
    "target": "ES6",
    "module": "commonjs",
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "resolveJsonModule": true,
    "strict": true,
    "outDir": "./build"
  },
  "include": ["**/*.ts"],
  "exclude": ["node_modules", "build"]
}
```