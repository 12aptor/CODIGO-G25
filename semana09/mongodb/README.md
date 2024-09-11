# MongoDB

## Instalación

- Instalar MongoDB
- Instalar MongoDB Compass
- Instalar Mongosh

### Abrir terminal de MongoDB

```bash
mongosh
```

### Mostrar las bases de datos

```bash
show dbs
```

### Conectar o crear una base de datos

```bash
use ecommerce
```

### Eliminar base de datos

```javascript
db.dropDatabase();
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

### Eliminar una colección

```javascript
db.users.drop();
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
db.customers.deleteOne({ _id: ObjectId("66df9e30bd95766ed8c73c02") });
```

### Eliminar una propiedad de un documento

```javascript
db.customers.updateOne(
  { _id: ObjectId("66df9e30bd95766ed8c73c02") },
  { $unset: { age: 1 } }
);
```

### Ordenar datos de una colección

```javascript
db.customers.find().sort({ age: 1 });
```

### Limite de documentos

```javascript
db.customers.find().limit(2);
```

### Pagination

```javascript
db.customers.find().skip(2).limit(2).sort({ age: -1 });
```

## Busquedas avanzadas

### Operadores de comparación

- $eq: Igual a

    ```javascript
    db.customers.find({
        age: {
            $eq: 30
        }
    })
    ```

- $ne: No igual a

    ```javascript
    db.customers.find({
        age: {
            $ne: 40
        }
    })
    ```

- $gt: Mayor que

    ```javascript
    db.customers.find({
        age: {
            $gt: 30
        }
    })
    ```

- $gts: Mayor o igual que

    ```javascript
    db.customers.find({
        age: {
            $gte: 35
        }
    })
    ```

- $lt: Menor que

    ```javascript
    db.customers.find({
        age: {
            $lt: 30
        }
    })
    ```

- $lte: Menor o igual que

    ```javascript
    db.customers.find({
        age: {
            $lte: 30
        }
    })
    ```

- $in: Coincide

    ```javascript
    db.customers.find({
        tags: {
            $in: ["cool"]
        }
    })
    ```

- $nin: No coincide

    ```javascript
    db.customers.find({
        tags: {
            $nin: ["cool"]
        }
    })
    ```

### Operadores lógicos

- $and: Combina las condiciones, todos deben cumplirse

    ```javascript
    db.customers.find({
        $and: [
            {
                age: {
                    $gt: 30
                }
            },
            {
                tags: {
                    $in: ["cool"]
                }
            }
        ]
    })
    ```

- $or: Combina las condiciones, al menos una debe cumplirse

    ```javascript
    db.customers.find({
        $or: [
            {
                age: {
                    $gt: 30
                }
            },
            {
                tags: {
                    $in: ["cool"]
                }
            }
        ]
    })
    ```

- $not: Inversa la condición

    ```javascript
    db.customers.find({
        age: {
            $not: {
                $gt: 30
            }
        }
    })
    ```

- $nor: Inversa la condición combinada con $or

    ```javascript
    db.customers.find({
        $nor: [
            {
                age: {
                    $gt: 30
                }
            },
            {
                tags: {
                    $in: ["cool"]
                }
            }
        ]
    })
    ```

### Los operadores de elementos

- $exists: Verifica si existe un campo

    ```javascript
    db.customers.find({
        tags: {
            $exists: true
        }
    })
    ```

- $type: Verifica el tipo de un campo

    ```javascript
    db.customers.find({
        age: {
            $type: "number"
        }
    })
    ```

### Cosultas en arrays

- $elemMatch: Coincide con un elemento de un array

    ```javascript
    db.customers.find({
        tags: {
            $elemMatch: {
                $eq: "cool"
            }
        }
    })
    ```

- $size: Verifica el tamaño de un array

    ```javascript
    db.customers.find({
        'location.coordinates': {
            $size: 1
        }
    })
    ```