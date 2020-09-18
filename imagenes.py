import quandl
import pandas as aapl
import time
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = 'XXXXXXXXXXXXX' 


fecha_inicio="2000-01-01"
fecha_final="2017-04-11"


grupo1=["MSFT","GOOGL","AMZN","TSLA","BA","GM","BAC","F","WFC","AMD","DAL","UAL","CCL","AAPL","T","MGM","JPM","C","MU","VAC","NBL","LEG","EA","AAL","AAP","ABBV","ABC","ABBV","ACN","ADBE","ADI","ADM","ADP","ADS","ADSK","AEE","AEP","AES","AET","AEL","AGN","AIG","AIV","AIZ","AJG"]
grupo2= ["AAL","AAP","ABBV","ABC","ABBV","ACN","ADBE","ADI","ADM","ADP","ADS","ADSK","AEE","AEP","AES","AET","AEL","AGN","AIG","AIV","AIZ","AJG"]
grupo3= ["AKAM","ALB","ALGN","ALK","ALL","ALLE","ALXN","AMAT","AME","AMG","AMGN","AMP","AMT","ANDV","ANSS","ANTM","AON","AOS","APA","APC","APD","APH"]
grupo4= ["APTV","ARE","ATVI","AVB","AVGO","AVY","AWK","AXP","AZO","BAC","BAX","BBT","BBY","BBX","BEN","BHF","BHGE","BIIB","BK","BLK","BLL"]


valores=grupo1

for x in range(0,len(valores)):
    
    valor= "WIKI/" + valores[x]
    print ('Generando imagenes de: ' + (valor))
    aapl = quandl.get(valor, start_date=fecha_inicio, end_date=fecha_final)
    time.sleep(.100)
    
    #Calculando parametros para cada imagenes.
    
    ventana_imagen=200 # en la inicializacion final_imagen
    ventana_rentabilidad=50
    ventana_siguiente=1
    tamanyo_tratar=len(aapl.index)
    inicio_imagen=ventana_imagen
    condicion_terminar=200
    final_rentabilidad=ventana_imagen
    final_tratamiento=(tamanyo_tratar-ventana_rentabilidad-ventana_imagen)

    while (condicion_terminar < final_tratamiento):

    
        #Es la clase por defecto.
        clase=100    
        split=aapl.iloc[inicio_imagen,6]           
      
        final_imagen=inicio_imagen+ventana_imagen
        final_rentabilidad=final_imagen+ventana_rentabilidad  
        
        df_tratar=aapl.iloc[inicio_imagen:final_imagen]
       
        valor_inicial=aapl.iloc[inicio_imagen,3]
        valor_final=aapl.iloc[final_rentabilidad,3] 
        
        rentabilidad=(valor_final-valor_inicial)/valor_inicial

        clase=0

        if ((rentabilidad>=0)):

                clase=1


        #Calculo nombre imagen
        rentabilidad=round(rentabilidad, 4)
        nombre_imagen=str(clase) + '/' + str(clase) + '-' + str(inicio_imagen) + '-' + str(final_imagen) + '-' + str(rentabilidad)+ '.jpg' 
        print(nombre_imagen) 
        
        #Generación de la imagen
        #Calculo las medias moviles       

        media200 = aapl['Close'].rolling(window=200).mean()
        media100 = aapl['Close'].rolling(window=100).mean()
        #media50 = aapl['Close'].rolling(window=50).mean()
        media25 = aapl['Close'].rolling(window=25).mean()        
        #media10 = aapl['Close'].rolling(window=10).mean()
        media3 = aapl['Close'].rolling(window=3).mean()
      
        #Tamaño de la imagen
        plt.figure(figsize=(0.6,0.3))

        ax = plt.axes([0,0,1,1], frameon=False)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        plt.plot(df_tratar['Close'],'b')
        plt.plot(media200.iloc[inicio_imagen:final_imagen],'c')
        plt.plot(media100.iloc[inicio_imagen:final_imagen],'m')
        #plt.plot(media50.iloc[inicio_imagen:final_imagen],'y')
        plt.plot(media25.iloc[inicio_imagen:final_imagen],'g')    
        #plt.plot(media10.iloc[inicio_imagen:final_imagen],'g')
        plt.plot(media3.iloc[inicio_imagen:final_imagen],'g')

        #Grabamos a disco la imagen
        plt.autoscale(tight=True)
        plt.axis('off')
        plt.savefig(nombre_imagen)
                
        #Condiciones de final          
        inicio_imagen=inicio_imagen+ventana_siguiente
        condicion_terminar=condicion_terminar+1
        print (valor + ' Imagenes a tratatadas: ' + str(condicion_terminar))
        print ('Final rentabilidad + Final tratamiento: ' + str(final_rentabilidad) + '-'  + str(final_tratamiento))    
      
        plt.close("all")
        #Tiempo de espera entre generación de graficas para no saturar el sistema.
        time.sleep(0.01)
