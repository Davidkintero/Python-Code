print('Bienvenido al sistema de ubicación para zonas públicas WIFI')
nombre_usuario = 51743
contrasena = 34715

nombre_usuarioinput = int(input('Ingrese el nombre de usuario: '))

if nombre_usuario == nombre_usuarioinput:
    contrasena_input = int(input('Ingrese la contrasena: '))
    if contrasena == contrasena_input:
        captcha1= 743
        captcha2= 5 * 3 - 5 - 6
        captchasuma = captcha1 + captcha2
        captcha_input = int(input(f'Solucione el siguiente captcha: \n743+4: '))
        if captcha_input == captchasuma:
            print('Inicio de sesion con exito')
            print('Sesion Iniciada')
        else:
            print('Error')
    else:
        print('Error')
else:
    print('Error')

