# Conversor de xls em apkg
### Transforma arquivos de planilhas (excel, sheets) em flashcards
---
Para conseguir converter as colunas do excel em flashcards é precisa adicionar certas informações no código
Nas partes `file_path = "caminho_do_arquivo"` `q_column = 'PERGUNTA' a_column = 'RESPOSTA'`
O caminho do arquivo será algo parecido com isso: C:\Users\joao\Desktop\arquivo.xls
O "q_column" é primeiro item (nome, número) da coluna do excel que deseja colocar no card, nesse caso, a pergunta
O "a_column" é segundo item (nome, número) da coluna do excel que deseja colocar no card, nesse caso, a resposta
Caso queira adicionar mais um item basta criar mais uma variavel abaixo de "a_column" e atribuir a str do primeiro item da coluna, como por exemplo `column = 'DESCRIÇÃO'`. Depois é só criar uma variável dentro da função abaixo da `resposta = row[a_column]`, atribuindo a ela a sua coluna do excel, dessa forma: `descricao = row[column]`. Dessa forma, pode-se adicionar essas novas linhas da coluna na frente ou na traseira da carta, como por exemplo `front = f"DESCRIÇÃO: {descricao} {pergunta if pd.notna(pergunta) else ''}"`.

É isso, espero ter ajudado.
Peço a compreensão de todos pois estou começando.
Caso tenha algo a acrescentar é só criar uma issues.
OBRIGADO!