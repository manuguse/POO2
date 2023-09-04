from produto import Produto
from cliente import Cliente
from categoria import CategoriaProduto

produto1 = (Produto(1, "Esse é o Produto 1", CategoriaProduto("Categoria 1"), 10, 10.0, Cliente("Cliente 1", "111111111")))
print(produto1.get_descricao())