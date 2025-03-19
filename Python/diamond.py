'''
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. 
Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size
'''

def diamond(main):
    if main < 0 or main%2 == 0:
        return None
    else:
        lados_arriba =  0
        tot = main
        while tot > 1:
            lados_arriba += 1
            tot -= 2
        
        diamante = ''
        fila = 0
        nueva_fila = 1
        lados_abajo = lados_arriba
        
        while lados_arriba > 0:
            diamante += ' '*lados_arriba + '*' + '*'*2*fila + '\n'
            lados_arriba -= 1
            fila += 1
            
        diamante += '*'*main + '\n'
        
        while lados_abajo > 0:
            diamante += ' '*nueva_fila + '*' + '*'*2*(lados_abajo-1) + '\n'
            lados_abajo -= 1
            nueva_fila += 1
        
        return diamante
