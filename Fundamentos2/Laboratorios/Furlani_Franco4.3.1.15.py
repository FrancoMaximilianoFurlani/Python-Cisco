def contar_letras(file_name):
    frecuencia_letras = {}
    with open(file_name, 'r') as file:
        for line in file:
            line = line.lower()
            for char in line:
                if char.isalpha():
                    frecuencia_letras[char] = frecuencia_letras.get(
                        char, 0) + 1

    return frecuencia_letras


def imprimir_histograma(frecuencia_letras):
    for letra in sorted(frecuencia_letras):
        count = frecuencia_letras[letra]
        print(f"{letra} -> {count}")


# Pedir al usuario el nombre del archivo de entrada
nombre_archivo = input("Ingrese el nombre del archivo de entrada: ")

# Contar las letras en el archivo
frecuencia = contar_letras(nombre_archivo)

# Imprimir el histograma
imprimir_histograma(frecuencia)
