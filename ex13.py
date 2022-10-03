carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))
carrinho.append(('Produto 4', 90))
carrinho.append(('Produto 5', 10))

total = sum([x[1] for x in carrinho])
print(total)
