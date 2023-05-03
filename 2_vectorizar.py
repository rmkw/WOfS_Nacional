import os
from datetime import datetime

current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print('Proceso iniciado en: '+current_time)

home = ("D:\\WOfS\\2021\\WOfS\\Rasters_Binarios")
output_path = "D:\\WOfS\\2021\\WOfS\\Shapes"

for root, dirs, files in os.walk(home):
    for f in files:
        if f.endswith(".tif") and root == home:
            # Preparación de directorios de entrada y salida
            raster_path = os.path.join(root, f)
            nombre = f.replace('.tif', '')
            shape_path = os.path.join(output_path, nombre + '.shp')

            # Verificar si el archivo binario ya existe
            #if not os.path.exists(raster_binario_path):
            cmdstring = 'gdal_polygonize.bat ' + raster_path + ' -b 1 -f "ESRI Shapefile" ' + shape_path + ' ' + nombre + ' wofs'
            os.system(cmdstring)

final_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print('Proceso finalizado en: '+final_time)