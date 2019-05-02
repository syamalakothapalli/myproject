l1,p = list(input()),1
while l1 != ['Z']:
    l2,l3,l4,l5 = input(),input(),input(),input()
    list1,list2 = [list(l1),list(l2),list(l3),list(l4),list(l5)],list(input())
    print('puzzle #',p)
    for i in range(5):
        for j in range(5):
            if list1[i][j] == " ":f,s = i,j
    for ch in range(len(list2)):
        if list2[ch] == 'A':
            if f == 0:
                print('This configuration is not possible')
                break
            else:list1[f][s],list1[f-1][s],f,s = list1[f-1][s],list1[f][s],f-1,s
        elif list2[ch] == 'B':
            if f == 5:
                print('This configuration is not possible')
                break
            else:list1[f][s],list1[f+1][s]f,s = list1[f+1][s],list1[f][s],f+1,s
        elif list2[ch] == 'R':
            if s == 5:
                print('This configuratiom is not possible')
                break
            else:list1[f][s],list1[f][s+1],f,s = list1[f][s+1],list1[f][s],f,s+1
        elif list2[ch] == 'L':
            if s == 0:
                print('This configuration is not possible')
                break
            else:list1[f][s],list1[f][s-1],f,s = list1[f][s-1],list1[f][s],f,s-1
        elif list2[ch] == '0':
            for f in range(5):
                for s in range(5):
                    print(list1[f][s],end = ' ')
                print()
        else:
            break
    l1 = list(input())        
    p += 1   
