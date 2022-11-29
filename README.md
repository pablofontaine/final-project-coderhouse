# Proyecto final para Coderhouse
Este proyecto es realizado por:
- Fontaine Gilardi, Pablo Nicolas
- Magali, Nieva
- Victor Gianfranco, Flores

## Temática del proyecto
Realizado con Python, con framework Django.
Hemos decidido realizar un blog de "Tenis y Jugadores".

- Sistema de registro y autenticación (login y logout) de usuarios, mediante modulo nativo de Django.
- CRUD completo para la gestión de usuarios, mediante vistas basadas en clases.
-CRUD completo para la gestión de noticias, mediante vistas basadas en clases. Solo superusuarios tienen acceso a crear y modificar noticias.
- CRUD completo para la gestión de jugadores, mediante vistas basadas en clases. Solo superusuarios tienen acceso a crear y modificar jugadores.
- Los usuarios puede cargar un avatar personal, ver noticias y jugadores.
    - Los usuarios utilizan el modelo por defecto User
    - Las noticias utilizan el modelo New, creado para este sitio.
    - Los jugadores utilizan el modelo Player, creado para este sitio.

## Estructura del proyecto y ramas de trabajo
Hemos dividido el proyecto de la siguiente manera, para organizar el trabajo.
- branch 'master': aquí hemos realizado los merge con el código probado y funcionando desde la rama 'develop'
- branch 'develop': aqui realizamos los merge de las ramas personales de desarrollo. Aquí unimos los códigos personales y realizamos pruebas de integración, para luego migrar a la rama master.
- branch 'develop_[name]': a partir de 'develop'. Existen 3 ramas de estas, una por cada miembro. Acá cada uno desarrolla su parte del trabajo, que luego de probado personalmente, realiza pull request a la rama 'develop'.
    - Rama de desarrollo de Magui: 'develop_magui' a partir de la rama develop.
    - Rama de desarrollo de Victor: 'develop_victor' a partir de la rama develop.
    - Rama de desarrollo de Pablo: 'develop_pablo' a partir de la rama develop.

## Instrucciones para iniciar proyecto en local
Bash de Windows
1. En una ruta y carpeta elegida para almacenar el repositorio, abrir un bash y tipear:
~~~
git clone https://github.com/pablofontaine/final-project-coderhouse.git
cd final-project-coderhouse
~~~
2. Crear/activar entorno virtual
~~~
python -m venv venv
./venv/Scripts/activate
~~~
3. Instalar requisitos
~~~
pip install -r requirements.txt
~~~
4. Iniciar el proyecto en servidor local
~~~
cd blog
python manage.py runserver
~~~
5. Visitar sitio en URL local, por defecto: 'localhost:8000'
[Visitar sitio en servidor local](localhost:8000)