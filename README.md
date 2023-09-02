# PyRepoSearch

PyRepoSearch es un proyecto creado en Python que permite buscar carpetas con un nombre determinado en varios repositorios de red que hayas especificado. Con PyRepoSearch, puedes encontrar carpetas en diferentes tipos de repositorios, como carpetas compartidas, servidores FTP y más.

## Características

- Busca carpetas con un nombre determinado en repositorios de red usando la entrada del usuario.
- Muestra las carpetas encontradas en la terminal con sus rutas completas.
- Permite acceder a las carpetas encontradas directamente desde la terminal o copiar sus enlaces.
- Establece un tiempo máximo de búsqueda en cada repositorio para evitar bloqueos o esperas innecesarias.

## Requisitos

Para ejecutar PyRepoSearch, necesitas tener instalado Python 3.6 o superior y las siguientes librerías:

- os
- time
- ftplib
- subprocess

Puedes instalarlas usando el comando `pip install -r requirements.txt`.

Una vez descargado, edita el script en el comentario "Especifica los repositorios de red" y especifica los repositorios que quieras utilizar.

## Uso

Para iniciar PyRepoSearch, ejecuta el archivo `pyreposearch.py` desde la terminal o desde tu IDE preferido. Aparecerá una ventana donde podrás introducir el nombre de la carpeta a buscar. Después de pulsar la tecla "Enter", se iniciará la búsqueda en los repositorios especificados. Se mostrarán las carpetas encontradas o los mensajes de error en caso de que haya algún problema. También podrás acceder a las carpetas encontradas o copiar sus enlaces usando los comandos que se indican. Para salir del programa, presiona cualquier tecla.

## Licencia

PyRepoSearch está licenciado bajo la [Licencia MIT], lo que significa que puedes usarlo, modificarlo y distribuirlo libremente, siempre que incluyas el archivo `LICENSE.txt` original y una nota de atribución.

## Contribuciones

Si quieres contribuir al desarrollo de PyRepoSearch, puedes hacerlo de varias formas:

- Reportando errores o sugerencias a través de la sección de [Issues] del repositorio.
- Enviando tus propios cambios o mejoras mediante [Pull Requests].
- Ayudando a mejorar la eficiencia o la compatibilidad del código con otros tipos de repositorios.
