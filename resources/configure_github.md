# Configuración de GitHub en Git

Para configurar [GitHub](https://www.github.com) se necesita realizar una cuenta en la plataforma. Posteriormente se recomienda agregar una clave para el protocolo `ssh` asociada al dispositivo que se esté utilizando, esto con la fin de evitar métodos de autenticación menos prácticos y menos robustos.

## Diferencia entre Git y GitHub:

Git es el programa que permite gestionar el control de versiones haciendo uso de *commits*, *branches* y otras funcionalidades. 

GitHub es una plataforma de almacenameiento de repositorios de Git en la nube, existen otras plataformas para esto como: GitLab, BitBucket, entre otras.

## Instalar y configurar Git:

### Linux (Debian, Ubuntu, WSL)

Para instalar git realizar el siguiente comando en una terminal:

```bash
sudo apt update         # Actualiza la lista de repositorios a los paquetes.
sudo apt upgrade        # Actualiza los paquetes instalados para los que existan actualizaciones disponibles
sudo apt install git    # Instala git utilizando apt como administrador de paquetes
```

Posteriormente se debe configurar un nombre de usuario y correo de manera local para que Git pueda llevar un registro del quién hace los cambios.

```bash
git config --global user.email "ejemplo@ejemplo.com" 
git config --global user.name "Ejemplo Ejemplo"
```

### Windows (no WSL)

Descargar el [instalador](https://git-scm.com/download/win), ejecutarlo y seguir los pasos de instalación. Cuando se solicite, elija la opción que permita **agregar a la shell de Windows**.

En una terminal de Windows (PowerShell, Windows terminal, Git terminal, u otras variaciones) realizar los comandos de configuración.

```bash
git config --global user.email "ejemplo@ejemplo.com" 
git config --global user.name "Ejemplo Ejemplo"
```

## Configurar GitHub:

1. Entrar en [https://www.github.com](https://www.github.com) y crear una nueva cuenta.
2. Crear una nueva clave para la máquina que se desea asociar:
    
    Entrar a una terminal y realizar el comando:
    ```bash
    ssh-keygen
    ```
    Seguir los pasos dando `Enter` y escribiendo lo solicitado (si no desea agreagar una clave dejar en blanco esa sección).
3. Copiar la clave pública, esta es el texto que se encuentra en el archivo ubicado en `~/.ssh/id_rsa.pub`. Para visualizarla en una terminal se puede realizar el comando:
    ```bash
    cat ~/.ssh/id_rsa.pub
    ```
    **Nota:** el símbolo `~` representa la carpeta de usuario, es decir `/home/usuario` en Linux y `C:\Users\usuario` en Windows.
4. Abrir la configuración de GitHub, entrar en: `Settings > SSH and GPG keys`.
5. Seleccionar `New SSH key`.
6. Agregar un nombre para recordar a que máquina está asociada dicha clave.
7. Pegar la clave generada.

## Crear un nuevo repositorio local
Se puede crear un repositorio en cualquier directorio (carpeta) que se desee llevar un control de versiones. Para esto se debe ubicar dentro del directorio e inizializar un repositorio. Con el repositorio inicializado se puede llevar el control de versiones del mismo.

**Nota:** Todo este procedimiento es posibre realizarlo de manera gráfica desde VS-code pero por facilidad se explicará desde la línea de comandos.

```bash
cd path/al/directorio/deseado # Se ubica en el directorio
git init # Se inicializa un repositorio nuevo
```

**Nota:** si el directorio deseado ya pertenece a un repositorio no se debe inicializar un repositorio nuevo, si se desea puede copiar el directorio en otro lugar y realizar allí un nuevo repositorio. Existen métodos avanzados que permiten copiar el historial de cambios de un directorio a otro sitio y luego agregar este como un submódulo de repositorio original.

## Vincular un repositorio local a GitHub
Se debe crear un repositorio nuevo en GitHub, darle un nombre y después copiar las instrucciones indicadas.

1. Crear un repositorio nuevo, agreagar nombre y descripción pero no cambiar las opciones que permiten agregar un `README.md` o una `LICENCE`.
2. En una terminal ir al directorio que contiene el repositorio local:
    ```bash
    cd path/al/directorio/deseado # Se ubica en el directorio
    ```

3. Copiar las instrucciones de la sección *or push an existing repository from the command line*:
    ```bash
    git remote add origin git@github.com:JARA99/test.git
    git branch -M main
    git push -u origin main
    ```

¡Listo! Ahora para actualizar se pueden utilizar los comandos `git pull` y `git push` para sincronizar los datos de la nube a la máquina y de la máquina a la nube respectivamente. 


