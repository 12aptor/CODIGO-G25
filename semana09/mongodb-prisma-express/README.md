# Modelar con MongoDB

## Tips

### Elegir entre Embedding y Referencing

- Referencing: Uno de los modelos referencia a otro modelo.
- Embedding: Uno de los modelos se incorpora a otro modelo.

### Modelar para consultas frecuentes

Preveer consultas frecuentes para optimizar la consulta.

### Evitar documentos muy grandes

MongoDB tiene un límite de tamaño de documento de 16MB. Si el tamaño de un documento es mayor, se puede dividir el documento en partes más pequeñas.

## Usar el campo \_id sabiamente

MongoDB crea un campo \_id automáticamente si no lo defines. Este campo es la clave primaria y puede ser un ObjectId. Es importante aprovechar este campo para garantizar la unicidad en los documentos.

### Usar índices

Los índices son una forma de optimizar la consulta.

### Ponderar la consistencia y el rendimiento

En MongoDB se puede priorizar la consistencia (asegurarnos que siempre tengas datos actualizados) o el rendimiento (asegurarnos de que tengas los datos más rápido).
