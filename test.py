emails = []

# Cristian
emails.append("crisfemoar2011@hotmail.com")
emails.append("tumamita@gmail.com")

# Nini



# Julian



# Jonathan Gonzalez



# Juan David



# Mary Ann



# Mayra



# Juan Pablo



# Lady



# Stephanie



# Wilson



# Diego



# Monica



# Jhonatan Andres



#----------------------------
dic = dict()

with open("mails.txt", "r") as f:
    for line in f.readlines():
        mail, name = line.split(",")
        dic[mail] = name

for mail in emails:
    if mail in dic:
        print("El email %s es de %s" %(mail, dic[mail]) )
    else:
        print("El email %s no está en la base de datos" % mail)

