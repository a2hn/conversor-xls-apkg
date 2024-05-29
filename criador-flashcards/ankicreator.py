from excelreader import create_flashcards
import genanki

nomearq = 'pm.apkg'

# Criar o modelo do Anki
model_id = 1607392319
model = genanki.Model(
  model_id,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

# Criar o deck
deck_id = 2059400110
deck = genanki.Deck(
  deck_id,
  'Flashcards Deck')

# Adicionar os flashcards ao deck
for front, back in create_flashcards():
    note = genanki.Note(
      model=model,
      fields=[front, back])
    deck.add_note(note)

# Salvar o arquivo do Anki
genanki.Package(deck).write_to_file(nomearq)