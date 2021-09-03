names = ["Cristian", "Nini", "Julian", "Jonathan", "JuanDavid", "MaryAnn", "Mayra",
"JuanPablo",
"Lady",
"Stephanie",
"Wilson",
"Diego",
"Monica",
"Jhonatan"]

for name in names:
    f = open("tools/" + name + ".py", "a")
    method = 'def add' + name + 'ToParty(party):\n\tpass'
    f.write(method)
    f.close()

