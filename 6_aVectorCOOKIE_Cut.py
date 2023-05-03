import subprocess
import os
from datetime import datetime

current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print('Proceso iniciado en: '+current_time)

cookie="C:\\WOfS\\COOKIE\\Mex_Wofs_p.shp"
input_path=("C:\\WOfS\\vectores_binarios_wofs_corregidos")
output_path="C:\\WOfS\\vectores_bin_wofs_recorte"

for root,dirs,files in os.walk(input_path):
    for f in files:
        if f.endswith(".shp"):
            # Preparación de directorios de entrada y salida
            input_shp = os.path.join(root, f)
            nombre = f.replace('.shp', '')
            output_shp = os.path.join(output_path, nombre + '_cortado.shp')
            cmd = ['qgis_process', 'run', 'native:clip',
                   '--distance_units=meters', '--area_units=m2',
                   '--ellipsoid=USER:100000',
                   '--INPUT='+input_shp+'',
                   '--OVERLAY='+cookie+'',
                   '--OUTPUT='+output_shp+'']
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(result.stdout)

final_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print('Proceso finalizado en: '+final_time)






