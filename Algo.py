
import math



def max_throughput(k,V,S):
    m = 0
    v = -1
    for i, j in enumerate(V[k]):
        if i in S:
            continue
        
        if j[2] == 1:
            if m < j[0]:
                m = j[0]
                v = i
            else:
                pass
        else:
            if m < j[1]:
                m = j[1]
                v = i
            else:
                pass
    return v
        
def updating(V,list_label,x):
    for i in list_label[1:]:
        direction = V[i[2]][i[1]][2]
        
        V[i[1]][i[2]][0] -= direction * x
        V[i[1]][i[2]][1] += direction * x
        
        V[i[2]][i[1]][0] -= direction * x
        V[i[2]][i[1]][1] += direction * x

def printning(res,f):
    d = 0
    for i in res[:-1]:
        print(f" Максимальний потік на цей маршрут : (f{d} = {f[d]}) |>  ",end="")
        for j in i:
            print(j[1]+1,end="")
            if j[1] != stock:
                print(" --> ",end="")
        d += 1
        print()    
        
        

V = [[[0, 0, 1], [7, 0, 1], [7, 0, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
      [[7, 0, -1], [0, 0, 1], [5, 0, -1], [4, 0, 1], [3, 0, 1], [0, 0, 0]],
      [[7, 0, -1], [5, 0, 1], [0, 0, 1], [0, 0, 0], [10, 0, 1], [0, 0, 0]],
      [[0, 0, 0], [4, 0, -1], [0, 0, 0], [0, 0, 1], [11, 0, -1], [8, 0, 1]],
      [[0, 0, 0], [3, 0, -1], [10, 0, -1], [11, 0, 1], [0, 0, 1], [4, 0, 1]],
      [[0, 0, 0], [0, 0, 0], [0, 0, 0], [8, 0, -1], [4, 0, -1], [0, 0, 1]]]



nv = len(V)
source = 0
stock =  nv - 1                                 # minus 1 because of indexes[0,...,5]
label = (math.inf, 0, source)
f = []
res_route = []

counter = source
while counter != -1:
    k = source
    list_label = [label]
    S = {source}
    while k != stock:        
        counter = max_throughput(k,V,S)        
        if counter == -1:
            if k == source:
                break
            else:
                k = list_label.pop()[2]
                continue
        else:
            if V[k][counter][2] == 1:
                a = V[k][counter][0]
            elif V[k][counter][2] == -1:
                a = V[k][counter][1]
        
        list_label.append((a,counter,k))
        S.add(counter)
        
        if counter == stock:
            f.append(min(list_label)[0])
            updating(V,list_label,f[-1])
            break
       
        k = counter
    
    res_route.append(list_label)

print("\nУсі маршрути: \n")
printning(res_route,f)
res = sum(f)
print("\nМаксимальний потік на мережу :",res)
        
