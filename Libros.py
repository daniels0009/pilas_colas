clase  Pila :
    "" " Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. ""

    def  __init__ ( self ):
        "" " Crea una pila vacía. " ""
        # La pila vacía se r {epresenta con una lista vacía
        auto .items = []

    def  apilar ( self , x ):
        "" " Agrega el elemento xa la pila. " ""
        # Apilar es agregar al final de la lista.
        auto .items.append (x)

    def  desapilar ( uno mismo ):
        "" Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. ""
        tratar :
            volver  auto .items.pop ()
        excepto  IndexError :
            elevar  ValueError ( " La pila está vacía " )

    def  es_vacia ( self ):
        "" " Devuelve True si la lista está vacía, False si no. " ""
        volver  auto .items == []
clase  libro :
    def  __init__ ( self , nombre , categoria  ):
        auto .nombre = nombre
        auto categoria = categoria
          clase  Pila :
    "" " Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. ""

    def  __init__ ( self ):
        "" " Crea una pila vacía. " ""
        # La pila vacía se r {epresenta con una lista vacía
        auto .items = []

    def  apilar ( self , x ):
        "" " Agrega el elemento xa la pila. " ""
        # Apilar es agregar al final de la lista.
        auto .items.append (x)

    def  desapilar ( uno mismo ):
        "" Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. ""
        tratar :
            volver  auto .items.pop ()
        excepto  IndexError :
            elevar  ValueError ( " La pila está vacía " )

    def  es_vacia ( self ):
        "" " Devuelve True si la lista está vacía, False si no. " ""
        volver  auto .items == []
clase  libro :
    def  __init__ ( self , nombre , categoria ):
        auto .nombre = nombre
        auto categoria = categoria
            def  getNombre ( self ):
        volver  auto .nombre
def  getNombre ( self ):
        volver  auto .categoria


archivo =  abierto ( " libros.csv " , " r " )
lista = [(x.split ( " ; " ) [ 0 ], x.split ( " ; " ) [ 1 ]) para x en archivo.readlines ()]

pila = pila ()
para x en la lista:
    libro = Libro (x [ 0 ], x [ 1 ] .strip ( " \ n " ) .strip ( " \ r " ) .strip ( "  " ))
    pila.apilar (libro)

opcion =  int ( input ( " digite la opcion que desea realizar \ n 1 si desea buscar por nombre del libro \ n 2 si desea buscar por categoria del libro \  " ))
if (opcion ==  1  u opcion ==  2  ):
    busqueda =  raw_input ( " digite para empezar the busqueda \ n " )
                elif (opcion ==  1 ):
                if (ultimoLibro.nombre == busqueda):
                    validacion =  Verdadero
            elif (opcion ==  2 ):
                if (ultimoLibro.autor == busqueda + " \ n " ):
                    Imprimir  " ENTRO "
                    validacion =  Verdadero
            si (validacion ==  Verdadero ):
                imprimir  " Primer libro encontrado con la especificacion es \ n nombre del libro: " , ultimoLibro.nombre, "  \ n categoria: " , ultimoLibro.categoria,"
        excepto  IndexError :
            imprimir  " La pila está vacía, no se encuentra un libro con estas especificaciones "
            validacion =  Verdadero
otra cosa :
    Imprimir  " opcion invalida "
