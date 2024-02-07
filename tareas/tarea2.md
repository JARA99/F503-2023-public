# Tarea 2

## Instrucciones

El objetivo de esta tarea es que se realicen todas las configuraciones necesarias para trabajar durante el semestre, además que comience a acostumbrarse a utilizar las herramientas que serán utilizadas durante el curso.

### Cree un repositorio para el curso

Cree un nuevo directorio donde se almacenarán las tareas, prácticas y otros archivos que desee sobre el curso con la siguiente estructura:

```
LabRedDat/
├── notas (opcional)
│   └── clase1.py
├── practicas
│   └── p1
└── tareas
    ├── t1
    └── t2
```

Genere un repositorio nuevo en este directorio:

```bash
cd LabRedDat
git init
```
Cree un repositorio **público** en la nube utilizando GitHub y suba el repositorio local a este. Puede encontrar información sobre como realizar esto en la página de [Configuración de GitHub en Git](../resources/configure_github.md).

### Ejecute el cuaderno realizado en clase

Ejecute una copia del [cuaderno](../Introduccion/introduccion.ipynb) en su computadora, colocando su nombre en el saludo, además genere una nueva gráfica de tipo `scatter` donde el eje *x* represente la profundidad del pico en milímetros `bill_depth_mm` y el eje *y* represente la longitud de la aleta `flipper_length_mm` manteniendo el color asociado a la especie.

**Nota:** Coloque la copia de este cuaderno en la carpeta `tareas/t2`.

### Ejecute el ejercicio de Streamlit

Ejecute de manera local la [página de streamlit](../Introduccion/streamlit_tests.py) creada en clase. Si todo está en orden agregue la nueva gráfica creada en el cuaderno copiando el código de esta, almacenandola en una variable y colocandola en la página.

Recuerde que para ejecutar la página de streamlit se utiliza el comando `streamlit run nombre_del_archivo.py`

**Nota:** Coloque la copia de la página de streamlit en la carpeta `tareas/t2`.

### Guarde sus cambios y realice una `commit`

Después de haber realizado lo anterior guarde todos sus cambios y realice una nueva commit. En una terminal puede realizarlo utilizando el comando:

```bash
cd LabRedDat/tareas/t2  # Se ubica en el directorio de la tarea 2.
git add .               # Agrega todos los cambios dentro del directorio a la cache para ponerlos dentro del commit
git commit -m 'tarea 2' # Realiza la commit y la nombra tarea 2
git push                # Sube los cambios a la nube
```

### Ejecute streamlit y publique la página

Después de haber subido sus cambios a GitHub podrá hacer `deploy` de su página, ejecute de nuevo la página de streamlit `streamlit run nombre_del_archivo.py` y en la esquina superior derecha verá un botón que indica `deploy`. Seleccionelo y seleccione la opción ``Streamlit Community Cloud''.

Deberá crear una cuenta utilizando Google o GitHub, recomiendo utilizar GitHub directamente ya que será necesario vincularlo de cualquier modo.

Streamlit solicitará permisos de visualización y edición de algunas cosas en GitHub, debe autorizarlos.

En automático Streamlit llenará el formulario que solicita el repositorio, rama y archivo para darle `deploy` a la página. Seleccione el botón `deploy` y espere a que la página sea generada.

#### Error por falta de dependencias

Para que Streamlit pueda saber que paquetes necesita el programa es necesario darle un archivo `requirements.txt`, este puede ser generado utilizando el comando:

```
cd LabRedDat/tareas/t1          # Entrar en el directorio de la tarea
pip freeze > requirements.txt   # Generar una lista de requerimientos
```

Es por esto que se recomienda tener instalaciones separadas de Python para cada proyecto utilizando `virtualenv`, así se evita una lista de requerimientos con paquetes innecesarios.

En esta ocación pueden utilizar crear el archivo [`LabRedDat/tareas/t2/requirements.txt`](../Introduccion/requirements.txt) con los siguientes requerimientos:

```python
altair==5.2.0
attrs==23.2.0
blinker==1.7.0
cachetools==5.3.2
certifi==2024.2.2
charset-normalizer==3.3.2
click==8.1.7
gitdb==4.0.11
GitPython==3.1.41
idna==3.6
importlib-metadata==7.0.1
Jinja2==3.1.3
jsonschema==4.21.1
jsonschema-specifications==2023.12.1
markdown-it-py==3.0.0
MarkupSafe==2.1.5
mdurl==0.1.2
numpy==1.26.4
packaging==23.2
pandas==2.2.0
pillow==10.2.0
plotly==5.18.0
protobuf==4.25.2
pyarrow==15.0.0
pydeck==0.8.1b0
Pygments==2.17.2
python-dateutil==2.8.2
pytz==2024.1
referencing==0.33.0
requests==2.31.0
rich==13.7.0
rpds-py==0.17.1
six==1.16.0
smmap==5.0.1
streamlit==1.31.0
tenacity==8.2.3
toml==0.10.2
toolz==0.12.1
tornado==6.4
typing_extensions==4.9.0
tzdata==2023.4
tzlocal==5.2
urllib3==2.2.0
validators==0.22.0
watchdog==3.0.0
zipp==3.17.0
```

Ahora basta con guardar los cambios, agregarlos a una nueva `commit` y subirlos de nuevo utilizando `git push` (o la interfaz de VS-code). En la esquina inferior derecha de la página de Streamlit que dió error hay un botón que dice `Manage app`, haga click en el y en los tres puntos e intente hacer un `Reboot` de la aplicación, si esto no arregla el error entonces borre la aplicación (`Delete`) e intente hacer el deploy de nuevo.

#### ¡Felicidades! su primera app de Streamlit

Una vez realizado el deploy con éxito puede compartir su aplicación copiando el enlace de la misma (el de la versión del deploy, no el `localhost`).

En la entrega de su tarea coloque el enlace tanto de esta aplicación como del repositorio creado en la carpeta de la tarea 2.
