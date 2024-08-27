import express from "express";

const app = express();
const port = 3000;

// Para procesar datos JSON
app.use(express.json());

// Middleware global
app.use((req, res, next) => {
  const url = req.url;
  const method = req.method;
  console.log(`Method: ${method}, URL: ${url}`);
  next();
});

// Rutas en express
app.get("/", (req, res) => {
  res.send("Hello World!");
});

// Middleware para una ruta especifica
app.get(
  "/home",
  (req, res, next) => {
    const url = req.url;
    const method = req.method;
    console.log(`Method: ${method}, URL: ${url}`);
    next();
  },
  (req, res) => {
    res.send("Welcome to home");
  }
);

// Recuperar parametros por la ruta
app.get("/user/:userId", (req, res) => {
  const userId = parseInt(req.params.userId);
  res.send(`User id: ${userId}`);
});

const getAllUsers = (req, res) => {
  const method = req.method;
  console.log(`El metodo de la ruta /user/list es ${method}`);
  return res.send("Users fetched successfully")
};

app.get("/users/list", getAllUsers);

// CRUD de ejemplo

let tasks = [
  {
    id: 1,
    name: "Make tests",
  },
  {
    id: 2,
    name: "Create CRUD",
  },
];

// Listar los task
app.get("/task/list", (req, res) => {
  res.status(200).json(tasks);
});

// Crear un nuevo task
app.post("/task/create", (req, res) => {
  const body = req.body;
  tasks.push(body);
  res.status(201).json(tasks);
});

// Actualizar un task por el ID
app.put("/task/update/:taskId", (req, res) => {
  const taskId = parseInt(req.params.taskId);
  const body = req.body;

  const task = tasks.find((t) => t.id === taskId);

  if (!task) {
    return res.status(404).send("Task not found");
  }

  task.name = body.name;

  return res.status(200).json(task);
});

// Eliminar un task por el ID
app.delete("/task/delete/:taskId", (req, res) => {
  const taskId = parseInt(req.params.taskId);

  const task = tasks.find((t) => t.id === taskId);

  if (!task) {
    return res.status(404).send("Task not found");
  }

  tasks = tasks.filter((t) => t.id !== taskId);

  return res.status(200).json(tasks);
});

app.listen(port, () => {
  console.log(`Running app: http://localhost:${port}`);
});
