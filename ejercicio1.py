import json
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime

def cargar_datos(ruta):
    with open(ruta) as contenido:
        cursos = json.load(contenido)
        
        return cursos

if __name__ == '__main__':
            dt3 = 'años.json'
            dt2 = 'fechas.json'
            dt = 'fechacte.json'
            fechascte = cargar_datos(dt)
            fechas = cargar_datos(dt2)
            # y = cargar_datos(dt3)

            # print(fechascte["fechacte"])

            # data=[]
           
            # item1="30-11-2020";
            # item2="31-12-2021";
            x=[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021];
            y=[];
            for item1 in fechas["fechas"]:
                a=0;
                b=0;
                sumap=0;
                sumadmacn=0;
                
                for item2 in fechascte["fechacte"]:
                        data1=datetime.strptime(item1, "%d-%m-%Y")
                        data2=datetime.strptime(item2, "%d-%m-%Y")
                        diferencia = data2-data1
                        dias=diferencia.days
                        # print(dias)
                        dt=dias/365.3
                        dtaños=round(dt, 2)
                        # print(dtaños)

                        
                        if(item2=="31-12-2021"):
                            b=1045;
                            sm=a+b;

                        if(item2 != "31-12-2021"):

                            b=45;
                            sm=a+b;

                        # print(sm)

                        if(dtaños>=0):
                            denominador=(1.055)**dtaños
                            numerador=sm
                            valor=numerador/denominador
                            valoractual=round(valor, 3)
                            pvv=dtaños*valoractual
                            pvt=round(pvv, 3)
                            # print(pvt)
                            # print(type(valoractual))
                            
                        if(dtaños<0): 
                            # valor=0;
                            pvt=0.0;
                            valoractual=0;
                            
                            # print(pvt)
                        
                        sumap=sumap+valoractual;
                        preciosucio=round(sumap, 3);
                sumadmacn=round(((sumadmacn+pvt)/preciosucio),3);
                        
                # print(preciosucio)
                # print(sumadmacn)
                y.append(preciosucio)
            print(x)
            print(y)
            # plt.plot(x,y)
            # plt.show()



# navidad = datetime.strptime("2021-12-25", "%Y-%m-%d")
# fin_anio = datetime.strptime("2021-12-31", "%Y-%m-%d")
# diferencia = fin_anio-navidad

# print(f"La diferencia es de {diferencia.days} días y {diferencia.seconds} segundos. La diferencia total es de {diferencia.total_seconds()} segundos")