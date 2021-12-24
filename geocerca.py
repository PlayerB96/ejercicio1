import json
import xlsxwriter

def cargar_datos(ruta):
    with open(ruta) as contenido:
        cursos = json.load(contenido)
        
        return cursos

if __name__ == '__main__':
    dt2 = 'geofences.json'
    dt = 'groups.json'
    group = cargar_datos(dt)
    geofen = cargar_datos(dt2)
    # print(group)
    
    data=[]
    for key, values in group.items():
        # print(key)
        # print(values["n"])
        geofences=[]
        for item in values["zns"]:
            # print(geofen[str(item)]["n"])
            n = geofen[str(item)]["n"]
            d = geofen[str(item)]["d"]
            lat = geofen[str(item)]["b"]["cen_x"]
            lon = geofen[str(item)]["b"]["cen_y"]
            
            geofences.append({
                "nombre":n,
                "descripcion":d,
                "latitud": lat,
                "longitud": lon
            })
            # print(geocerca)
        data.append({
            "grupo": values["n"],
            "geocerca": geofences
        })
    planta=[]
    planta.append(data[1])
    # print(planta)

    workbook = xlsxwriter.Workbook('Venta de Saldos.xlsx')
    worksheet = workbook.add_worksheet()
    
    for row_num, row_data in enumerate(planta):
        print(row_data)
        # print(row_data["grupo"])
        worksheet.write(row_num,1, 'Grupo')
        worksheet.write(row_num,2, row_data["grupo"])
        for col_num, row_data in enumerate(row_data["geocerca"]):
            # nombre=row_data["nombre"]
            # print(col_num)
            worksheet.write(col_num, 4, row_data["nombre"])
            worksheet.write(col_num, 5, row_data["descripcion"])
            worksheet.write(col_num, 6, row_data["latitud"])
            worksheet.write(col_num, 7, row_data["longitud"])
            
    workbook.close()
    
    
    
    
    
    
    
    # print(data[0]["geocerca"][0])
        
    # for dato in data:

    #     print(data[0]["grupo"])
    #     print(data[0]["geocerca"][0]["nombre"])
    #     print(data[0]["geocerca"][0]["descripcion"])
    #     print(data[0]["geocerca"][0]["latitud"])
    #     print(data[0]["geocerca"][0]["longitud"])
        

    # for x in range(0, len(data[0]["geocerca"])):
        # for n, item in zip(enumerate(data[0]["geocerca"]), data[0]["geocerca"]):
        #     tabla = xlsxwriter.Workbook('prueba10.xlsx')
        #     print(n[0])
        #     var=n[0]
        #     print(type(var))
        #     print(item["nombre"])
        #     tbgeocerca = tabla.add_worksheet()
        #     # tbgeocerca.write(2,1,'GRUPO')
        #     # tbgeocerca.write(2,2, item["grupo"])
        #     tbgeocerca.write(var,1,'Nombre')
        #     tbgeocerca.write(var,2, item["nombre"])
        #     # tbgeocerca.write(4,1,'Descrip')
        #     # tbgeocerca.write(4,2, item["descripcion"])
        #     # tbgeocerca.write(5,1,'Lat')
        #     # tbgeocerca.write(5,2, str(item["latitud"]))
        #     # tbgeocerca.write(6,1,'Lon')
        #     # tbgeocerca.write(6,2, str(item["longitud"]))

        #     tabla.close()
