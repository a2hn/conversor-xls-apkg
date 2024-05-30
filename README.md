# Conversor de xls em apkg
### Transforma arquivos de planilhas (excel, sheets) em flashcards
---
Para conseguir converter as colunas do excel em flashcards é precisa alterar certas informações no código. Nas partes `file_path = "caminho_do_arquivo"` e `q_column = 'PERGUNTA' a_column = 'RESPOSTA'`. 

## Alterar

* O caminho do arquivo será algo parecido com isso: C:\Users\joao\Desktop\arquivo.xls.

* O `q_column` é igual ao primeiro item da coluna do excel que deseja colocar no flahcardcard, nesse caso, a "PERGUNTA".

* O `a_column` é igual ao segundo item da coluna do excel que deseja colocar no flahcardcard, nesse caso, a "RESPOSTA". 
---

## Adicionar novo item no flashcard

1. Caso queira adicionar mais um item basta criar mais uma variavel abaixo de `a_column` e atribuir a string do primeiro item da coluna do excel. Como por exemplo: `column = 'DESCRIÇÃO'`. 

2. Depois é só criar uma variável dentro da função, embaixo da `resposta = row[a_column]`, atribuindo a ela a sua coluna do excel, dessa forma: `descricao = row[column]`.

3. Pode-se adicionar essas novas linhas da coluna do excel na frente ou na traseira da carta, como por exemplo `front = f"DESCRIÇÃO: {descricao} {pergunta if pd.notna(pergunta) else ''}"`.

É isso, espero ter ajudado.

Peço a compreensão de todos pois estou começando. Caso tenha algo a acrescentar é só criar uma issues.


OBRIGADO!
