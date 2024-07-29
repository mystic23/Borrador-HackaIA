# Proyecto de Chatbot para ProcessOptima - HackaIA

## Descripción

Este proyecto consiste en un chatbot diseñado para mejorar la eficiencia y comunicación interna de la empresa ProcessOptima. El chatbot proporciona información sobre procesos internos relacionados con ganadería sostenible. El backend está desarrollado en Flask y se encarga de manejar las peticiones del frontend y comunicarse con la API de Google Generative AI para obtener respuestas.

## Qué Hace el Proyecto

El chatbot tiene como objetivo principal facilitar el acceso a la información sobre procesos internos de la empresa en las áreas de ganadería  sostenible. Las principales funcionalidades incluyen:

- **Consulta de Información**: Permite a los usuarios hacer preguntas sobre diversos aspectos relacionados con los procesos internos de la empresa en manejo de las fincas y el cuidado apropiado
- **Generación de Respuestas**: Utiliza la API de Google Generative AI para generar respuestas precisas y relevantes a las preguntas de los usuarios, sin embargo, no se hace uso directo de este
- **Mejora de la Comunicación Interna**: Facilita el acceso a la información relevante, mejorando la eficiencia en la comunicación interna y reduciendo el tiempo necesario para obtener respuestas a preguntas frecuentes.

## Estructura del Proyecto

- `static/`: Carpeta que contiene las imágenes utilizadas en el proyecto.
- `templates/`: Carpeta que contiene los archivos HTML para el frontend.
- `api.py`: Archivo que gestiona las claves API y la configuración de acceso a Google Cloud.
- `GeminiChat.py`: Archivo principal del backend en Flask que maneja las peticiones del frontend e interactúa con la API de Google Generative AI.

## Dependencias


1. **Instalación de Dependencias**
   `pip install -r requirements.txt
