
de pila import  *
 Libro de clase :
    
    def  __init__ ( self , nombre ,autor, tematica ,paginas,editorial):
        auto .n = nombre
         auto.a=autor
        auto .t = tematica
        auto .p = paginas
      auto .e = editorial


    
    def  getNombre ( self ):
        volver  auto .n       
    def  getNombre ( self ):
        volver  auto .a
        def  getNombre ( self ):
        volver  auto .t     
    def  getNombre ( self ):
        volver  auto .p
        def  getNombre ( self ):
        volver  auto .e  

libro1= libro(El principito,Antoine de Saint,ciencia ficcion,182,libroz)
libro2=libro(Los miserables,Victor hugo,Novela,256,norma)
libro3=libro(La divina comedia,Dante Alighieri,ciencia ficcion,182,risitas)
libro4=libro(Alicia en el pais de las maravillas,Lewis carroll,ciencia ficcion,164,spec)
libro5=libro(Cien años de soledad,Gabriel garcia,novela,420;norma)
libro6=libroEl conde de montecristo,Alejandro dumashistoria,171,spec)
libro7=libro(Don quijote de la mancha,Miguel de cervantes,cuento,174,norma)
libro8=libro(El perfume,patrick sustkind,comedia,125,norma)
libro9=libro(Elretrato de dorian grey,oscar wilde,cuento,186,papelin)
libro10=libro(El señor de los anillos,J.r.r tolkien,comedia,100,torren)
libro11=libro(La Casa de Papel,Nicolas Garzon,historia,122,papelin)
libro12=libro(Narcos,Laura Casas,ciencia ficción,179,torren)
libro13=libro(La Bella y la Bestia,Armando Perez,cuento,110,torren)
libro14=libro(Matilda,Santiago Ruiz,cuento,98,edilibro)
libro15=libro(La Bruja,Pepe Sanchez,terror,136,spec)
libro16=libro(El Aro,Sara Garay,terror,157,papelin)
libro17=libro(Mision Imposible,Nicolas Garzon,ciencia ficción,168,spec)
libro18=libro(Que paso ayer,Elkin Paz,comedia,133,torren)
libro19=libro(Los Reyes,Tatiana Diaz,historia,127,edilibro)
libro20=libro(Pinocho,Pepe Sanchez,cuento,80,edilibro)
pila = pila ()

imprimir ( " una continuación se agregará a la pila los libros" +  " \ n " )

pila.apilar (libro1.getNombre ())
pila.apilar (libro2.getNombre ())
pila.apilar (libro3.getNombre ())
pila.apilar (libro4.getNombre ())
pila.apilar (libro5.getNombre ())
pila.apilar (libro6.getNombre ())
pila.apilar (libro7.getNombre ())
pila.apilar (libro8.getNombre ())
pila.apilar (libro9.getNombre ())
pila.apilar (libro10.getNombre ())
pila.apilar (libro11.getNombre ())
pila.apilar (libro12.getNombre ())
pila.apilar (libro13.getNombre ())
pila.apilar (libro14.getNombre ())
pila.apilar (libro15.getNombre ())
pila.apilar (libro16.getNombre ())
pila.apilar (libro17.getNombre ())
pila.apilar (libro18.getNombre ())
pila.apilar (libro19.getNombre ())
pila.apilar (libro20.getNombre ())

imprimir ( " los elementos de la pila son los siguientes: " +  " \ n " )
imprimir (pila.items)
imprimir ( " \ n " )
imprimir ( " A continuacion se Desapilaran los elementos: " +  " \ n " )          
    
Si bien pila.es_vacia () ! =  Verdadero :
    imprimir (pila.desapilar ())
imprimir ( " \ n " )
imprimir ( " la pila esta vacia " +  " \ n " )
imprimir (pila.items)
