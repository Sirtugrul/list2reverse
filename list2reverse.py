liste=[]

def list2reverse(gliste):
    gliste.reverse()
    
    for i in gliste:
        liste1=[]
        if type(i)==list:
            i.reverse()
            
            for j in i:
                 liste1.append(j)
            liste.append(liste1)
        else:
            liste.append(i)
       


list2reverse([[7, 6, 5], [4, 3], [2, 1]])
print(liste)








