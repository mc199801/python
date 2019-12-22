f = open("C:\\小鲶鱼.txt")

boy = []
giel = []
count = 1

for each_line in f:
    if each_line[:6] != "======":
        (role, line_spoken) = each_line.split("：", 1)
        if role =="小甲鱼":
            boy.append(line_spoken)
        if role == "小客服":
            giel.append(line_spoken)
    else:
        file_name_boy = "boy_" + str(count) + ".txt"
        file_name_giel = "giel_" + str(count) + ".txt"

        boy_file = open("file_name_boy","w")
        giel_file = open("file_name_giel", "w")

        boy_file.writelines(boy)
        giel_file.writelines(giel)

        boy_file.close()
        giel_file.close()

        boy=[]
        giel=[]
        count +=1

f.close()
