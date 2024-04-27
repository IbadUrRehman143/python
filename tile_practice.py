
def find_grater_sentence(sentences):
    grater = len(sentences[0])

    for i in range(1, len(sentences)):
        if len (sentences[i]) > grater:
            grater = len (sentences[i])

    return grater

def tile (sentences, char):
    lineWidth = find_grater_sentence(sentences)
    lineWidth = lineWidth + 4
    print(char*lineWidth)
    for i in range (len(sentences)):
        spaces =lineWidth - len(sentences[i])
        spaces = spaces - 3
        print(char + " " + str(sentences[i])+ " "*spaces + char)

    print(char*lineWidth)
sen = [
    "zama ashna raze da khapero da bagh malyara",
    "golona rawra da gulzara",
    "zama ashna raze da khapero da bagh malyara zama ashna raze", 
    "Back in June we diliverd oxygen equipment of the same size. Te quick brown fox jumps over the lazy dog.",
    "Love is life.",
    "My Wife is the world best Wife."
]

tile(sen, "*")
tile(sen, "=")
    