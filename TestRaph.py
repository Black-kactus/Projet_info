#test
ch='af ba cd ef th uj af hy'
L=ch.split(" ")
L2=[]
for i in range(0,len(L),2):
    L2.append(L[i]+L[i+1])
#print(L2)

def interpreteur_script(script):
    script = script.split(' ')
    L=[]
    #for i in range(0,len(script),2):
        #L.append([script[i].split("-"),script[i+1].split("-")])
    for i in range(len(script)):
        L.append(script[i].split("-"))
    return L

print(interpreteur_script("e2-e4 c7-c5 c2-c3 d7-d5 e4-d5 d8-d5 c2-d4 g8-f6 g1-f3 c8-g4 f1-e2 e7-e6 h2-h3 g4-h5 roque b8-c6 c1-e3 c5-d4 c3-d4 f8-b4"))