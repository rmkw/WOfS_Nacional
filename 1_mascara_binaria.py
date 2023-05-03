import os
from datetime import datetime

current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print('Proceso iniciado en: '+current_time)

home=("D:\\WOfS\\2021\\WOfS\\wofs_2021")
output_path = "D:\\WOfS\\2021\\WOfS\\wofs_2021\\raster_binarios"

for root,dirs,files in os.walk(home):
    for f in files:
        if f.endswith(".tif") and root == home:
            # Preparación de directorios de entrada y salida
            raster_path = os.path.join(root, f)
            nombre = f.replace('.tif', '')
            raster_binario_path = os.path.join(output_path, nombre + '_binario.tif')

            # Verificar si el archivo binario ya existe
            #if not os.path.exists(raster_binario_path):

            cmdstring = 'gdal_calc --calc "A >=50" --format GTiff --type Int32 -A ' + raster_path + ' --A_band 1 --outfile ' + raster_binario_path
            os.system(cmdstring)

final_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print('Proceso finalizado en: '+final_time)