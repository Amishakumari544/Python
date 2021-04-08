letter= '''hi,everyone\n I am <|name|> sophomore who loves to meet new people '''
print(letter)
a=input("\tenter your name")
letter.replace('<|name|>', a)
print(letter)