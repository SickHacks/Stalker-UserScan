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

    if sistema_cliente == 'Windows' or 'Linux' or "AIX" or "FreeBSD":
        return sistema_cliente
    elif sistema_cliente == 'Darwin':
        return 'MacOS'
    elif sistema_cliente == 'Java':
        return 'Java Virtual Machine (JVM).'
    elif sistema_cliente == 'SunOS':
        return 'SunOS: También conocido como Solaris.'
    else:
        return 'No se reconoce el sistema operativo'
    

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
        print("\n")
        print("""
              
███████╗████████╗ █████╗ ██╗     ██╗  ██╗███████╗██████╗ 
██╔════╝╚══██╔══╝██╔══██╗██║     ██║ ██╔╝██╔════╝██╔══██╗
███████╗   ██║   ███████║██║     █████╔╝ █████╗  ██████╔╝
╚════██║   ██║   ██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████║   ██║   ██║  ██║███████╗██║  ██╗███████╗██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
         Herramienta de escaneo a usuarios""")

        print("---------------------------------------------------------")
        print("Seleccione una opcion")
        print("[1] Escanear")
        print("[0] Salir")
        opcion = input("-> ")

        if opcion == '1':
            print("--------------------- RESULTADOS ------------------------")
            print(f"[+] IP: {ip_cliente}")
            print(f"[+] Dispositivo: {nombre_fabricante}")
            print(f"[+] Sistema operativo: {os_cliente}")
            print("---------------------------------------------------------")
            print("Seleccione una opcion")
            print("[1] Volver al menu")
            print("[2] Mas detalles")
            print("[0] Salir")
            volver = input("-> ")
            if volver == '1':
                print("[+] Volviendo al menu principal")

            elif volver == '2':
                print("-------------------- MAS DETALLES -----------------------")
                print(f"[+] MAC (Media Access Control): {mac_cliente}")
                print("")
                print("Seleccione una opcion")
                print("[1] Volver al menu")
                print("[0] Salir")
                volver = input("-> ")
                if volver == '1':
                    print("[+] Volviendo al menu principal")
                elif volver == '0':
                    print ("[+] Saliendo del programa")
                    break
            elif volver == '0':
                print("[+] Saliendo del programa")
                break
            else:
                print("Opcion invalida, intente nuevamente")
        elif opcion == '0':
            print("[+] Saliendo del programa")
            break
        else:
            print("Opcion invalida, intente nuevamente")

menu()
