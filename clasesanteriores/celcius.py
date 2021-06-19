entrada = input('Digite grados: ')
entrada2 = input('Tipo: ')
try:     
    grados = float(entrada)
    if(entrada2 == 'c' or entrada2 == 'C'):
        far = grados*(9/5)+32
        print("Grados fahrenheit %.2f"%(far))
    elif(entrada2 == 'f' or entrada2 == 'F'):
        cel = (grados - 32.0)*(5.0/9.0)
        print("Grados celcius %.2f"%(cel))
    else:
        print("Unidad no identificada");
except:    
     print('Debe ingresar un número')