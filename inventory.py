def func(list, opr, list_row, opr_row, answers):
    for i in range(0,opr_row):

        if(opr[i][0]=="ADD"):           
                        #add operation
            for j in range (0, list_row):
                if(list[j][0]==opr[i][1]):
                    flag=True
                    index=j
                    break
                else:
                    flag=False

            if(flag==True):
                l=int(list[index][1]) 
                o=int(opr[i][2])
                sum=l+o
                list[index][1]=sum
                answers.append("UPDATED Item "+ list[index][0])

            else:
                list.extend([[opr[i][1], opr[i][2]]])
                answers.append("ADDED Item " +  opr[i][1])
                list_row+=1

        elif(opr[i][0]=="DELETE"): 
                        # delete operation
            for j in range (0, list_row):

                if(list[j][0]==opr[i][1]):
                    flag_del=True
                    index=j
                    break
                else:
                    flag_del=False

            if(flag_del==True):
                if(int(opr[i][2]) < int(list[index][1])):

                    answers.append("DELETED Item " + list[index][0])
                    list[index][1]=int(list[index][1]) - int(opr[i][2])

                else:
                    answers.append("Item "+ list[index][0] + " could not be DELETED")

            else:
                answers.append("Item " + opr[i][1] + " does not exist")

    print(list)       
    sum=0
    for i in range(0,list_row):
        sum+=int(list[i][1])
    answers.append("Total Items in Inventory: "+ str(sum))
    
if __name__ == '__main__':
    test=int(input())
    final=[]
    for i in range (0,test):
        n=int(input())        #number of items
        inventory=[]
        inventory = [input().split() for i in range(n)]
        print(inventory)

        m=int(input())        #number of operations
        operations=[]
        operations = [input().split() for i in range(m)]
        func(inventory, operations, n, m, final)

    # final.remove(0)
    for x in final:
        print(x)