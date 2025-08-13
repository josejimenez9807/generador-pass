import secrets
import string

def generar_contraseña(longitud, usar_mayus, usar_minus, usar_num, usar_simbolos):
    conjunto = ''
    if usar_mayus:
        conjunto += string.ascii_uppercase
    if usar_minus:
        conjunto += string.ascii_lowercase
    if usar_num:
        conjunto += string.digits
    if usar_simbolos:
        conjunto += string.punctuation

    if not conjunto:
        print("⚠️ Error: Debes seleccionar al menos un tipo de carácter.")
        return None

    return ''.join(secrets.choice(conjunto) for _ in range(longitud))

def main():
    print("🔐 Generador de Contraseñas Seguras\n")

    try:
        longitud = int(input("📏 Longitud de la contraseña: "))
        if longitud <= 0:
            print("⚠️ La longitud debe ser mayor que cero.")
            return
    except ValueError:
        print("⚠️ Error: La longitud debe ser un número entero.")
        return

    usar_mayus = input("¿Incluir mayúsculas? (s/n): ").strip().lower() == 's'
    usar_minus = input("¿Incluir minúsculas? (s/n): ").strip().lower() == 's'
    usar_num = input("¿Incluir números? (s/n): ").strip().lower() == 's'
    usar_simbolos = input("¿Incluir símbolos? (s/n): ").strip().lower() == 's'

    contraseña = generar_contraseña(longitud, usar_mayus, usar_minus, usar_num, usar_simbolos)

    if contraseña:
        print("\n✅ Contraseña generada:")
        print(contraseña)

if __name__ == "__main__":
    main()