import sys
#这个算法的目标是在给定一个二进制字符串中找到一个子串，
# 满足其中 0 的数量比 1 的数量多一个，且该子串是长度最大的。
# 先找出所有的 001 串，将其存入列表中。对于每个 001 串，
# 计算其中 0 和 1 的数量，如果 0 的数量比 1 的数量多一个，就把这个子串存入结果列表中。然后找到结果列表中长度最大的子串并输出。

#定义solve_method()函数，
def solve_method(in_str):    #0010101010110000101000010
    bits = list(in_str)      #[0,0,1,0,1,0,1,0,1,0,1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0 ]
                             # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
    waves = []               #[]

    first = in_str.find("1")  #2
    last = in_str.rfind("1")  #23
    i = first  #2

    while i <= last:  #2<=23;3;4;5;6;7;8;9;10;11;12;   13;14;15;16;17;18;19;20;21;22;23;24。
        if i + 1 < len(bits) and bits[i] == "0" and bits[i + 1] == "0":
            #3<25 bit[2]=1 bit[3]=0;
            #4<25 bit[3]=0 bit[4]=1;
            #5<25 bit[4]=1 bit[5]=0;
            #6<25 bit[5]=0 bit[6]=1;
            #7<25 bit[6]=1 bit[7]=0;
            #8<25 bit[7]=0 bit[8]=1;
            #9<25 bit[8]=1 bit[9]=0;
            #10<25 bit[9]=0 bit[10]=1;
            #11<25 bit[10]=1 bit[11]=1;
            #12<25 bit[11]=1 bit[12]=0;
            #13<25 bit[12]=0 bit[13]=0; ****
            #14<25 bit[13]=0 bit[14]=0; ****
            #15<25 bit[14]=0 bit[15]=0; ****
            #16<25 bit[15]=0 bit[16]=1;
            #17<25 bit[16]=1 bit[17]=0;
            #18<25 bit[17]=0 bit[18]=1;
            #19<25 bit[18]=1 bit[19]=0;
            #20<25 bit[19]=0 bit[20]=0; ****
            #21<25 bit[20]=0 bit[21]=0; ****
            #22<25 bit[21]=0 bit[22]=0; ****
            #23<25 bit[22]=0 bit[23]=1;
            waves.append(in_str[first - 1:i + 1])  #first:2,i:12; first:13,i:13; first:14,i:14; first:15,i:19; first:20,i:20; first:21,i:21;
            #waves=in_str==[1:13]=[0,1,0,1,0,1,0,1,0,1,1,0]
            #waves=in_str==[12:14]=[0, 0]
            #waves=in_str==[13:15]=[0, 0]
            #waves=in_str==[14:20]=[0,0,1,0,1,0]
            #waves=in_str==[19:21]=[0,0]
            #waves=in_str==[20:22]=[0,0]
            while i < len(bits) and bits[i] == "0":
            #12<25 bits[12]=0;
            #13<25 bits[13]=0;
            #14<25 bits[14]=0;
            #20<25 bits[20]=0;
            #21<25 bits[21]=0;
                i += 1 #i:13;14;15;20;21;22;
            first = i  #first:13;14;15;20;21;22;
        else:
            i += 1  #3;4;5;6;7;8;9;10;11;12;  16;17;18;19; 23;24。
        #waves=[0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0]
    waves.append(in_str[first - 1:last + 2])
    #in_str[21:25]=[0,0,1,0]
    #waves=[0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0]

    res = []
    for wave in waves: #waves=[0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0]
        n0, n1 = 0, 0
        for c in wave:    #0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0
            if c == "0":  #
                n0 += 1   #21
            else:
                n1 += 1   #9

        if n0 - n1 == 1:  # 12
            res.append(wave) #

    res.sort(key=len, reverse=True)
    if res:
        print(res[0], end="")
    else:
        print("-1", end="")


if __name__ == "__main__":
    in_str = sys.stdin.readline().strip()
    solve_method(in_str)