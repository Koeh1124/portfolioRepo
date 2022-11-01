cats = []
with open("allCats.txt","r") as file:
    f = file.readlines()
    for line in f:
        line = line.strip()
        print(line)
        if "/" in line:
            line.replace("|","/")
        cats.append(line)
print(cats)
for cat in cats:
    with open(cat+".txt","w+") as file:
        ui = ""
        while ui != "q":
            try:
                ui = input(cat+"\n")
                if ui != "q" and ui != "":
                    file.write(ui+"\n")
            except:
                print("oops")
        file.close()