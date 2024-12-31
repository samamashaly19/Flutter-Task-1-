list_Of_Dublications=[10, 20 ,23 ,45, 96 , 10 ,21 ,22 ,21]

List_of_Uniques=[]

for number in list_Of_Dublications:
    if number not in List_of_Uniques:
        List_of_Uniques.append(number)

reversed_list=[]
for number in reversed(List_of_Uniques):
    reversed_list.append(number)
print ("The original list:",list_Of_Dublications)
print ("list after removing duplications:",List_of_Uniques)
print ("Reversed List:",reversed_list)
