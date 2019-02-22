class bolo:
    def __init__(instancia, sabor, cobertura):
        instancia.sabor = sabor
        instancia.cobertura = cobertura
     
bolo1 = bolo('chocolate', 'chocolate')
bolo2 = bolo('chocolat', 'leite condensado')

print(bolo1.sabor, bolo1.cobertura)
print(bolo2.sabor, bolo2.cobertura)
