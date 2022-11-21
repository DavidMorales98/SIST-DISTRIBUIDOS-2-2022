# Funciones necesarias para el correcto funcionamiento del código

def continents():
    asia = ["Afganistan", "Armenia", "Emiratos Arabes Unidos", "Indonesia","Iraq","Japon","Malasia","Mongolia","Nepal","Pakistan","Qatar","Yemen","Arabia Saudita","Filipinas","India","Iran","Israel","Jordania","Kuwait","Libano","Maldivas","Palestina","Singapur","Siria","Tailandia","Vietnam"]
    africa = [
    "Africa del sur",
    "Argelia",
    "Cabo Verde",
    "Costa de Marfil",
    "Ghana",
    "Guinea Ecuatorial",
    "Kenia",
    "Libia",
    "Madagascar",
    "Marruecos",
    "Nigeria",
    "Somalia",
    "Tanzania",
    "Tunez",
    "Angola",
    "Camerún",
    "Congo",
    "Egipto",
    "Etiopia",
    "Mali",
    "Senegal",
    "Sudan",
    "Uganda",
    "Zimbabwe"
    ] 
    europa = [
    "Andorra",
    "Belgica",
    "Croacia",
    "España",
    "Holanda",
    "Italia",
    "Monaco",
    "Polinia",
    "Rumania",
    "Suecia",
    "Ucrania",
    "Alemania",
    "Austria",
    "Bulgaria",
    "Dinamarca",
    "Eslovenia",
    "Estonia",
    "Francia",
    "Grecia",
    "Irlanda",
    "Lituania",
    "Macedonia",
    "Noruega",
    "Portugal",
    "Rusia",
    "Suiza"
    ]
    america = [
    "Barbados",
    "Costa Rica",
    "Jamaica",
    "Mexico",
    "Canada",
    "Cuba",
    "Estados Unidos",
    "Panama",
    "Argentina",
    "Brasil",
    "Colombia",
    "Venezuela",
    "Bolivia",
    "Chile",
    "Ecuador",
    "Peru",
    "Uruguay"
    ]
    oceania = [
    "Australia",
    "Nueva Zelanda"
    ]
    continentes =[america,europa,asia,africa,oceania]
    return continentes
def apiKey():
    key = 'cbcbcb213521febd7571bfd57b978cb2'
    return key
def where(pais, continentes):
    if (pais in continentes[0]):
        return 'america'
    elif (pais in continentes[1]):
        return 'europa'
    elif (pais in continentes[2]):
        return 'asia'
    elif (pais in continentes[3]):
        return 'africa'
    elif (pais in continentes[4]):
        return 'oceania'
    return False

