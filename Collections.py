pricet='a:2:{i:0;a:2:{s:3:"qty";i:1;s:5:"price";s:4:"0.39";}i:1;a:2:{s:3:"qty";i:3;s:5:"price";s:4:"0.33";}}'
PriceTierCount=int(pricet[2])
print(PriceTierCount)
loop_pos = 0
sp=pricet.split(';')
holdingstring:str =''
firstPT_QTY:int =0
firstPT_Val:float =0.0
secPT_QTY:float =0
secPT_Val:float =0.0
PTCount:int = 0
for s in sp:
    if loop_pos==2:
        #look for first qty
        spq=s.split(':')
        firstPT_QTY=int(spq[1])
        PTCount+=1
    if loop_pos == 4:
        # look for first qty
        spq = s.split(':')
        holdingstring = spq[2]
        firstPT_Val = float(holdingstring[1:-1])
    if loop_pos == 7:
        # look for first qty
        spq=s.split(':')
        secPT_QTY=int(spq[1])
        PTCount += 1
    if loop_pos == 9:
        # look for first qty
        spq = s.split(':')
        holdingstring = spq[2]
        secPT_Val=float(holdingstring[1:-1])
    loop_pos+=1

dic_build =''
loop_dic=0
commaseperator:str=','
for loop_dic in range(0, PTCount):
    if dic_build=='':
        commaseperator=''
    else:
        commaseperator=','

    dic_build =  dic_build + commaseperator + "'" + str(loop_dic) +"':{'num':" + str(0) +",'qty':" + str(1) + ",'price':" + str(0.0) + "}"
full_dict="{" +dic_build + "}"
print(dic_build)
#retP={'1':{'num':0,'qty':1,'price':0.3},'2':{'num':0,'qty':4,'price':0.25}}
print("s")