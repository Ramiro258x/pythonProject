from pathlib import Path
#path = Path('test-carpeta')
#path.rename('nuevo_test')

# Renombrar archivo
#path = Path('nuevo_test/gastos.txt')
#nuevo_nombre_path = path.with_name('gastos-enero.txt')
#print(nuevo_nombre_path)
#path.rename(nuevo_nombre_path)


# Obtenr path de los subdirectorios inmediatos
carpeta = Path('2024')
for path in list(carpeta.iterdir())
    print(path)