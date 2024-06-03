# Repositorio de los proyectos de la asignatura de Diseño avanzado de sistemas de software - MITA.

Para crear el entorno de desarrollo deben de realizar los siguientes comandos (debes de tener instalado docker y docker compose, las instrucciones están en moodle):

Clonar el repo:
~~~
git clone https://gitlab.com/amgdark/software_mita.git
~~~


Ingresar al repo:
~~~
cd software_mita 
~~~

Iniciar la descarga, creación e instalación de las imágenes y contenedores:
~~~
docker compose up -d
~~~

Para ingresar al contenedor de las aplicaciones:
~~~
docker compose exec app bash
~~~

Para cerrar la sesión dentro del contenedor:
~~~
exit
~~~

Para apagar los contenedores:
~~~
docker compose down
~~~