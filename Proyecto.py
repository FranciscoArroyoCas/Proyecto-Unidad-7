from typeguard import typechecked

class Libro:
    @typechecked
    def __init__(self, titulo: str, autor: str, isbn: str, copias_disponibles: int):
        """
        Inicializa un objeto Libro con validación de tipos.
        Porqué: Se usa @typechecked para evitar errores de ejecución si se introducen 
        datos de tipo incorrectos.
        """
        self.titulo = titulo
        self.autor = autor
        self.__isbn = "0000000000000"     # ISBN por defecto para evitar nulos
        self.__copias_disponibles = 0    # Stock inicial controlado

        # Se usa el setter para validar el ISBN desde la creación del objeto
        self.isbn = isbn

        if copias_disponibles >= 0:
            self.__copias_disponibles = copias_disponibles

    @property
    def isbn(self):
        """Getter para acceder al atributo privado __isbn."""
        return self.__isbn

    @isbn.setter
    def isbn(self, nuevo_isbn):
        """Valida que el ISBN tenga 13 dígitos numéricos."""
        if len(nuevo_isbn) == 13 and nuevo_isbn.isdigit():
            self.__isbn = nuevo_isbn
        else:
            print("ERROR: El ISBN no es válido. Debe tener 13 dígitos.")

    @property
    def copias_disponibles(self):
        """Retorna el stock actual del libro."""
        return self.__copias_disponibles

    def incrementar_copias(self, cantidad):
        """Aumenta el stock. Usado para devoluciones o nuevas altas."""
        self.__copias_disponibles += cantidad
        return self.__copias_disponibles

    def decrementar_copias(self, cantidad):
        """
        Reduce el stock si hay disponibilidad.
        Porqué: Evita que el inventario tenga valores negativos, devolviendo -1 como error.
        """
        if cantidad > self.__copias_disponibles:
            return -1
        self.__copias_disponibles -= cantidad
        return self.__copias_disponibles

    def __str__(self):
        """Representación visual del objeto para el usuario final."""
        return f"Título: {self.titulo}, autor: {self.autor}, ISBN: {self.__isbn}, copias: {self.__copias_disponibles}"


class Inventario:
    @typechecked
    def __init__(self, coleccion_libros: list):
        """Contenedor principal de la lógica de negocio del sistema."""
        self.__coleccion_libros = coleccion_libros

    @property
    def coleccion_libros(self):
        """Retorna la lista completa de objetos Libro."""
        return self.__coleccion_libros

    def agregar_libro(self, libro):
        """
        Gestiona el alta de libros.
        Porqué: Si el ISBN ya existe, actualiza el stock en lugar de duplicarlo.
        """
        for l in self.__coleccion_libros:
            if l.isbn == libro.isbn:
                l.incrementar_copias(1)
                return "El Libro existe con lo cuál se ha incrementado su stock."
        
        self.__coleccion_libros.append(libro)
        return "Libro añadido."

    def alquilar_copia(self, titulo_o_isbn):
        """Busca un libro por nombre o código para realizar un préstamo."""
        for libro in self.__coleccion_libros:
            if libro.titulo == titulo_o_isbn or libro.isbn == titulo_o_isbn:
                if libro.decrementar_copias(1) != -1:
                    return libro
                else:
                    return "ERROR: El libro no tiene copias."
        return "ERROR: Libro no encontrado."

    def devolver_copia(self, isbn):
        """Registra el retorno de un libro al sistema mediante su ISBN."""
        for libro in self.__coleccion_libros:
            if libro.isbn == isbn:
                libro.incrementar_copias(1)
                return "Copia devuelta correctamente."
        return "ERROR: No existe un libro con ese ISBN."

    def listar_libros_disponibles(self):
        """Genera una lista solo con libros que tienen stock > 0."""
        lista = []
        for libro in self.__coleccion_libros:
            if libro.copias_disponibles > 0:
                lista.append(str(libro))
        return lista


def menu(inventario):
    while True:
        print("\n----- MENÚ -----")
        print("1. Listar libros disponibles")
        print("2. Alquilar libro")
        print("3. Devolver libro")
        print("4. Suma de libros que hay en stock")
        print("5. Salir")

        opcion = int(input("Elige una opción: "))

        match opcion:
            case 1:
                disponibles = inventario.listar_libros_disponibles()
                for l in disponibles:
                    print(l)

            case 2:
                dato = input("Introduce título o ISBN: ")
                resultado = inventario.alquilar_copia(dato)
                print(resultado)

            case 3:
                isbn = input("Introduce ISBN: ")
                print(inventario.devolver_copia(isbn))

            case 4:
                total = sum(libro.copias_disponibles for libro in inventario.coleccion_libros)
                print(f"Total de libros en stock: {total}")

            case 5:
                break

            case _:
                print("ERROR: Tiene que elegir un número del menú.")





def inicializar_inventario() -> Inventario:
    """Función para pre-cargar el inventario con datos para la prueba."""
    inventario = Inventario([])

    # Prueba de ISBN válido e inválido
    l1 = Libro("POO con Python", "Alice C.", "1234567890123", 2)
    l2 = Libro("Bases de Datos SQL", "Bob D.", "9876543210987", 3)
    l3 = Libro("POO con Python", "Alice C.", "1234567890123", 1)

    print("\n--- INICIALIZANDO INVENTARIO ---")
    print(inventario.agregar_libro(l1))
    print(inventario.agregar_libro(l2))
    print(inventario.agregar_libro(l3))

    # Prueba de asignación de ISBN inválido
    l2.isbn = "9876543210XXX"
    print(f"ISBN de L2 después de intento fallido: {l2.isbn}")

    # Pre-ajuste de stock
    inventario.alquilar_copia("Bases de Datos SQL")
    inventario.alquilar_copia("Bases de Datos SQL")
    inventario.alquilar_copia("1234567890123")
    print("--------------------------------")

    return inventario


if __name__ == "__main__":
 biblioteca = inicializar_inventario()
 menu(biblioteca)
