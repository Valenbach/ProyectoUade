def calcularVolFinalPasajes(VCDi,VCDtarget,volInicial,cantPasajes):
    #Generar una lista en la que se almacene el volumen final de cada pasaje.
    
    listavolFinalPasajes=[]
  
    
    for i in range(cantPasajes):
    
        volFinalPasaje=(VCDi*volInicial)/VCDtarget
        listavolFinalPasajes.append(volFinalPasaje)
        volInicial=volFinalPasaje
        
    return listavolFinalPasajes



def calcularMedioExp(listavolFinalPasajes):
    volMedioExp=sum(listavolFinalPasajes)
    return volMedioExp


VCDi=float(input("Ingrese el valor de VCD con la que desea iniciar cada pasaje: "))
VCDtarget=float(input("Ingrese el valor de VCD target a la que desea llevar el pasaje: "))
cantPasajes=int(input("Ingrese la cantidad de pasajes que desea efectuar durante la etapa de expansión, teniendo en cuenta que cada pasaje durará 3 días: "))
volInicial=int(input("Ingrese el volumen inicial del primer pasaje, en ml: "))   
    
ListavolFinalPasajes=calcularVolFinalPasajes(VCDi,VCDtarget,volInicial,cantPasajes)
print("Los volumenes finales de los pasajes a realizar son los siguientes: ", ListavolFinalPasajes)
VolFinalPasajes=calcularMedioExp(ListavolFinalPasajes)
print("El volumen final de medio de expansión necesario para el proceso es: ", VolFinalPasajes)
