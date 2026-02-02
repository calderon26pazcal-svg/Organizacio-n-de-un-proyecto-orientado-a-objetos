"""
Dashboard - Programación Orientada a Objetos (Personalizado)

Cambios realizados por: Marilin Calderon
Fecha: 2026-02-01
Descripción:
- Se añadió persistencia de tareas en JSON (tasks.json)
- Se añadió menú para gestionar tareas del curso (ver/agregar/completar/eliminar)
- Se mejoró la organización del código con funciones y validaciones
"""

import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
TASKS_FILE = BASE_DIR / "tasks.json"

CONFIG = {
    "usuario": "Marilin Calderon",
    "curso": "Programación Orientada a Objetos",
}

PRIORIDADES_VALIDAS = ("Alta", "Media", "Baja")


def load_tasks():
    """Carga tareas desde tasks.json. Si no existe, retorna lista vacía."""
    if not TASKS_FILE.exists():
        return []
    try:
        return json.loads(TASKS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        # Si el archivo está dañado o vacío, evita que el programa se caiga
        return []


def save_tasks(tasks):
    """Guarda tareas en tasks.json con formato legible."""
    TASKS_FILE.write_text(
        json.dumps(tasks, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def add_task(tasks, titulo, unidad="General", prioridad="Media"):
    """Agrega una tarea a la lista."""
    tasks.append({
        "titulo": titulo.strip(),
        "unidad": unidad.strip(),
        "prioridad": prioridad,
        "estado": "Pendiente",
        "creada": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })


def list_t_
