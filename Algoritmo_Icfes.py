def lectura():
    file = open("C:/Users/User/Documents/MINTIC_2022/PROYECTOS_T/BASE_ICFES/2021-1.txt","r", encoding="utf8")
    line= file.readline()
    header=[]
    matriz_data=[]
    header_process= line.rstrip('\n').split('¬')   
    for icon in header_process:
        if icon =='FAMI_ESTRATOVIVIENDA' or icon=='ESTU_GENERO':
            header.append(icon)
        elif icon=='ESTU_DEPTO_RESIDE' or  icon =='ESTU_MCPIO_RESIDE' or icon=='COLE_NATURALEZA':
            header.append(icon)
        elif icon=='PUNT_GLOBAL' or  icon=='DESEMP_INGLES':
            header.append(icon) 
    header.sort()
    line= file.readline()
    while line: 
        panel=[]
        data_process=line.rstrip('\n').split('¬')
        for d in range(len(data_process)): 
            if data_process[d]=='':
                data_process[d]='NO_DATA'
        for i in header:
            possion=header_process.index(i)
            panel.append(data_process[possion])
        matriz_data.append(panel)     
        line= file.readline()   
        if not line:
            break
    return header,matriz_data

def main():
    Estrato_1,Estrato_2,Estrato_3,Estrato_4,Estrato_5,Estrato_6,Sin_Estrato=0,0,0,0,0,0,0
    prom_p=0 
    A,A1,A2,B,B1=0,0,0,0,0
    No_Oficial,Oficial=0,0
    men,women=0,0
    No_data,data=0,0
    header,matriz_data=lectura() 
    print('Si va a buscar  depto=BOGOTÁ pero si es ciudad=BOGOTA D.C')
    try:
        item_1=str(input('Get into your first item for compare-->'))  
    except:
        item_1=str(input('Get into AGAIN your first item for compare-->'))
    else:
        for index in range(len(matriz_data)):
            if item_1 == matriz_data[index][2] and item_1==matriz_data[index][4]:
                item_1=str(input('SE REPITE OTRA VEZ')) 

    item_1.upper()  
    for index in range(len(matriz_data)):
            if item_1 == matriz_data[index][2] or item_1==matriz_data[index][4]:
                data+=1
                prom_p+=int(matriz_data[index][6])
                if matriz_data[index][0] == 'NO OFICIAL':
                    No_Oficial+=1
                if matriz_data[index][0] == 'OFICIAL':
                    Oficial+=1
                if matriz_data[index][1]== 'A-':
                    A+=1
                if matriz_data[index][1]== 'A1':
                    A1+=1
                if matriz_data[index][1]== 'A2':
                    A2+=1
                if matriz_data[index][1]== 'B+':
                    B+=1
                if matriz_data[index][1]== 'B1':
                    B1+=1
                if matriz_data[index][3]=='M':
                    men += 1
                if matriz_data[index][3]=='F':
                    women += 1
                if matriz_data[index][5]== 'Estrato 1':
                    Estrato_1+=1
                if matriz_data[index][5]== 'Estrato 2':
                    Estrato_2+=1
                if matriz_data[index][5]== 'Estrato 3':
                    Estrato_3+=1
                if matriz_data[index][5]== 'Estrato 4':
                    Estrato_4+=1
                if matriz_data[index][5]== 'Estrato 5':
                    Estrato_5+=1
                if matriz_data[index][5]== 'Estrato 6':
                    Estrato_6+=1
                if matriz_data[index][5]== 'Sin Estrato':
                    Sin_Estrato+=1
                else:
                    No_data+=1

    prom=prom_p/data

    
    print(f"{item_1}")
    print("Estatros")
    print(f"Estrato 1 ->", {Estrato_1}, "Estrato 2 ->", {Estrato_2} , "Estrato 3 ->", {Estrato_3} , "Estrato 4 ->", {Estrato_4} ) 
    print(f"Estrato 5 ->", {Estrato_5} ,"Estrato 6 ->" , {Estrato_6} , "Sin Estrato  ->" , {Sin_Estrato} )

    print('Genero')
    print(f"'men' {men} 'women' {women}")

    print("COLEGIO")
    print(f"OFICIAL -->{Oficial}  NO OFICIAL-->{No_Oficial}")

    print("Nivel de ingles")
    print(f" A- -> {A} A1-> {A1}  A2-> {A2} B+ -> {B} B1-> {B1}")

    print('Promedio de notas')
    print(f"{prom}")
    
    print(f"No data {No_data}")

if __name__=='__main__':
    main()



