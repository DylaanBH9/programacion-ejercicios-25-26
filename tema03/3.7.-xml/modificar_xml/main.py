import xml.etree.ElementTree as ET

def data_input():
    country = input("Introduzca el nombre del pais: ")
    year = input("Introduzca el año del pais: ")
    rank = input("Introduzca el rango del pais: ")
    gdppc = input("Introduzca el gdppc del pais: ")

    neighbor_list = []
    neighbor = ""
    continuar = ""
    while continuar.lower() != "x":
        neighbor = input("Introduzca un vecino del pais: ")
        neighbor_direction = input("Introduzca la direccion del pai vecino: ")
        neighbor_list.append([neighbor, neighbor_direction])
        continuar = input("'x' para terminar o pulse intro para introducir otro pais vecino")

    diccionario_datos = {country: {"rank": rank, "year": year, "PIB": gdppc, "Neighbors": neighbor_list}}
    return (diccionario_datos)


def data_addition(country_info, arbol, raiz):
    for pais in country_info:
        nuevo_pais = ET.SubElement(raiz, "country")
        nuevo_pais.set("name", pais)
        ET.SubElement(nuevo_pais, "rank").text = country_info[pais]["rank"]
        ET.SubElement(nuevo_pais, "year").text = country_info[pais]["year"]
        ET.SubElement(nuevo_pais, "gdppc").text = country_info[pais]["PIB"]

    ET.indent(arbol, space="    ", level=0)
    arbol.write("country_data_new.xml")

def data_display(raiz):
    paises = raiz.findall("country")

    lista_paises_rangos = []
    for pais in paises:
        pais_str = pais.get("name")
        rango = pais.find("rank").text
        lista_paises_rangos.append([pais_str, rango])

    lista_paises_rangos_ordenada = sorted(lista_paises_rangos, key=lambda x: x[1])

    for pais, rango in lista_paises_rangos_ordenada:
        print(f"-{rango}: {pais}")



def main():
    arbol = ET.parse("country_data.xml")
    raiz = arbol.getroot()
    country_info = data_input()
    data_addition(country_info, arbol, raiz)
    data_display(raiz)

if __name__ == '__main__':
    main()
