phone_book = {}
contacts = []

def show_contacts(phone_book):
    show_contacts = list(phone_book)
    return show_contacts

def add_contact(phone_book):
    if name in contact:
        print('Error. El nombre ya existe')
    else:
        phone_book = {
        'nombre': name,
        'teléfono': phone
        }
        contacts.append(phone_book)

def remove_contact(phone_book):
    if name in phone_book:
        del(phone_book[name])
    else:
        print('Error. El nombre no existe')

def menu():
    print('Opciones: ')
    print('1. Mostrar lista de contactos')
    print('2. Añadir contacto (nombre y teléfono)')
    print('3. Borrar contacto (nombre)')
    print('4. Salir')

while True:
    menu()

    optionmenu = int(input('Introduce una opción: '))

    if optionmenu == 1:
        print(show_contacts(phone_book))

    elif optionmenu == 2:
        while  True:
            name = str(input('Introduzca el nombre: '))
            if name in phone_book:
                print('Error. El nombre ya existe')
            phone = int(input('Introduzca el número: '))
            exit = input('¿Quiere salir? [s|n]: ' )
            add_contact(phone_book)

            if exit == 's':
                break

    elif optionmenu == 3:
        while  True:
            name = str(input('Introduzca el nombre: '))
            if not name in phone_book:
                print('Error. El nombre no existe')

            exit = input('¿Quiere salir? [s|n]: ' )
            if exit == 's':
                break

                remove_contact(phone_book)

    elif optionmenu == 4:
        break
