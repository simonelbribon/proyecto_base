# Proyecto Base

> Plataforma base para el desarrollo del pipeline **SEME** utilizando FastAPI, Pytest y una arquitectura limpia orientada a eventos.

---

## Objetivo

Este proyecto constituye la base de una plataforma de procesamiento denominada **SEME**.

Actualmente implementa:

- API REST con FastAPI
- Pipeline desacoplado de la capa HTTP
- Pruebas automatizadas con Pytest
- Arquitectura preparada para evolucionar hacia procesamiento de eventos
- Integración con Git y GitHub

---

## Arquitectura


Cliente
│
▼
FastAPI
│
▼
API (/v1)
│
▼
Pipeline SEME
│
▼
Resultado


La lógica de negocio permanece independiente del framework web, permitiendo reutilizar el pipeline desde otros componentes.

---

## Estructura del proyecto


proyecto_base/

├── src/
│ ├── api/
│ ├── seme/
│ └── main.py
│
├── tests/
│
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore


---

## Requisitos

- Python 3.14+
- FastAPI
- Uvicorn
- Pytest

---

## Instalación

Crear entorno virtual:

```bash
python -m venv ds_env

Activar:

Linux

source ds_env/bin/activate

Instalar dependencias:

pip install -r requirements.txt
Ejecutar la API
uvicorn src.main:app --reload

Abrir:

http://127.0.0.1:8000/docs
Ejecutar pruebas
pytest -v
Endpoint principal

POST

/v1/pipeline

Ejemplo:

{
    "text": "Hola SEME"
}

Respuesta:

{
    "seme": "hola seme",
    "final": "HOLA SEME"
}
Estado del proyecto

Versión actual

v1.0

Estado

API estable
Tests aprobados
Repositorio GitHub
Pipeline desacoplado
Roadmap
v1.1
Schemas con Pydantic
Logging estructurado
Configuración centralizada
v1.2
Procesamiento de eventos
Pipeline enriquecido
Trazabilidad
v2.0
Plataforma SEME completa
Arquitectura orientada a eventos
Publicadores y consumidores
Filosofía del proyecto

El objetivo no es únicamente construir una API.

La meta es desarrollar una plataforma mantenible, desacoplada y evolutiva, donde cada componente tenga una responsabilidad clara y pueda crecer sin comprometer el resto del sistema.

Licencia

MIT
