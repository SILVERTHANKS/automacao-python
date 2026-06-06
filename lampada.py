#lampada
lampada = False
def Ligar_lampada():
    global  lampada
    lampada = True 
    print('Lampada Acesa!')  
def Desligar_lampada():
    global lampada
    lampada = False
    print('Lampada apagada!')
def Estado_lampada():
    if lampada:
        print('lampada esta ligada')
    else:
        print('lampada Desligada')    

Ligar_lampada() 
Estado_lampada()
Desligar_lampada()
Estado_lampada()
