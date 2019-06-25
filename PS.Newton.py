
'''Exercicio 3'''

def filmes(ano):
    dicfilme = {
        2013:"Frozen",
        2012:"Marvel's The Avengers",
        1997:"Titanic",
        2018:"Black Panther",
        2015:"Avengers: Age of Ultron",
        2009:"Avatar",
        2015:"Star Wars: The Force Awakens",
        2017:"Star Wars: The Last Jedi",
        2015:"Furious 7",
        2011:"Harry Potter and The Deathly Hallows - Part 2",
        2019:"Avengers: Endgame",
        2015:"Jurassic World",
        2018:"Avengers: Infinity War",
        2017:"Beauty and the Beast",
        2018:"Jurassic World: Fallen Kingdom",
        }
    dicUS$ = {
        2013:"127640335",
        2012:"1518812988",
        1997:"2187463944",
        2018:"1346913161",
        2015:"1405403694",
        2009:"2787965087",
        2015:"2068223624",
        2017:"1332539889",
        2015:"1516045911",
        2011:"1341693157",
        2019:"2750667499",
        2015:"1671713208",
        2018:"2048359754:",
        2017:"1263521126",
        2018:"1309484461",
        }
   
    return(dicfilmes[ano], dicUS$[ano])

'''Exercicio 4'''

for k in dicUS$:
    print('Valor arrecadado em {} :'.format(k)) 
    print('US$ {}'.format(dicfilmes.get(k))

'''Exercicio 2'''

def calcular_valor(valor):
     valorfloat = float(valor)
     valor_real = valorfloat/1000000000  
     return (valor_real:.2f)
               

          
    
