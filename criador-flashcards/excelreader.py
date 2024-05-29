import pandas as pd

# Ler o arquivo XLS
file_path = "C:\\Users\\aaron\\Desktop\\arquivoanki.xlsx"
data = pd.read_excel(file_path)

# Declaração
coluna1 = 'PERGUNTA'
coluna2 = 'RESPOSTA'

# Função para criar os flashcards em uma lista
def create_flashcards():
    flashcards = []
    for index, row in data.iterrows():
        pergunta = row[coluna1]
        resposta = row[coluna2]
        
        front = f"{pergunta if pd.notna(pergunta) else ''}"
        back = f"{resposta if pd.notna(resposta) else ''}"
        
        flashcards.append((front, back))
    
    return flashcards

# Criar flashcards
flashcards = create_flashcards()

# Mostar a frente e o verso da carta
for front, back in flashcards:
    print(f"Front: {front}\nBack: {back}\n")