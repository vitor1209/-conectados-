SELECT Nome_Produto AS 'Nome Produto', Preco_Unit AS 'Preco Unit'
	FROM produtos
	WHERE Preco_Unit >= 1000
	ORDER BY Preco_Unit asc;
      

SELECT Nome_Produto AS 'Nome Produto', Marca_Produto AS 'Marca produtos'
	FROM produtos
    WHERE Marca_Produto = "DELL";


SELECT *
	FROM pedidos
    WHERE Data_venda = "2019-01-03";

SELECT *
	FROM clientes
    WHERE Sexo = "M" and Estado_Civil = "S";

SELECT *
	FROM produtos
    WHERE Marca_Produto = "DELL" or Marca_Produto = "SAMSUNG";
    
-- Funções 

select 
	count(	distinct Escolaridade)
	from clientes;
    
select  
	sum(Receita_Venda) AS 'Soma Venda' , 
    AVG(Receita_Venda) AS 'media Venda' , 
    min(Receita_Venda) AS 'menor Venda' , 
    max(Receita_Venda) AS 'maior Venda' 
from pedidos;

select 
	Sexo, 
    count(*) AS 'qtd clientes'
	from clientes
    group by Sexo;
    
select 
	Marca_Produto, 
    count(*) AS 'qtd de marca'
	from produtos
    group by Marca_Produto 
    ORDER BY COUNT(*) DESC;
    
select 
	ID_Loja,
    sum(Receita_Venda) AS 'soma receita' ,
    sum(Custo_Venda) AS 'soma custo'
	from pedidos
    group by ID_loja 
	ORDER BY sum(Receita_Venda) asc;
    
-- tabela A -> tabela FATO = tabela pedidos
-- tabela B -> tabela DIMENSÃO = tabela lojas

-- chave primaria -> ID_loja
-- chave estrangeira -> ID_loja

select 
	pedidos.*,
    lojas.Loja,
    lojas.Gerente,
    lojas.Telefone
from pedidos
inner join lojas
	on pedidos.ID_Loja = Lojas.ID_Loja;