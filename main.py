meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROLF": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro"
            }
    
for i in range(5):

    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("no tenemos informacion sobre esta palabra.")
