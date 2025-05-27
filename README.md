# 🎵 AsuMusic Blog

AsuMusic Blog es una plataforma web donde los amantes de la música pueden leer, crear y comentar artículos sobre géneros musicales, artistas, álbumes, conciertos y mucho más. El proyecto está desarrollado con Django y utiliza Bootstrap 5 para una interfaz moderna y responsive, junto con `django-crispy-forms` para mejorar la presentación de formularios y `Pillow` para el manejo de imágenes.

---

## 🚀 Características

- Registro e inicio de sesión de usuarios
- Crear, editar y eliminar entradas del blog

- Panel de administración con gestión de usuarios y contenido
- Formularios personalizados con Bootstrap 5

---

## 📁 Estructura del Proyecto


└── sdazap-proyblog/

    ├── users.txt
    └── proyblog/
        ├── db.sqlite3
        ├── manage.py
        ├── blog/
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── models.py
        │   ├── tests.py
        │   ├── urls.py
        │   ├── views.py
        │   ├── __pycache__/
        │   ├── migrations/
        │   │   ├── __init__.py
        │   │   └── __pycache__/
        │   ├── static/
        │   │   └── blog/
        │   │       └── main.css
        │   └── templates/
        │       └── blog/
        │           ├── about.html
        │           ├── base.html
        │           ├── home.html
        │           ├── post_confirm_delete.html
        │           ├── post_detail.html
        │           └── post_form.html
        ├── media/
        │   └── profile_pics/
        ├── proyblog/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   ├── wsgi.py
        │   └── __pycache__/
        └── users/
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── forms.py
            ├── models.py
            ├── signals.py
            ├── tests.py
            ├── views.py
            ├── __pycache__/
            ├── migrations/
            │   ├── __init__.py
            │   └── __pycache__/
            └── templates/
                └── users/
                    ├── login.html
                    ├── logout.html
                    ├── profile.html
                    ├── profileUpdate.html
                    └── register.html


---

## 🛠️ Instalación y configuración

Sigue estos pasos para instalar y ejecutar el proyecto localmente.

### 1. Clonar el repositorio

```bash
git clone https://github.com/SdazaP/proyblog
cd proyblog
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
pip install -r requirements.txt
```
Si no tienes el archivo requirements.txt, puedes instalar los paquetes principales de forma manual:
```bash
pip install django
pip install django-crispy-forms
pip install crispy-bootstrap5
pip install Pillow
```
### 🔄 Migraciones y ejecución
1. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```
2. Crear superusuario
```bash
python manage.py createsuperuser
```
Sigue las instrucciones para establecer nombre de usuario, correo y contraseña.

3. Ejecutar el servidor
```bash
python manage.py runserver
