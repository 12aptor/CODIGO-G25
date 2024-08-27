# Express

## Inicializar un proyecto de express

```bash
npm init
npm init -y # Aceptar todas las preguntas
```

## Instalar express

```bash
npm install express
```

## Instalar nodemon (Para el hot reload)

```bash
npm install --save-dev nodemon
```

Agregamos el comando `npm run dev` a nuestro package.json
```json
...
"scripts": {
    ...
    "dev": "nodemon index.js"
},
...
```