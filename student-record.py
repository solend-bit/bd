F="students.txt"
while (c:=input("\n1.Add 2.View 3.Exit: "))!="3":
    if c=="1":
        try:
            open(F,"a").write(",".join(input(f"Enter {x}: ") for x in ["ID","Name","Marks"])+"\n")
        except Exception as e:
            print("Error:",e)
    elif c=="2":
        print("ID\tName\tMarks\n"+"-"*30)
        [print(*r.strip().split(","),sep="\t") for r in open(F)]
    else: print("Invalid!")
print("Thank You!")