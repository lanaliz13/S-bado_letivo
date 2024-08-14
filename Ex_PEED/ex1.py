
precos_acoes = [ 
      [150, 200, 180, 220, 170], 
      [155, 205, 185, 225, 175], 
      [160, 210, 190, 230, 180],
      [165, 215, 195, 235, 185], 
      [170, 220, 200, 240, 190], 
      [175, 225, 205, 245, 195], 
      [180, 230, 210, 250, 200] 
]




def calcular_media(precos_acoes):
    total_dias = len(precos_acoes)           
    num_empresas = len(precos_acoes[0])      
    medias = []                             
    
    for j in range(num_empresas):            
        soma = 0
        for i in range(total_dias):          
            soma += precos_acoes[i][j]     
        media = soma / total_dias          
        medias.append(media)                
    
    return medias                           

media_diaria = calcular_media(precos_acoes)
print("Média Diária:", media_diaria)

def variacao_diaria(preco_acoes):
    num_dias = len(precos_acoes)
    num_empresas = len(precos_acoes[0])
    variacoes = []

    for j in range(num_empresas):
        preco_min = precos_acoes[0][j]
        preco_max = precos_acoes[0][j]
        
        for i in range(1, num_dias):
            preco = precos_acoes[i][j]
            if preco < preco_min:
                preco_min = preco
            if preco > preco_max:
                preco_max = preco

        variacao = preco_max - preco_min
        variacoes.append(variacao)

    return variacoes

variacao_diaria = variacao_diaria(precos_acoes)
print("Variação Diária:", variacao_diaria)

def encontramaxmin(precos_acoes, indice_empresa):
    preco_empresa = []
    for i in range(len(precos_acoes)):
        preco_empresa.append(precos_acoes[i][indice_empresa])
    
    dia_max = 0
    dia_min = 0

    for i in range(1, len(preco_empresa)):
        if preco_empresa[i] > preco_empresa[dia_max]:
            dia_max = i
        if preco_empresa[i] < preco_empresa[dia_min]:
            dia_min = i

    return dia_max, dia_min

dia_max_preco, dia_min_preco = encontramaxmin(precos_acoes, 1)
print(f"Dia com maior preço da empresa B: {dia_max_preco + 1} (1 = Primeiro dia)")
print(f"Dia com menor preço da empresa B: {dia_min_preco + 1} (1 = Primeiro dia)")


def atualizarmatriz_media(precos_acoes, aumento_percentual):
    num_dias = len(precos_acoes)
    num_empresas = len(precos_acoes[0])
    aumento = 1 + aumento_percentual / 100
    precos_atualizados = []
    
    for i in range(num_dias):
        linha_atualizada = []
        for preco in precos_acoes[i]:
            preco_atualizado = preco * aumento
            linha_atualizada.append(preco_atualizado)
        precos_atualizados.append(linha_atualizada)

    return calcular_media(precos_atualizados)

nova_media_diaria = atualizarmatriz_media(precos_acoes, 5)
print("Nova Média Diária com aumento de 5%:", nova_media_diaria)