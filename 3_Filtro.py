import os
from datetime import datetime
from osgeo import ogr

current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print('Proceso iniciado en: '+current_time)

output_path = "D:\\WOfS\\2021\\WOfS\\Shapes"

for root, dirs, files in os.walk(output_path):
    for f in files:
        if f.endswith(".shp"):
            # Preparación de directorios de entrada y salida
            shape_path = os.path.join(root, f)

            # Eliminación de vectores con valor de wofs <50%
            print('Abriendo shapefile para borrar registros...')
            dataset = ogr.Open(shape_path, True)
            layer = dataset.GetLayer(0)
            print('Cantidad de registros antes de eliminación: {}'.format(layer.GetFeatureCount()))
            for i in range(layer.GetFeatureCount()):
                row = layer.GetFeature(i)
                wofs_val = row.GetField(row.GetFieldIndex('wofs'))
                if wofs_val == 0:
                    layer.DeleteFeature(i)
            dataset.ExecuteSQL('REPACK ' + layer.GetName())
            dataset.ExecuteSQL('RECOMPUTE EXTENT ON ' + layer.GetName())
            print('Cantidad de registros después de eliminación: {}'.format(layer.GetFeatureCount()))
            print('Eliminando objetos...')
            dataset = None
            layer = None
            row = None
            print('OK!')

final_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print('Proceso finalizado en: '+final_time)