# MongoDB

## Instalación

- Instalar MongoDB
- Instalar MongoDB Compass
- Instalar Mongosh

## Mongo shell

### Abrir terminal de MongoDB

```bash
mongosh
```

### Mostrar las bases de datos

```bash
show dbs
```

### Conectar a la base de datos

```bash
use ecommerce
```

### Crear una colección

```javascript
db.createCollection("customers");
// ó
db.customers.insertOne({ name: "John Doe", age: 30 });
```

### Mostrar las colecciones

```bash
show collections
```

### Insertar datos en una colección

```javascript
db.customers.insertOne({ name: "John Doe", age: 30 });

db.customers.insertMany([
  { name: "Jane Doe", age: 25 },
  { name: "Bob Smith", age: 35 },
  { name: "Alice Johnson", age: 40 },
]);

db.customers.insertOne({
  name: "Charlie Brown",
  age: 40,
  tags: ["cool", "funny"],
  location: {
    city: "New York",
    state: "NY",
    country: "USA",
    coordinates: [40.7127, 74.0059],
  },
});
```

### Buscar datos en una colección

```javascript
db.customers.find();
db.customers.find({ name: "John Doe" });
db.customers.find({ age: 30 });
```

### Actualizar datos de una colección

```javascript
db.customers.updateOne({ name: "John Doe" }, { $set: { age: 26 } });
```

### Eliminar datos de una colección

```javascript
db.customers.deleteOne({ name: "John Doe" });
db.customers.deleteOne({ _id: ObjectId('66df9e30bd95766ed8c73c02') })
```

### Eliminar una propiedad de un documento

```javascript
db.customers.updateOne(
    { _id: ObjectId('66df9e30bd95766ed8c73c02') },
    { $unset: { age: 1 }}
)
```