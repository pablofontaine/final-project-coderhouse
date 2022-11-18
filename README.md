# Proyecto final para Coderhouse
Este proyecto es realizado por:
- Magali, Nieva
- Victor Gianfranco, Flores
- Fontaine Gilardi, Pablo Nicolas

## Temática del proyecto
Realizado con Python, con framework Django.
Hemos decidido realizar un blog de "cocina y recetas".
- El proyecto cuenta con 3 aplicaciones, 

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