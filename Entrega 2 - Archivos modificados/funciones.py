# Funciones necesarias para el correcto funcionamiento del código

def continents():
    asia = ["Afganistan", "Armenia", "United Arab Emirates", "Indonesia","Iraq","Japon","Malasia","Mongolia","Nepal","Pakistan","Qatar","Yemen","Arabia Saudita","Filipinas","India","Iran","Israel","Jordania","Kuwait","Libano","Maldivas","Palestina","Singapur","Siria","Tailandia","Vietnam"]
    africa = [
    "Sudafrica",
    "Algeria",
    "Cabo Verde",
    "Ivory Coast",
    "Ghana",
    "Guinea Ecuatorial",
    "Kenia",
    "Libia",
    "Madagascar",
    "Morocco",
    "Nigeria",
    "Somalia",
    "Tanzania",
    "Tunisia",
    "Angola",
    "Camerún",
    "Congo",
    "Egipto",
    "Etiopia",
    "Republic of Mali",
    "Senegal",
    "Sudan",
    "Uganda",
    "Zimbabwe"
    ] 
    europa = [
    "Andorra",
    "Croacia",
    "Spain",
    "Netherlands",
    "Italia",
    "Monaco",
    "Polonia",
    "Romania",
    "Suecia",
    "Ukraine",
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
    "Noruega",
    "Portugal",
    "Rusia",
    "Switzerland"
    ]
    america = [
    "Barbados",
    "Costa Rica",
    "Mexico City",
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
    "Republic of Peru",
    "Uruguay"
    ]
    oceania = [
    "Australia",
    "New Zealand"
    ]
    continentes =[america,europa,asia,africa,oceania]
    return continentes



def continentsData():
    asia = ["Afghanistan",
    "Armenia",
    "United Arab Emirates",
    "Indonesia",
    "Iraq",
    "Japan",
    "Malaysia",
    "Mongolia",
    "Nepal",
    "Pakistan",
    "Qatar",
    "Yemen",
    "Saudi Arabia",
    "Philippines",
    "Innichen",
    "Iran",
    "Israel",
    "Hashemite Kingdom of Jordan",
    "Kuwait City",
    "Líbano",
    "Maldives",
    "Palestine",
    "Singapore",
    "Syria",
    "Thailand",
    "Vietnam"]

    africa =["Republic of South Africa",
    "Algeria",
    "Republic of Cabo Verde",
    "Ivory Coast",
    "Ghana",
    "Equatorial Guinea",
    "Kenya",
    "Libya",
    "Madagascar",
    "Morocco",
    "Nigeria",
    "Somalia",
    "Tanzania",
    "Tunisia",
    "Angola",
    "Cameroon",
    "Republic of the Congo",
    "Egypt",
    "Ethiopia",
    "Mali",
    "Senegal",
    "Sudan",
    "Uganda",
    "Zimbabwe"]

    europa = [
    "Andorra",
    "Croatia",
    "Spain",
    "Netherlands",
    "Italy",
    "Monaco",
    "Polonia",
    "Romania",
    "Sweden",
    "Ukraine",
    "Germany",
    "Austria",
    "Bulgaria",
    "Denmark",
    "Slovenia",
    "Estonia",
    "Francia",
    "Greece",
    "Ireland",
    "Republic of Lithuania",
    "Norway",
    "Portugal",
    "Russia",
    "Switzerland"
    ]
    america = [
    "Barbados",
    "Costa Rica",
    "Mexico City",
    "Cuba",
    "United States of America",
    "Panama",
    "Argentina",
    "Brazil",
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
    "New Zealand"
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

