// Type Alias
type Person = {
    readonly id: number;
    name: string;
    age?: number;
}

type ClientBase = {
    ruc: string;
    email: string;
    status: boolean;
}

type Client = Person & ClientBase;


// Objetos
let person: Person = {
    id: 1,
    name: "Eduardo",
};

let client: Client = {
    id: 1,
    name: "Eduardo",
    ruc: "123456789",
    email: "eduardo@gmail.com",
    status: true
}

// Mutar un objeto
person.name = "Miguel";
person.age = 30;

// Funciones
const createPerson = (id: number, name: string): Person => {
    return {
        id,
        name
    }
}

let pepito = createPerson(1, 'Pepito')

