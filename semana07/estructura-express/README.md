# Prisma ORM

## Instalación

```bash
npm install --save-dev prisma
```

## Configuración

```bash
npx prisma init
# Si queremos usar otra base de datos
# npx prisma init --datasource-provider postgresql
# npx prisma init --datasource-provider mysql
# npx prisma init --datasource-provider mongodb
# npx prisma init --datasource-provider sqlite
```

## Crear modelo de datos

```bash
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model users {
  id       Int     @id @default(autoincrement())
  name     String
  email    String  @unique
  password String  @db.Text
  tasks    tasks[]
}

model tasks {
  id          Int      @id @default(autoincrement())
  name        String
  description String?  @db.Text
  status      Boolean  @default(false)
  created_at  DateTime @default(now())
  updated_at  DateTime @updatedAt
  user_id     Int
  user        users    @relation(fields: [user_id], references: [id])
}
```

## Crear migraciones

```bash
npx prisma migrate dev
# npx prisma migrate dev --name "migration_name"
```