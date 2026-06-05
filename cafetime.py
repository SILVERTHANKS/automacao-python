while True:
    #estado do cafe
    
    cafe = str(input("Se café tiver quente?digitar = (vazio/cheio):")).strip().lower()
    if cafe == "vazio":
        print('encher')
        break
    
    elif cafe == "cheio":
        print('Tomar')
        break

    else:
        print("Esta tudo bem")
        break

else:
    print('fim do progama')        

