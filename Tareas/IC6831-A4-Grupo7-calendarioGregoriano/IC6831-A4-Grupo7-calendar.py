import tkinter
from tkinter import*


#clase que realiza validaciones de fechas de calendario
#Atributos: mensaje: sirve para guardar algun mensaje de error

class ValidatorTipoDatosCalendario:
#Funcion es_numero
#Entradas: un string
#Salidas: Booleano que determina si string es unicamente numerico
#Proceso: recorre caracter por caracter a ver si es numero
    def es_numero(self,num):
        if len(num) == 0:
            return False
        for i in num:
            if i not in "1234567890":
                return False
        return True


#Funcion: es_dato_de_calendario
#Entradas: Un numero
#Salidas un booleano que determina si el numero puede ser un dia, mes o anio
#Proceso: revisa si dato es un numero entero y positivo y esta dentro de los rangos de dias, mese y anios
    def es_dato_de_calendario(self,num):
        if num < 0:
            return False
        elif num in range (1,13) or num in range (1,32) or num >= 1582:
            return True
        else:
            return False

###################################################################################
                
#Clase Calendario
#Hace consultas y calculos sobre fechas de un calendario
class Calendario:
    mensajeError = ""

#Funcion: bisiesto
#Entradas: un anio
#Salidas: un booleano
#Proceso: se hace validacion de datos y luego se usa el modulo 4 para ver
#         si es divisible por 4

    def bisiesto(self, anio):
        return anio % 4 == 0

#Funcion: fecha_es_valida
#Entradas: una tupla (anio,mes,dia)
#Salidas: un booleano
#Proceso: Se toma en consideracion los siguientes aspectos:
#           -El mes debe estar entre 1 y 12
#           -El dia depende del mes y anio
#           -Febrero tiene 29 dias en un anio bisiesto y sino 28
#           -Meses con 31 dias: Enero, marzo, mayo, julio, agosto, octubre y
#           diciembre
#           -Mese con 30 dias: Abril, junio, setiembre y noviembre

    def fecha_es_valida(self,fecha):
        anio = fecha[0]
        mes = fecha[1]
        dia = fecha[2]

        if mes != 2:
            if mes in [1,3,5,7,8,10,12] and dia in range(1,32):
                return True
            elif mes in [4,6,9,11] and dia in range(1,31):
                return True
            else:
                self.mensajeError = "Dia y mes invalido"
                return False
        else:
            if self.bisiesto(anio):
                if dia in range(1,30):
                    return True
                else:
                    self.mensajeError = "Febrero tiene 29 dias en un anio bisiesto"
                    return False
                
            else:
                if dia in range(1,29):
                    return True
                else:
                    self.mensajeError = "Febrero tiene 28 dias en un anio no bisiesto"
                    return False

#Funcion dia_siguiente
#Entradas: una tupla (anio,mes,dia)
#Salidas: una tupla con la fecha del siguiente dia
#Proceso: se usa la funcion fecha_es_valida y su estructura para ver si dia + 1 aun es valido
                
    def dia_siguiente(self, fecha):
        
        anio = fecha[0]
        mes = fecha[1]
        dia = fecha[2]


        if self.fecha_es_valida(fecha):
            if mes == 12 and dia == 31:
                return (anio + 1, 1, 1)

            if self.fecha_es_valida((anio, mes, dia+1)):
                return (anio, mes, dia + 1)

            else:
                return (anio, mes + 1, 1)
        else:
            return ()


#Funcion dias_desde_primero_de_enero
#Entradas: una tupla fecha (anio, mes, dia)
#Salidas: un entero con la cantidad de dias desde el primero de enero
#Proceso: se va incrementando dias desde la fecha primero de enero de 2018 hasta la ingresada usando dia_siguiente

    def dias_desde_primero_de_enero(self,fecha):
        anio = fecha[0]
        mes = fecha[1]
        dia = fecha[2]
        
        dias = 0
        fechaActual = (anio,1,1)
        

        if not self.fecha_es_valida(fecha):
            return
        else:
            
            while fechaActual != fecha:
                fechaActual = self.dia_siguiente(fechaActual)
                dias = dias + 1
            return dias

