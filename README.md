# Proyecto de Chatbot para ProcessOptima - HackaIA

## Descripción

Este proyecto consiste en un chatbot diseñado para mejorar la eficiencia y comunicación interna de la empresa ProcessOptima. El chatbot proporciona información sobre procesos internos relacionados con ganadería y agricultura sostenible. Está compuesto por dos partes principales: un frontend en React y un backend en Flask. El frontend se encarga de la interfaz de usuario y la comunicación con el backend, mientras que el backend maneja las peticiones del frontend y se comunica con la API de Google Generative AI para obtener respuestas.

## Qué Hace el Proyecto

El chatbot tiene como objetivo principal facilitar el acceso a la información sobre procesos internos de la empresa en las áreas de ganadería y agricultura sostenible. Las principales funcionalidades incluyen:

- **Consulta de Información**: Permite a los usuarios hacer preguntas sobre diversos aspectos relacionados con los procesos internos de la empresa.
- **Generación de Respuestas**: Utiliza la API de Google Generative AI para generar respuestas precisas y relevantes a las preguntas de los usuarios.
- **Interfaz Intuitiva**: Ofrece una interfaz amigable y fácil de usar a través de la aplicación React, que facilita la interacción con el chatbot.
- **Mejora de la Comunicación Interna**: Facilita el acceso a la información relevante, mejorando la eficiencia en la comunicación interna y reduciendo el tiempo necesario para obtener respuestas a preguntas frecuentes.

## Estructura del Proyecto

El proyecto está organizado en dos carpetas principales:

1. **`chatbot-frontend`**: Contiene la aplicación React que sirve como interfaz de usuario.
   - `src/`: Carpeta con los archivos fuente de React.
   - `public/`: Contiene archivos estáticos y configuraciones para el frontend.

2. **`backend`**: Contiene los archivos relacionados con el servidor Flask y la API de Google.
   - `Gemini.py`: Código para interactuar con la API de Google Generative AI.
   - `GeminiChat.py`: Archivo Flask que maneja las peticiones del frontend.
   - `GanaderIAKey.json`: Archivo con credenciales para acceder a la base de datos de Google.

## Configuración del Proyecto

### Frontend (React)

1. **Instalación de Dependencias**

   ```bash
   cd chatbot-frontend
   npm install
