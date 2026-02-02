# PROGRAMACION-ORIENTADA-A-OBJETOS
Este repositorio contiene el código fuente desarrollado durante la asignatura **Programación Orientada a Objetos**, impartida en la **Universidad Estatal Amazónica**. Está diseñado como un recurso de apoyo para estudiantes y profesionales interesados en conceptos y prácticas de programación orientada a objetos.

## Información de la asignatura

- **Institución**: Universidad Estatal Amazónica (UEA)  
- **Carrera**: Ingeniería en Tecnologías de la Información  
- **Asignatura**: Programación Orientada a Objetos  

## Contenido del repositorio

Este repositorio incluye:
1. Ejercicios prácticos de programación orientada a objetos.
2. Ejemplos de implementación en Python.
3. Proyectos desarrollados como parte de las actividades de la asignatura.
4. Documentación y apuntes adicionales para reforzar el aprendizaje.

## Objetivos

- Aplicar los principios fundamentales de la programación orientada a objetos.
- Desarrollar soluciones eficientes y estructuradas utilizando Python.
- Familiarizarse con conceptos como clases, objetos, herencia, polimorfismo y encapsulamiento.

## Instrucciones para el uso

1. Clona el repositorio:  
   ```bash
   git clone https://github.com/snogales-uea/2525-PROGRAMACION-ORIENTADA-A-OBJETOS.git
   cd 2525-PROGRAMACION-ORIENTADA-A-OBJETOS 

2. Crear un nuevo repositorio en tu cuenta de GitHub Ve a GitHub: https://github.com/new

3. Cambiar el repositorio remoto del proyecto clonado
   ```bash
   git remote remove origin
   git remote add origin https://github.com/tu-usuario/proyecto-clonado.git

4. Subir el proyecto a tu repositorio personal
   ```bash
   git push -u origin main

## Personalización del Dashboard

**Estudiante:** Marilin Calderon  
**Asignatura:** Programación Orientada a Objetos  
**Institución:** Universidad Estatal Amazónica  

### Descripción de los cambios realizados
Para esta tarea se realizaron adaptaciones al archivo `Dashboard.py` con el fin de personalizarlo para la gestión de actividades del curso. Las principales modificaciones fueron:

- Personalización del Dashboard con el nombre del estudiante y la asignatura.
- Implementación de un sistema de gestión de tareas mediante consola.
- Almacenamiento de tareas utilizando un archivo `tasks.json` para mantener la información de forma persistente.
- Opciones para:
  - Ver tareas registradas.
  - Agregar nuevas tareas.
  - Marcar tareas como completadas.
  - Eliminar tareas.
- Validación de la prioridad de las tareas (Alta, Media o Baja).
- Organización del código mediante funciones y comentarios descriptivos.

### Ejecución del programa
Para ejecutar el Dashboard, ubíquese en la carpeta del proyecto y ejecute el siguiente comando:

```bash
python Dashboard.py
