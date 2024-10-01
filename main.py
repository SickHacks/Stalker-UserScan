import socket
import uuid
import platform
 

# Obtención de la ip 
def obtener_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


# Obtención dirección MAC
def obtener_mac():
    # Obtener la dirección MAC completa como un entero de 48 bits
    mac_address = uuid.getnode()
    # Formatear la dirección MAC en formato hexadecimal separado por ':'
    mac_str = ':'.join(
        f'{(mac_address >> 8*i) & 0xff:02x}' for i in range(5, -1, -1)).upper()
    return mac_str


# Obtención OUI
def obtener_oui():
    # Obtener la dirección MAC completa como un entero
    mac_address = uuid.getnode()
    # Extraer los primeros 3 bytes (24 bits) para el OUI
    oui = (mac_address >> 24) & 0xffffff
    # Formatear el OUI en formato hexadecimal separado por '-'
    oui_str = '-'.join(f'{(oui >> 8*i) & 0xff:02x}' for i in range(2, -1, -1)).upper()
    return oui_str


# Cargar el diccionario de OUI
def cargar_diccionario_oui(archivo):
    lista_oui = {}
    with open(archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            if ' : ' in linea:
                partes = linea.split(' : ')
                oui = partes[0].strip("' ")
                nombre = partes[1].strip("' \n")
                lista_oui[oui] = nombre
    return lista_oui


# Determinar OS 
def obtener_os():
    sistema_cliente = platform.system()

    match sistema_cliente:
        case 'Windows' | 'Linux' | 'AIX' | 'FreeBSD':
            resultado = sistema_cliente
        case 'Darwin':
            resultado = 'MacOS'
        case 'Java':
            resultado = 'Java Virtual Machine (JVM).'
        case 'SunOS':
            resultado = 'SunOS: También conocido como Solaris.'
        case _:
            resultado = 'No se reconoce el sistema operativo'
    return resultado


archivo_oui = 'Stalker-UserScan/oui_list.txt'
lista_oui = cargar_diccionario_oui(archivo_oui)
ip_cliente = obtener_ip()
oui_cliente = obtener_oui()
os_cliente = obtener_os()
mac_cliente = obtener_mac()
nombre_fabricante = lista_oui.get(oui_cliente, 'Desconocido')

# Menú principal
def menu():
    while True:
        print("""\n
              
███████╗████████╗ █████╗ ██╗     ██╗  ██╗███████╗██████╗ 
██╔════╝╚══██╔══╝██╔══██╗██║     ██║ ██╔╝██╔════╝██╔══██╗
███████╗   ██║   ███████║██║     █████╔╝ █████╗  ██████╔╝
╚════██║   ██║   ██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████║   ██║   ██║  ██║███████╗██║  ██╗███████╗██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
         Herramienta de escaneo a usuarios""")

        opcion = input(
            "---------------------------------------------------------\nSeleccione una opcion\n[1] Escanear\n[0] Salir\n-> ")

        match opcion:
            case '1':
                print(f"--------------------- RESULTADOS ------------------------"
                    f"\n[+] IP: {ip_cliente}\n[+] Dispositivo: {nombre_fabricante}\n[+] Sistema operativo: {os_cliente}\n[+] MAC (Media Access Control): {mac_cliente}\n---------------------------------------------------------"
                    f"\nSeleccione una opcion\n[1] Volver al menu\n[0] Salir")
                volver = input("-> ")
                match volver:
                    case '1':
                        print("[+] Volviendo al menu principal")

                    case '0':
                        print("[+] Saliendo del programa")
                        break
                    case _:
                        print("Opcion invalida, intente nuevamente")
            case '0':
                print("[+] Saliendo del programa")
                break
            case _:
                print("Opcion invalida, intente nuevamente")

menu()
