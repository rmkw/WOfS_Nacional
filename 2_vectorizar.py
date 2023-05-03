import os
from datetime import datetime

from qgis import processing

from osgeo import ogr
from osgeo import gdal

current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print('Proceso iniciado en: '+current_time)
#origen
home=("C:\\WOfS")
#salida
output_path = "C:\\WOfS\\vectores"

for root,dirs,files in os.walk(home):
    for f in files:
        if f.endswith(".tif"):
            # Preparación de directorios de entrada y salida
            raster_path = os.path.join(root, f)
            nombre = f.replace('.tif', '')
            shape_path = os.path.join(output_path, nombre + '_.shp')
            cmdstring = 'gdal_polygonize.bat ' + raster_path + ' -b 1 -f "ESRI Shapefile" ' + shape_path + ' ' + nombre + ' wofs'
            os.system(cmdstring)

final_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
print('Proceso finalizado en: '+final_time)

processing.run("native:fixgeometries", {'INPUT':'C:\\Users\\\Edificaciones.shp','METHOD':1,'OUTPUT':'C:/Users//lol.shp'})

#qgis_process run native:fixgeometries --distance_units=meters --area_units=m2 --ellipsoid=EPSG:7019 --INPUT='C:/Users/LUIS.CASTANEDAL/Documents/CURSOS/CURSO BÁSICO DE QGIS ABRIL 3 A 30 DE ABRIL/Ejercicio_3/Edificaciones.shp' --METHOD=1 --OUTPUT='C:/Users/LUIS.CASTANEDAL/Documents/CURSOS/lol.shp'


from osgeo import ogr
from osgeo import gdal
# Open the input dataset inDS = gdal.OpenEx('input.tif') # Get the input layer inLayer = inDS.GetLayer() # Create a new output layer outLayer = inLayer.Clone() # Apply the correction outLayer.ForceToMultiPolygon() # Save the corrected layer driver = ogr.GetDriverByName('ESRI Shapefile') outDS = driver.CreateDataSource('output.shp') outDS.CopyLayer(outLayer, 'output')