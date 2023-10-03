
informacion_personal = {
    'nombre': 'George Altamirano',
    'edad': 34,
    'ciudad': 'Quito',
    'profesion': 'Arquitecto'
}

# Acceder al valor asociado con la clave 'ciudad' y modificarlo
informacion_personal['ciudad'] = 'Guayaquil'


# Verificar si la clave 'telefono' existe, sino agregarla
if "telefono" not in informacion_personal:
    informacion_personal['telefono'] = '06-2332-009'

# Eliminar la clave 'edad' del diccionario
if 'edad' in informacion_personal:
    del informacion_personal['edad']

# Imprimir el diccionario resultante
print('Nombre:', informacion_personal['nombre'])
print('Ciudad:', informacion_personal['ciudad'])
print('Profesión:', informacion_personal['profesion'])
print('Teléfono:', informacion_personal['telefono'])
