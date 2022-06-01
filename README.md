# Api Task
El siguiente proyecto para la asignatura programación III.
## Despliegue
Para el despliegue vamos a clonar el repositorio

```
git clone https://github.com/jmgalviis/api-task.git
```

ingresamos al directorio creado

```
cd api-task
```

Creamos el entorno virtual

```
python -m virtualenv venv
```

Activamos el entorno virtual en windows

```
.\venv\Scripts\activate
```

En *nix o Mac

```
source venv/bin/activate
```

una vez activado el entorno virtual procedemos a instalar las dependencias

```
pip install -r requirements.txt
```

una vez termine de instalar las dependencias ejecutamos

```
python main.py
```

Versiones usadas

Python 3.10

PostgreSQL 13

Para realizar pruebas pueden utilizar [postman](https://www.postman.com) o [insomnia](https://insomnia.rest) 
