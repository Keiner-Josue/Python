# 🐍 Aprendiendo Python

## 🧠 ¿De qué trata este proyecto?

Este repositorio contiene ejercicios, pruebas y códigos prácticos que me ayudan a entender mejor la lógica y herramientas de Python.  
Es una libreta de aprendizaje personal en la que voy mejorando paso a paso, para fortalecer mi base como programador y aplicar esos conocimientos en otros lenguajes como Java o C++.

---

## ⚙️ ¿Cómo se ejecuta?

Para ejecutar los archivos de este proyecto necesitas:

- Tener Python instalado (preferiblemente la última versión)
- Tener Visual Studio Code o cualquier editor de código
- Instalar la extensión de Python si usas VS Code

Una vez hecho esto, puedes ejecutar cualquier archivo `.py` desde el terminal o directamente con el botón "Run".

---

## 🛠️ Tecnologías y herramientas utilizadas

- Python
- Visual Studio Code
- Extensión oficial de Python
- Terminal de Windows

---

## 🎯 Logros alcanzados

- Comprender los fundamentos de Python
- Mejorar mi lógica de programación
- Aprender a usar condicionales, ciclos, funciones y variables

---

## 🚀 Metas en progreso

- Aprender más estructuras y funciones avanzadas
- Aplicar Python en proyectos reales
- Llegar a dominar el lenguaje
- Usarlo como base para aprender ciberseguridad, automatización y más

---

## ✍️ Autor

**Keiner Josue / Keiner Barbosa**

Desde Colombia, aprendiendo, practicando y mejorando cada día.  
_"Cada línea que escribo es una versión mejor de mí mismo."_

---
classDiagram
    %% CLASES PRINCIPALES
    class Cliente {
        📝 Datos del cliente
        ---
        id
        nombre
        telefono
        direccion
    }

    class ItemCatalogo {
        🛍️ Productos
        ---
        id
        nombre
        precio
        stock
    }

    class Orden {
        📦 Pedido
        ---
        id
        fecha
        estado
        ---
        getTotal()
    }

    class DetalleOrden {
        📋 Línea de pedido
        ---
        cantidad
        ---
        getSubtotal()
    }

    class EstadoOrden {
        <<estado>>
        ---
        PENDIENTE
        EN_PROCESO
        ENVIADA
        ENTREGADA
        CANCELADA
    }

    class DistrisoftService {
        🎯 GESTOR PRINCIPAL
        ---
        Gestiona clientes
        Gestiona productos
        Gestiona órdenes
        Guarda todo en archivos
    }

    %% RELACIONES
    Cliente "1" -- "*" Orden : realiza
    Orden "*" -- "1" EstadoOrden : tiene un
    Orden "1" *-- "*" DetalleOrden : contiene
    DetalleOrden "*" -- "1" ItemCatalogo : producto
    
    DistrisoftService ..> Cliente : administra
    DistrisoftService ..> ItemCatalogo : administra
    DistrisoftService ..> Orden : administra

