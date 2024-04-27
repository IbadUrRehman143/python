def add_info(sentences):
    sentences[0] =  "Name :  | " + sentences[0] 
    sentences[1] =  "Price:  | " + sentences[1] 
    sentences[2] =  "S.no :  | " + sentences[2] 
    sentences[3] =  "Size :  | " + sentences[3] 

def heading_line(sentences, heading = "Fan Information"):
    lineWidth = find_grater_sentence(sentences)
    headingWidth = len(heading)
    halfLine = lineWidth//2
    halfHeading = headingWidth//2
    halfLine = halfLine-halfHeading
    print("+"*halfLine + "< " + heading + " >" + "+"*halfLine)


def find_grater_sentence(sentences):
    grater = len(sentences[0])

    for i in range(1, len(sentences)):
        if len(sentences[i]) > grater:
            grater = len(sentences[i])
    return grater

def tile(sentences, char="*"):
    add_info(sentences)
    lineWidth = find_grater_sentence(sentences)
    lineWidth = lineWidth + 4
    # print(char*lineWidth)
    heading_line(sentences)
    for i in range(len(sentences)):
        spaces = lineWidth - len(sentences[i])
        spaces = spaces - 3
        print(char + " " +  str(sentences[i]) + " "*spaces + char)
    
    print(char*lineWidth)