#Funcion dia_de_hoy
#Entradas: una tupla fecha (anio,mes,dia)
#Salidas: Un digito representando dia de semana 0:domingo...6:sabado
#Proceso: tomado de: http://code.activestate.com/recipes/266464-date-to-day-of-the-week/
    def dia_de_hoy(self,fecha):
        anio = fecha[0]
        mes = fecha[1]
        dia = fecha[2]
        
        if mes < 3:
            z = anio - 1
        else:
            z = anio
        diaSemana = ( 23*mes//9 + dia + 4 + anio + z//4 - z//100 + z//400 )
        if mes >= 3:
            diaSemana -= 2
        diaSemana = diaSemana % 7
        return diaSemana

#funcion dia primero de enero
#Entradas un anio
#Salidas: un digito representado dia de semana 0:domingo..6:sabado
#Proceso: se usa la funcion dia_de_hoy con el primero de enero
    def dia_primero_enero(self,anio):
        return self.dia_de_hoy((anio,1,1))
                       
                
########################################################
#clase CalendarController
#Clase que interactua con la interfaz y las clases de Calendario y ValidatorTipoDatosCalendario
class CalendarController:
    validator = ValidatorTipoDatosCalendario()
    calendario = Calendario()
    vista = None
    
#funcion __init__
    #Esta funcion asigna la interfaz inicializada al atributo vista, asi se puede llamar
    # los atributos de la interfaz y modificarlos
    
    def __init__(self,app):
        self.vista= app

#funcion esBiciesto
#Entradas: un anio
#Salidas: un string de si es o no biciesto o un mensaje de error
#Proceso: Hace validacion de datos con el validator y luego llama a la funcion de Calendario de bisiesto
    def esBiciesto(self,anio):
        if self.validator.es_numero(anio):
            anio = int(anio)
            if self.validator.es_dato_de_calendario(anio):
                resultado = self.calendario.bisiesto(anio)
                
                if resultado:
                    self.vista.lResultado.config(text="Si es bisiesto")
                else:
                    self.vista.lResultado.config(text="No es bisiesto")
            else:
                self.vista.lResultado.config(text= "Debe ingresar un anio mayor a 1582")
        else:
            self.vista.lResultado.config(text="Debe ingresar un numero entero")

#funcion verificarFecha
#Entradas: un anio,mes y dia
#Salidas: un string de si es o no una fecha valida o u mensaje de error
#Proceso: Hace validacion de datos con el validator y luego llama a la funcion de fecha_es_valida del Calendario

    def verificarFecha(self,anio,mes,dia):
        if not self.validator.es_numero(anio):
            self.vista.lResultado.config(text="Debe ingresar un anio entero")
        elif not self.validator.es_numero(mes):
            self.vista.lResultado.config(text="Debe ingresar un mes entero entre 1 y 12")
    
        elif not self.validator.es_numero(dia):
            self.vista.lResultado.config(text="Debe ingresar un dia entero entre 1 y 31")

        else:
            anio = int(anio)
            mes = int(mes)
            dia = int(dia)

            if not self.validator.es_dato_de_calendario(anio):
                self.vista.lResultado.config(text= "Debe ingresar un anio mayor a 1582")
            elif not self.validator.es_dato_de_calendario(mes):
                self.vista.lResultado.config(text="Debe ingresar un mes entero entre 1 y 12")
            elif not self.validator.es_dato_de_calendario(dia):
                self.vista.lResultado.config(text="Debe ingresar un dia entero entre 1 y 31")

            else:
            
                resultado = self.calendario.fecha_es_valida((anio,mes,dia))
                if resultado:
                    self.vista.lResultado.config(text="Fecha ingresada es valida")
                else:
                    self.vista.lResultado.config(text="Fecha ingresada no valida: \n" + self.calendario.mensajeError)

#funcion diaSiguiente
#Entradas: un anio,mes y dia
#Salidas: un string del dia siguiente a la fecha o un mensaje de error
#Proceso: Hace validacion de datos con el validator y luego llama a la funcion de Calendario de dia_siguiente
    def diaSiguiente(self,anio,mes,dia):
        if not self.validator.es_numero(anio):
            self.vista.lResultado.config(text="Debe ingresar un anio entero")
        elif not self.validator.es_numero(mes):
            self.vista.lResultado.config(text="Debe ingresar un mes entero entre 1 y 12")
    
        elif not self.validator.es_numero(dia):
            self.vista.lResultado.config(text="Debe ingresar un dia entero entre 1 y 31")

        else:
            anio = int(anio)
            mes = int(mes)
            dia = int(dia)

            if not self.validator.es_dato_de_calendario(anio):
                self.vista.lResultado.config(text= "Debe ingresar un anio mayor a 1582")
            elif not self.validator.es_dato_de_calendario(mes):
                self.vista.lResultado.config(text="Debe ingresar un mes entero entre 1 y 12")
            elif not self.validator.es_dato_de_calendario(dia):
                self.vista.lResultado.config(text="Debe ingresar un dia entero entre 1 y 31")

            else:
                resultado = self.calendario.dia_siguiente((anio,mes,dia))
                if len(resultado) == 0:
                    self.vista.lResultado.config(text=self.calendario.mensajeError)
                else:
                    self.vista.lResultado.config(text="Dia siguiente: " + str(resultado[2]) + " del mes " + str(resultado[1]) + " del " + str(resultado[0]))

#funcion diasDesdePrimeroEnero
#Entradas: un anio,mes y dia
#Salidas: un string con los dias desde el primero de enero de 2018 o un mensaje de error
#Proceso: Hace validacion de datos con el validator y luego llama a la funcion de Calendario de dias_desde_primero_enero
    def diasDesdePrimeroEnero(self,anio,mes,dia):
        if not self.validator.es_numero(anio):
            self.vista.lResultado.config(text="Debe ingresar un anio entero")
        elif not self.validator.es_numero(mes):
            self.vista.lResultado.config(text="Debe ingresar un mes entero entre 1 y 12")
    
        elif not self.validator.es_numero(dia):
            self.vista.lResultado.config(text="Debe ingresar un dia entero entre 1 y 31")

        else:
            anio = int(anio)
            mes = int(mes)
            dia = int(dia)

            if not self.validator.es_dato_de_calendario(anio):
                self.vista.lResultado.config(text= "Debe ingresar un anio mayor a 1582")
            elif not self.validator.es_dato_de_calendario(mes):
                self.vista.lResultado.config(text="Debe ingresar un mes entero entre 1 y 12")
            elif not self.validator.es_dato_de_calendario(dia):
                self.vista.lResultado.config(text="Debe ingresar un dia entero entre 1 y 31")

            else:
                resultado = self.calendario.dias_desde_primero_de_enero((anio,mes,dia))
                if resultado == None:
                    self.vista.lResultado.config(text=self.calendario.mensajeError)
                else:
                    self.vista.lResultado.config(text="Han pasado " + str(resultado) + " dias desde el 1ero de enero de ese anio")

    def diaPrimeroDeEnero(self,anio):
        if not self.validator.es_numero(anio):
            self.vista.lResultado.config(text="Debe ingresar un anio entero")
        else:
            anio = int(anio)
            if not self.validator.es_dato_de_calendario(anio):
                self.vista.lResultado.config(text= "Debe ingresar un anio mayor a 1582")
            else:
                resultado = self.calendario.dia_primero_enero(anio)
                dias = { 0:"Domingo",
                         1: "Lunes",
                         2: "Martes",
                         3: "Miercoles",
                         4: "Jueves",
                         5: "Viernes",
                         6: "Sabado" }
                self.vista.lResultado.config(text="Dia " + str(resultado)+ ":" + str(dias[resultado]))
            
            
#######################################################

#Clase CalendarApp
#Clase de GUI que interactua con clase CalendarController
class CalendarApp:

    def llamarBiciesto(self):
        anio = self.eAnio.get()
        self.controlador.esBiciesto(anio)

    def llamarValidarFecha(self):
        anio = self.eAnio.get()
        mes = self.eMes.get()
        dia = self.eDia.get()
        self.controlador.verificarFecha(anio,mes,dia)

    def llamarDiaSiguiente(self):
        anio = self.eAnio.get()
        mes = self.eMes.get()
        dia = self.eDia.get()
        self.controlador.diaSiguiente(anio,mes,dia)

    def llamarDiasEnero(self):
        anio = self.eAnio.get()
        mes = self.eMes.get()
        dia = self.eDia.get()
        self.controlador.diasDesdePrimeroEnero(anio,mes,dia)

    def llamarPrimeroDeEnero(self):
        anio = self.eAnio.get()
        mes = self.eMes.get()
        dia = self.eDia.get()
        self.controlador.diaPrimeroDeEnero(anio)
         
    def __init__(self,app):
       self.controlador = CalendarController(self)
       self.app = app
       app.geometry("400x600")

       self.controlador.vista = self
       self.anio = StringVar()
       self.mes = StringVar()
       dia = StringVar()

       self.lTitulo = Label(app,text="CalendarioTec",font=("Times New Roman",24))
       self.lTitulo.place(x=150,y=10)

       self.lOpcion = Label(app,text="Seleccione una opcion")
       self.lOpcion.place(x=150,y=50)

       self.bBiciesto = Button(app,text="Bisiesto",command=self.llamarBiciesto)
       self.bBiciesto.config(height=4, width=10)
       self.bBiciesto.place(x=30,y=90)

       self.bFechaValida = Button(app,text="Fecha valida",command=self.llamarValidarFecha)
       self.bFechaValida.config(height=4, width=10)
       self.bFechaValida.place(x=150,y=90)

       self.bDiaSiguiente = Button(app,text="Dia siguiente",command=self.llamarDiaSiguiente)
       self.bDiaSiguiente.config(height=4,width=10)
       self.bDiaSiguiente.place(x=280,y=90)

       self.bDiasEnero = Button(app,text="Dias desde\n 1ero de \nenero",command=self.llamarDiasEnero)
       self.bDiasEnero.config(height=4,width=10)
       self.bDiasEnero.place(x=30,y=200)

       self.bDiaPrimero = Button(app,text="Dia primero\n de\n enero",command=self.llamarPrimeroDeEnero)
       self.bDiaPrimero.config(height=3,width=10)
       self.bDiaPrimero.place(x=150,y=200)

       self.lAnio = Label(app,text="Anio").place(x=60,y=280)
       self.eAnio = Entry(app)
       self.eAnio.config(width=8)
       self.eAnio.place(x=30,y=300)

       self.lMes = Label(app,text="Mes").place(x=180,y=280)
       self.eMes = Entry(app)
       self.eMes.config(width=8)
       self.eMes.place(x=150,y=300)

       self.lDia = Label(app,text="Dia").place(x=300,y=280)
       self.eDia = Entry(app)
       self.eDia.config(width=8)
       self.eDia.place(x=280,y=300)

       self.lResultado = Label(app)
       self.lResultado.place(x=30,y=450)

    

root = tkinter.Tk()
myCalendar = CalendarApp(root)
root.mainloop()

        



    
