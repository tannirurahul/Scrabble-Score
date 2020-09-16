def score(word):
    word = word.upper()
    m={
    1:["A", "E", "I","O", "U", "L", "N", "R", "S","T"],
    2:["D", "G"],
    3:["B", "C", "M","P"],
    4:["F","H","V","W","Y"],
    5:["K"],
    8:["J", "X"],
    10:["Q", "Z"]
    }
    value =0
    for x in word:
        for key,y in m.items():
            if x in y:
                value+= key
        print(value)
    return value