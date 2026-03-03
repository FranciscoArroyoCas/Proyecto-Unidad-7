#  Mi Proyecto de Gestión de Biblioteca



Este es el ejercicio de Python que he hecho para gestionar el inventario de una biblioteca. Sirve para llevar el control de qué libros hay, alquilarlos y devolverlos usando el ISBN.



---



##  Lo que necesitas para que funcione

Para que no te dé errores al ejecutarlo, asegúrate de tener esto instalado:



### Requisitos:

* **Python:** 3.10 o más nuevo

* **Librería Typeguard:** Versión 4.0.0



> **Importante:** He usado 'match-case', así que si usas un Python antiguo no te va a funcionar.



---



##  Cómo ponerlo en funcionamiento (Paso a paso)

He intentado que sea fácil de instalar para que el siguiente que lo use no pierda el tiempo:



1. **Descarga el código:** Clona el repositorio o bájate la carpeta del proyecto.

2. **Instala la librería de tipos:** Como he usado `@typechecked` para que los datos sean correctos, tienes que instalar esto en la terminal:

```bash

pip install typeguard

---

##  Para que se entienda cómo he hecho el código, aquí lo explico:

**Libro:** He creado esta clase para los libros. Se encarga de guardar la información y controla que los datos sean correctos. Por ejemplo, el ISBN tiene que ser de 13 números sí o sí usando un **setter**, si no, el programa te avisa.

**Inventario:** Esta clase es la que maneja la lista de libros. Tiene las funciones para alquilar y devolver, y se encarga de que si añades un libro que ya existe, solo suba el número de copias en vez de repetirlo.

**Patrón usado:** He usado **Programación Orientada a Objetos** para separar lo que es un "Libro" de lo que es la "Gestión" del inventario.

###  Mantenimiento y Tests
Si alguien quiere ampliar este programa o comprobar que todo está bien, he dejado esto preparado:

**Cómo probarlo:** Al final del archivo `.py` he creado una función llamada `inicializar_inventario()`. Ahí he metido unos cuantos libros de prueba para comprobar que las validaciones y el stock funcionan bien nada más arrancar.

**Para los que vayan a modificar el código:** Si vas a añadir funciones, recuerda usar `@typechecked`. Sirve para que, si te equivocas metiendo un texto donde va un número, el programa de un error.

















