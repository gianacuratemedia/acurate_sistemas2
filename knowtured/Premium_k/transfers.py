import requests
from requests_toolbelt.utils import dump 
import stripe
#Script para realizar los pagos de los profesores usuarios

r=requests.get("http://127.0.0.1:8000/premium/consultar_saldo/")

# Extrayendo datos en formato json 
data = r.json() 
saldo=data['available'][0]['amount']

#Calculando saldo a distribuir
pagos=saldo*0.8

#Calcular monto a pagar por vistas
p_vistas=pagos*0.6
#Monto a pagar por creación de contenido
p_contenido=pagos*0.4

#Obteniendo los ids de usuario 
r1=requests.get('http://127.0.0.1:8000/cursos/all-cursos/estadisticas/contenido/ids/')
data1=r1.json()
#Consultando el contenido total creado por todos los usuarios 
r2=requests.get('http://127.0.0.1:8000/cursos/all-cursos/estadisticas/contenido/total/')
data2=r2.json()
suma_contenido=data2['contenido_trimestral__sum']

#Obtener los ids de usuario para las vistas de los cursos 

r3=requests.get('http://127.0.0.1:8000/cursos/all-cursos/estadisticas/cursos/ids/')
data3=r3.json()

#Consultando el total de vistas por todos los cursos 
r4=requests.get('http://127.0.0.1:8000/cursos/all-cursos/estadisticas/cursos/total/')
data4=r4.json()
suma_vistas=data4['no_vistas_t__sum']

print("Saldo="+str(saldo),"Pagos="+str(pagos),"Pagos vistas="+str(p_vistas),"Pagos contenido="+str(p_contenido))

print ("suma contenido="+str(suma_contenido))
print ("suma vistas="+str(suma_vistas))

#Iterar ids

for id in data1['results']:
    user=id['owner_id']
    #Obtener cantidad total de contenido crado por el id usuario 
    r_t=requests.get('http://127.0.0.1:8000/cursos/all-cursos/estadisticas/contenido/total/'+str(user))
    data_t=r_t.json()
    contenido_user=data_t['contenido_trimestral']

    pago_user_contenido=(p_contenido/suma_contenido)*contenido_user
    print(user)
    print(data_t)
    print(pago_user_contenido)

    #Enlazar con cuenta en stripe y realizar la transferencia 
    #Consultar id de la cuenta de stripe del usuario que se almacenó al momento de registrarse el usuario 
    r_t1=requests.get('http://127.0.0.1:8000/premium/datos-cuenta-user/<int:user>'+str(user))
    data_t1=r_t1.json()
    cuenta_user=data_t1['acccount_Stripe']


    #Realizar la transferencia
    data_s = {'ammount':pago_user_contenido, 
            'destination':cuenta_user}
    r_t2=requests.post(url='http://127.0.0.1:8000/premium/transferencias/',data=data_s )
 


for id in data3['results']:
    user=id['owner']
    #Obtener cantidad total de vistas trimestrales crado por el id usuario 
    r_t=requests.get('http://127.0.0.1:8000/cursos/all-cursos/estadisticas/curso/total/'+str(user))
    data_t=r_t.json()
    vistas_user=data_t['no_vistas_t__suma']

    pago_user_vistas=(p_vistas/suma_vistas)*vistas_user

    print(user)
    print(data_t)
    print(pago_user_vistas)

  #Enlazar con cuenta en stripe y realizar la transferencia 

    #Consultar id de la cuenta de stripe del usuario que se almacenó al momento de registrarse el usuario 
    r_t1=requests.get('http://127.0.0.1:8000/premium/datos-cuenta-user/<int:user>'+str(user))
    data_t1=r_t1.json()
    cuenta_user=data_t1['acccount_Stripe']


    #Realizar la transferencia
    data_s = {'ammount':pago_user_vistas, 
            'destination':cuenta_user}
    r_t2=requests.post(url='http://127.0.0.1:8000/premium/transferencias/',data=data_s )
