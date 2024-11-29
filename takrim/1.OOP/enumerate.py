# with open("ice.txt","r") as db:
#     lines = db.readlines()
# count = 1

# def makeCompatible(num):
#     if len(str(num))<2:
#         return "7710" + str(num)
#     else:
#         return "771" + str(num)
# for i in lines:
#     with open("icestudents.db",'a') as file:
#         file.writelines(f"{makeCompatible(count)},{i.strip()}\n")
#     count+=1
with open("hello.txt","w") as f:
    f.write({"Hello":"world!"})