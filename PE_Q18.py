line1 = [75]
line2 = [95, 64]
line3 = [17, 47, 82]
line4 = [18, 35, 87, 10]
line5 = [20, 4, 82, 47, 65]
line6 = [19, 1, 23, 75, 3, 34]
line7 = [88, 2, 77, 73, 7, 63, 67]
line8 = [99, 65, 4, 28, 6, 16, 70, 92]
line9 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
line10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
line11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
line12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
line13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
line14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
line15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

paths = [0]
for a in range(2):
    temp2 = 75 + line2[a]
    for b in [a,a+1]:
        temp3 = temp2 + line3[b]
        for c in [b,b+1]:
            temp4 = temp3 + line4[c]
            for d in [c,c+1]:
                temp5 = temp4 + line5[d]
                for e in [d,d+1]:
                    temp6 = temp5 + line6[e]
                    for f in [e,e+1]:
                        temp7 = temp6 + line7[f]
                        for g in [f,f+1]:
                            temp8 = temp7 + line8[g]
                            for h in [g,g+1]:
                                temp9 = temp8 + line9[h]
                                for i in [h,h+1]:
                                    temp10 = temp9 + line10[i]
                                    for j in [i,i+1]:
                                        temp11 = temp10 + line11[j]
                                        for k in [j,j+1]:
                                            temp12 = temp11 + line12[k]
                                            for l in [k,k+1]:
                                                temp13 = temp12 + line13[l]
                                                for m in [l,l+1]:
                                                    temp14 = temp13 + line14[m]
                                                    for n in [m,m+1]:
                                                        temp15 = temp14 + line15[n]
                                                        paths.append(temp15)
max = 0
for i in range(len(paths)):
    if max < paths[i]:
        max = paths[i]
print(max)
