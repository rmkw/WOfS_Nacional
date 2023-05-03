import subprocess
import os
from datetime import datetime

current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print('Proceso iniciado en: '+current_time)

input_path=("C:\\WOfS\\vectores_binarios_wofs")
output_path="C:\\WOfS\\vectores_binarios_wofs_corregidos"

for root,dirs,files in os.walk(input_path):
    for f in files:
        if f.endswith(".shp"):
            # Preparación de directorios de entrada y salida
            input_shp = os.path.join(root, f)
            nombre = f.replace('.shp', '')
            output_shp = os.path.join(output_path, nombre + '_Corregido.shp')
            cmd = ['qgis_process', 'run', 'native:fixgeometries',
                   '--distance_units=meters', '--area_units=m2',
                   '--ellipsoid=USER:100000',
                   '--INPUT='+input_shp+'',
                   '--OUTPUT='+output_shp+'']
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(result.stdout)



final_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print('Proceso finalizado en: '+final_time)


processing.run("native:fixgeometries", {'INPUT':'C:/WOfS/vectores_bin_wofs_recorte/mascara_binaria_binario_Corregido_cortado.shp','OUTPUT':'TEMPORARY_OUTPUT'})
