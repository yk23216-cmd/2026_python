#a=input()
#b=input()
#print("從{1}飛往{0}，再從{0}飛回{1}".format(a,b))

#number1=int(input())
#number2=int(input())
#number3=int(input())
#print("倒序結果 : {2} -> {1} -> {0}".format(number1,number2,number3))

#a=input()
#b=input()
#print("您的{obj}成績為 {gra} 分".format(obj=a,gra=b))

#a=input()
#b=input()
#print("這隻寵物叫做 {name}，牠是一隻 {an}".format(name=a,an=b))

#a=input()
#b=input()
#D = {"thing":a, "mon":b}
#print("{thing}的價格是 {mon} 元".format(**D))

#c1=input()
#c2=input()
#List1=[c1,c2]
#print("前景顏色為 : {0[0]}，背景顏色為 : {0[01]}".format(List1))

#a=input()
#b=input()
#base_info={"status": "正取", "school": "第一高中"}
#user_info={"name":a, "數學":b}
#print("恭喜{school}的{name}同學，狀態 : {status}，數學分數為 : {數學}分".format(**base_info,**user_info))

#a=input()
#b=input()
#c=input()
#event_dict={"title": "AI體驗營"}
#user_dict={"name":a}
#payment_dict={"fee":b,"discount":c}
#print("【{title}】學員{name}您好，您本次的原始費用為 {fee} 元，扣除折價券 {discount} 元".format(**event_dict,**user_dict,**payment_dict))

#a= int(input())
#print("{:0>8}".format(a))

#a= input()
#print("{:-^15}".format(a))

#a = int(input())
#print("${:,}".format(a))

#a= int(input())
#print("{:X}".format(a))


# c1 = input("請輸入第1家公司名稱: ")
# m1 = int(input("請輸入第1家公司營收: "))
# c2 = input("請輸入第2家公司名稱: ")
# m2 = int(input("請輸入第2家公司營收: "))
# c3 = input("請輸入第3家公司名稱: ")
# m3 = int(input("請輸入第3家公司營收: "))
# print("--- 報表結果 ---")
# print("{:10}{:_>15,}".format(c1,m1))
# print("{:10}{:_>15,}".format(c2,m2))
# print("{:10}{:_>15,}".format(c3,m3))

# a=float(input("數字:"))
# b=int(input("寬度:"))
# c=int(input("保留小數點位數:"))
# d=input("字元填補:")
# print("{:{z}^{x}.{y}f}".format(a,x=b,y=c,z=d))

# a=float(input())
# b=float(input())
# c=float(input())
# d=float(input())
# print("|{:>7.2f} {:>7.2f}|".format(a,b))
# print("|{:>7.2f} {:>7.2f}|".format(c,d))
# print("|{:<7.2f} {:<7.2f}|".format(a,b))
# print("|{:<7.2f} {:<7.2f}|".format(c,d))

# a=input()
# b=input()
# c=input()
# d=input()
# print("|{:>10} {:>10}|".format(a,b))
# print("|{:>10} {:>10}|".format(c,d))
# print("|{:<10} {:<10}|".format(a,b))
# print("|{:<10} {:<10}|".format(c,d))

# a=input()
# b=input()
# print("玩家 %s 目前的等級是 LV.%s"%(a,b))

#a= input()
#print("[%-12s]"%(a))

#a= int(input())
#print("%06d"%a)

# import math 
# r = eval(input()) # eval 自動辨認型態是
# p=2*r*math.pi
# A= (r**2)*math.pi
# print("Radius = %.2f"%r)
# print("Perimeter = %.2f"%p)
# print("Area = %.2f"%A)

# h= eval(input())
# w= eval(input())
# p= (h+w)*2
# A= h*w
# print("Height = %.2f"%h)
# print("Width = %.2f"%w)
# print("Perimeter = %.2f"%p)
# print("Area = %.2f"%A)

# a= eval(input())
# b= eval(input())
# c= eval(input())
# d= eval(input())
# e= eval(input())
# print("%d %d %d %d %d"%(a,b,c,d,e))
# s= a+b+c+d+e
# print("Sum = %.1f"%s)
# print("Average = %.1f"%(s/5))

# x1= eval(input())
# y1= eval(input())
# x2= eval(input())
# y2= eval(input())
# print("( %s , %s )"%(x1,y1))
# print("( %s , %s )"%(x2,y2))
# print("Distance = %.4f"%(((x2-x1)**2)+((y2-y1)**2))**0.5)

# import math
# s= eval(input())
# s2=math.pow(s,2)
# T = math.tan(math.pi/5)
# print("Area = %.4f"%((5*s2)/(4*T)))

# import math
# n= eval(input())
# s= eval(input())
# print("Area = %.4f"%((n*(math.pow(s,2)))/(4*(math.tan(math.pi/n)))))

# number= eval(input())
# if number%2 ==0:
#     print("%s is an even number."%number)
# else:
#     print("%s is not an even number."%number)

# n= eval(input())
# if n%3==0 and n%5==0:
#     print("%s is a multiple of 3 and 5."%n)
# elif n%3==0:
#     print("%s is a multiple of 3."%n)
# elif n%5==0:
#     print("%s is a multiple of 5."%n)
# else:
#     print("%s is not a multiple of 3 or 5."%n)

# y= eval(input())
# if y%400==0:
#     print("%s is a leap year."%y)
# elif y%100==0:
#     print("%s is not a leap year."%y)
# elif y%4==0:
#     print("%s is a leap year."%y)
# else:
#     print("%s is not a leap year."%y)

# a= eval(input())
# b= eval(input())
# c= input()
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif c == '/':
#     if b != 0:
#         print(a / b)
#     else:
#         print("Error")
# elif c == '//':
#     print(a // b)
# elif c == '%':
#     print(a % b)

# while True:
#     a=input()
#     a=a.strip()
#     if a == "EXIT":
#         break
#     elif a.startswith("#")==True or a.startswith("//") or a.startswith("")==True:
#         print("註解或空行")
#     else:
#         print("有效程式碼")

# a=input()
# if a.startswith("https://")==False and a.startswith("ftps://")==False:
#     print("安全協定錯誤")
# elif "?" in a:
#     print("安全協定且含有查詢參數")
# else:
#     print("安全協定且無查詢參數")

# a=input()
# a=a.strip("-")
# if a.isdigit()==True:
#     print("合法整數")
# else:
#     print("不合法")

# a=input()
# X=True
# a=a.split(".")
# if len(a)!=4:
#     X=False
# else:
#     for i in a:
#         if i.isdigit()!=True:
#             X=False
#             break
#         elif i.isdigit()==True and int(i)>255:
#             X=False
#             break
# if X:
#     print("IP格式正確")
# else:
#     print("IP格式錯誤")

# letters=[]
# numbers=[]
# special=[]        
# password=input()
# for char in password:
#     if char.isalpha()and(('a'<= char <='z')or('A'<=char<='Z')):
#         letters.append(char)
#     elif '0'<= char <='9':
#         numbers.append(char)
#     else:
#         special.append(char)
# print("LETTERS:%10s"%(len(letters)))
# print("NUMBERS:%10s"%(len(numbers)))
# print("SPECIAL:%10s"%(len(special)))
        
# file = input().lower()
# F=file.split(".")
# if file.endswith((".jpg",".png",".jpeg"))!=True :
#     print("非支援的圖片格式")
# elif len(F[0]) <=5 :
#     print("合法但檔名太短")
# else:
#     print("合法且檔名長度足夠")

# p=input().lower()
# if p.endswith("?")==True:
#     if p.startswith(("why","how","what"))==True:
#         print("探究型疑問句")
#     else:
#         print("一般疑問句")
# elif p.endswith("!")==True:
#     print("強烈情感句")
# elif p.endswith(".")==True:
#     print("陳述句")
# else:
#     print("未知句型")

# a=input()
# if a.isalpha()and('a'<= a <='z')or('A'<=a<='Z'):
#     print("%s is an alphabet."%a)
# elif a.isdigit():
#     print("%s is a number."%a)
# else:
#     print("%s is a symbol."%a)

# point = eval(input())
# if 80<= point <=100:
#     print("A")
# elif 70<= point <=79:
#     print("B")
# elif 60<= point <=69:
#     print("C")
# elif  point <=59:
#     print("F")

# a=eval(input())
# if a <8000:
#     print("金額不足")
# elif 38000<=a:
#     print("%d元"%(a*0.7))
# elif 28000<=a<38000:
#     print("%d元"%(a*0.8))
# elif 18000<=a<28000:
#     print("%d元"%(a*0.9))
# else:
#     print("%d元"%(a*0.95))

# a= eval(input())
# print("{:X}".format(a))

# x2=eval(input())
# y2=eval(input())
# x1=5
# y1=6
# if ((x2-x1)**2 +(y2-y1)**2)**0.5<=15:
#     print("Inside")
# else:
#     print("Outside")

# a=eval(input())
# b=eval(input())
# c=eval(input())
# if a+b>c and b+c>a and a+c>b:
#     print(a+b+c)
# else:
#     print("Invalid")

# a=eval(input())
# b = eval(input())
# sum=0
# for i in range(a,b+1):
#     sum+=i
# print(sum)

# a=eval(input())
# b = eval(input())
# sum=0
# for i in range(a,b+1):
#     if(i%2==0):
#         sum+=i
# print(sum)

# a=int(input())
# for i in range(1,a+1):
#     for u in range(1,a+1):
#         if i>=u :
#             print("%4d"%(i*u),end=" ")
#     print()

# c=0
# a= int(input())
# for i in range(1,a+1):
#     if i % 5 == 0:
#         c+=i
# print(c)


# a=input()
# x= "".join(reversed(a))
# print(x)

# x=1
# a=int(input())
# for i  in range(1,a+1):
#     x*=i
# print(x)

# a= int(input())
# for i in range(1,a+1):
#     for u in range(1,a+1):
#         if u <=a:
#             print("%-2d%-2s%-2d%-2s%-4s"%(u,"*",i,"=",i*u),end="")
#     print()

# time=int(input())
# while time!=0:
#     a=input()
#     a="".join(a)
#     sum=0
#     for i in a:
#         sum +=int(i)
#     print("Sum of all digits of %s is %d"%(a,sum))
#     time-=1

# money=eval(input())
# y=eval(input())
# month=eval(input())
# print("Month \t Amount")
# for i in range(1,month+1):
#     money+=money*y/12/100
#     print("%3d \t %.2f"%(i,money))

# a= eval(input())
# s=0
# for i in range(1,a):
#     s+=1/(i**0.5+(i+1)**0.5)
# print("%.4f"%s)

# X=[]
# for i in range(10):
#     n=eval(input())
#     X.append(n)
# print(min(X))

# X=[]
# while True:
#     n=eval(input())
#     if n==9999:
#         break
#     X.append(n)
# print(min(X))

# X=[]
# a=eval(input())
# b=eval(input())
# for i in range(a,b+1):
#     if i %4==0 or i%9==0:
#         X.append(i)
# a=0
# for i in X:
#     if a==10:
#         print()
#     print("%-4d"%i,end="")
#     a+=1
# print()
# print("%-4d"%len(X))
# print("%-4d"%sum(X))

# while True:
#     a=eval(input())
#     if a==-9999:
#        break
#     elif 80<=a <=100:
#         print("A")
#     elif 70<=a <=79:
#         print("B")
#     elif 60<=a <=69:
#         print("C")
#     elif a <=59:
#         print("F")

# while True:
#     m=eval(input())
#     if m == -9999:
#         break
#     kg=eval(input())
#     BMI=kg/(m/100)**2
#     BMI1="%.2f"%(kg/(m/100)**2)
#     if BMI<18.5:
#         print("BMI: "+BMI1)
#         print("State: under weight")
#     elif 18.5<=BMI<25:
#         print("BMI: "+BMI1)
#         print("State: normal")
#     elif 25.0<=BMI<30:
#         print("BMI: "+BMI1)
#         print("State: over weight")
#     elif 30<=BMI:
#         print("BMI: "+BMI1)
#         print("State: fat")

# while True:
#     y= eval(input())
#     if y ==-9999:break
#     elif y%400==0:
#         print("%s is a leap year."%y)
#     elif y%100==0:
#         print("%s is not a leap year."%y)
#     elif y%4==0:
#         print("%s is a leap year."%y)
#     else:
#         print("%s is not a leap year."%y)

# Even_numbers=0
# Odd_numbers=0
# for i in range(10):
#     n=eval(input())
#     if n%2==0:
#         Even_numbers+=1
#     else:
#         Odd_numbers+=1
# print("Even numbers: %d"%Even_numbers)
# print("Odd numbers: %d"%Odd_numbers)

# Nami=0
# Chopper=0
# null=0
# for i in range(5):
#     v=eval(input())
#     if v == 1:
#         Nami+=1
#     elif v==2:
#         Chopper+=1
#     else:
#         null+=1
#     print("Total votes of No.1: %s = %d"%("Nami",Nami))
#     print("Total votes of No.2: %s = %d"%("Chopper",Chopper))
#     print("Total null votes = %d"%null)
# if Nami>Chopper:
#     print("=> No.1 Nami won the election.")
# elif Nami<Chopper:
#     print("=> No.2 Chopper won the election.")
# else:
#     print("=> No one won the election.")

# a= int(input())
# for i in range(a+1):
#     print("{:^{}}".format("*"*(2*i-1),2*a-1))

# a= int(input())
# for i in range(1,a+1):
#     print(" "*(a-i)+"*"*(2*i-1))

# def compute():
#     a=input()
#     b=input()
#     c=input()
#     print("Department: %s"%a)
#     print("Student ID: %s"%b)
#     print("Name: %s"%c)
# compute()
    
# def compute(x,y):
#     print(x*y)
# compute(eval(input()),eval(input()))

# a=eval(input())
# b = eval(input())
# def compute():
#     sum= 0
#     for i in range(a,b+1):
#         sum+=i
#     print(sum)
# compute()

# a=eval(input())
# b = eval(input())
# def compute(a,b):
#     print(a**b)
# compute(a,b)

# a=input()
# x = eval(input())
# y = eval(input())
# def compute():
#     for i in range(y):
#         for i in range(x-1):
#             print("%s "%a,end="")
#         print("%s "%a)
# compute()

# a=eval(input())
# b=eval(input())
# c=eval(input())
# def compute():
#     an1=(-b+((b**2-4*a*c)**0.5))/(2*a)
#     an2=(-b-((b**2-4*a*c)**0.5))/(2*a)
#     if an1==an2:
#         print(an1)
#     elif an1!=an2:
#         print(an1,an2)
#     else:
#         print("【Your equation has no root.】")
# compute()

# x=eval(input())
# def compute():
#     n=0
#     if x<0:
#         return False
#     for i in range(1,x+1):
#         if x%i==0:
#             n+=1
#     if n!= 2:
#         return False
#     else:
#         return True
# if compute()==True:
#     print("Prime")
# else:
#     print("Not Prime") 

# a=input()
# A=a.split(",")
# x=int(A[0])
# y=int(A[1])
# def compute(x,y):
#     D=[]
#     X=[]
#     Y=[]
#     for i in range(1,x+1):
#         if x%i==0:
#             X.append(i)
#     for u in range(1,y+1):
#         y%u==0
#         if y%u==0:
#             Y.append(u)
#     for z in X:
#         for g in Y:
#             if z==g:
#                 D.append(z)   
#     print(max(D))
# compute(x,y)

# def compute(x,y):
#     mx=max(x,y)
#     mn=min(x,y)
#     r=mx%mn
#     while r != 0:
#         mx=mn
#         mn=r
#         r=mx%mn
#     print(mn)
# x,y=map(int,input().split(","))
# compute(x,y)

# import math
# def compute(x,y):
#     return math.gcd(x,y)
# x,y=map(int,input().split(","))
# print(compute(x,y))

# import math
# a=input()
# b=input()
# x,y=map(int,a.split(","))
# m,n=map(int,b.split(","))
# q= y*n
# X=x*n
# M=m*y
# p=X+M
# def compute(p,q):
#     L=math.gcd(p,q)
#     ans="%d/%d"%((p/L),(q/L))
#     return ans 
# print("%d/%d + %d/%d = %s"%(x,y,m,n,compute(p,q)))

# def recursive_sum(n):
#     if n ==1:
#         return 1
#     return n+recursive_sum(n-1)
# print(recursive_sum(int(input())))

# def countdown(n):
#     if n==0:
#         print("發射 !")
#         return
#     print(n)
#     countdown(n-1)
# countdown(int(input()))

# def power_of_two(n):
#     if n==0:
#         return 1
#     return 2*power_of_two(n-1)
# print(power_of_two(int(input())))

# def compute(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return compute(n-2)+compute(n-1)
# a=int(input())
# for i in range(a):
#     print(compute(i),end=" ")

# def power(a,b):
#     if b==0:
#         return 1
#     return a*power(a,b-1)
# print(power(int(input()),int(input())))

# def sum_digits(n):
#     N=int(n)%10    
#     if str(N)==str(n)[0]:
#         return int(str(n)[0])
#     return N+sum_digits(int(n)//10)
# print(sum_digits(input()))    

# def reverse_string(s):
#     S=s[-1]
#     if S==s[0]:
#         return s[0]
#     return S+reverse_string(s[:-1])
# print(reverse_string(input()))

# def gcd(a,b):
#     if a%b==0:
#         return b
#     return gcd(b,a%b)
# print(gcd(int(input()),int(input())))

# X=[]
# for i in range(12):
#     a=int(input())
#     X.append(a)
# for i in range(len(X)):
#     print("%3s"%X[i], end=" ")
#     if (i + 1) % 3 == 0:
#         print()
# s=0
# for i in range(0,12,2):
#     print(i)
#     s+=int(X[i])
# print(s)

# X=[]
# for i in range(5):       
#     a= input()
#     if a =="J":
#         a=11
#     elif a =="Q":
#         a=12
#     elif a =="K":
#         a=13
#     elif a =="A":
#         a=1
#     X.append(int(a))
# print(sum(X))

# X=[]
# for i in range(10):
#     a=input()
#     X.append(a)
#     X.sort(reverse=True)
# print(X[0],X[1],X[2],end=" ")

# X=[]
# for i in range(10):
#     a=int(input())
#     X.append(a)
# U = max(X, key=X.count)
# print(U)
# print(X.count(U))

# X=[]
# for i in range(10):
#     a=eval(input())
#     X.append(a)
# X.remove(max(X))
# X.remove(min(X))
# print("%d\n%.2f"%(sum(X),sum(X)/8))

# def compute(cols,rows):
#     for i in range(cols):
#         for u in range(rows):
#             print("%4d"%(u-i),end="")
#         print()
# compute(int(input()),int(input()))
    
# A=[]
# B=[]
# C=[]
# print("The 1st student:")
# for i in range(5):
#     A.append(eval(input()))
# print("The 2nd student:")
# for i in range(5):
#     B.append(eval(input()))
# print("The 3rd student:")
# for i in range(5):
#     C.append(eval(input()))
# print("Student 1")
# print("#Sum %d\n#Average %.2f"%(sum(A),sum(A)/5))
# print("Student 2")
# print("#Sum %d\n#Average %.2f"%(sum(B),sum(B)/5))
# print("Student 3")
# print("#Sum %d\n#Average %.2f"%(sum(C),sum(C)/5))

# M=[]
# for i in range(3):
#     R=[]
#     for u in range(3):
#         R.append(eval(input()))
#     M.append(R)
# max_al=max(map(max,M))
# min_al=min(map(min,M))
# for i in range(3):
#     for j in range(3):
#         if M[i][j]==max_al:
#             Mmax=(i,j)
#         if M[i][j]==min_al:
#             Mmin=(i,j)
# print("Index of the largest number %d is: %s"%(max_al,Mmax))
# print("Index of the smallest number %d is: %s"%(min_al,Mmin))

# al=[]
# for u in range(2):
#     print("Enter matrix %d:"%(u+1))
#     mat=[]
#     for i in range(2):
#         r=[]
#         for j in range(2):
#             ij=int(input("[%d,%d]:"%((i+1),(j+1))))
#             r.append(ij)
#         mat.append(r)
#     al.append(mat)
# print("Matrix 1:")
# for i in al[0]:
#     for u in i :
#         print(u,end=" ")
#     print()
# print("Matrix 2:")
# for i in al[1]:
#     for u in i :
#         print(u,end=" ")
#     print()
# print("Sum of 2 matrices:")
# for i in range(len(al[0])):
#     for u in range(len(al[1])):
#         print(al[0][i][u]+al[1][i][u],end=" ")
#     print()

# A=[]
# alA=[]
# high=[]
# low=[]
# for i in range(4):
#     print("Week %d:"%(i+1))
#     for u in range(3):
#         A.append(input("Day %d:"%(u+1)))
#         A=list(map(float,A))
#         alA.append(sum(A))
#         high.append(max(A))
#         low.append(min(A))
#         A=[]
# print("Average: %.2f"%(sum(alA)/12))
# print("Highest: %.1f"%(max(high)))
# print("Lowest: %.1f"%(min(low)))

# L=[]
# while True:
#     a=int(input())
#     if a ==-9999:
#         break
#     else:
#         L.append(a)
#         l=len(L)
#         ma=max(L)
#         mi=min(L)
#         s=sum(L)
# a=tuple(L)
# print(a)
# print("Length: %d"%l)
# print("Max: %d"%ma)
# print("Min: %d"%mi)
# print("Sum: %d"%s)

# t1=()
# t2=()
# print("Create tuple1: ")
# while True:
#     a=eval(input())
#     if a ==-9999:
#         break
#     else:
#         t1+=(a,)
# print("Create tuple2: ")
# while True:
#     a=eval(input())
#     if a ==-9999:
#         break
#     else:
#         t2+=(a,) 
# t=t1+t2
# print("Combined tuple before sorting: ",t)
# print("Combined list after sorting: ",sorted(t))

# t=()
# while True:
#     a=input()
#     if a=="end":
#         break
#     else:
#         t+=(a, )
# print(t)
# print(t[0:3])
# print(t[-3:])
    
# N=set()
# while True:
#     a=int(input())
#     if a==-9999:
#         break
#     else:
#         N.add(a)
# print("Length: %d"%(len(N)))
# print("Max: %d"%(max(N)))
# print("Min: %d"%(min(N)))
# print("Sum: %d"%(sum(N)))

# set1=set()     
# set2=set()     
# set3=set()         
# print("Input to set1:")
# for i in range(5):
#     n=int(input())
#     set1.add(n)
# print("Input to set2:")
# for i in range(3):
#     n=int(input())
#     set2.add(n)
# print("Input to set3:")
# for i in range(9):
#     n=int(input())
#     set3.add(n)

# print("set2 is subset of set1:",str(set2.issubset(set1)))
# print("set3 is superset of set1:",str(set3.issuperset(set1)))

# k=int(input())
# for i in range(k):
#     a=input().lower()
#     A=set(a)
#     al=("abcdefghijklmnopqrstuvwxyz")
#     print(str(A.issuperset(al)))

# 弟弟的解答
# a=int(input())
# b=input()
# z=[]
# for i in range(0,len(b)):
#     for u in b[i]:
#         if u in "abcdefghijklmnopqrstuvwxyz":
#             z.append("0")
#         else:
#             z.append("1")
# Z=""
# for i in z:
#     Z+=i
# t = Z[0]
# n=[]
# for i in range(1, len(Z)):
#     if Z[i] == Z[i-1]:
#         t += Z[i]
#     else:
#         n.append(t)
#         t = Z[i]
# n.append(t)
# #print(n)
# L=[]
# for i in n:
#     L.append(len(i))
# #print(L)
# m_blocks = 0  
# c_blocks = 0 
# for l in L:
#     if l == a:
#         c_blocks += 1
#         if c_blocks > m_blocks:
#             m_blocks = c_blocks
#     elif l > a:
#         if c_blocks + 1 > m_blocks:
#             m_blocks = c_blocks + 1
#         c_blocks = 1
#         if c_blocks > m_blocks:
#             m_blocks = c_blocks
#     else:
#         c_blocks = 0
# print(m_blocks * a)

# X=[]
# Y=[]
# print("Enter group X's subjects:")
# while True:
#     a=input()
#     if a=="end":
#         break
#     else:
#         X.append(a)
# print("Enter group Y's subjects:")
# while True:
#     a=input()
#     if a=="end":
#         break
#     else:
#         Y.append(a)
# al=sorted(list(set(X+Y)))
# print(al)
# sam=[]
# for i in X:
#     for u in Y:
#         if i==u:
#             sam.append(i)
# print(sorted(sam))
# for i in sam:
#     for u in Y:
#         if i==u:
#             Y.remove(i)
# print(sorted(Y))
# for i in sam:
#     for u in X:
#         if i==u:
#             X.remove(i)
# print(sorted(X+Y))


# c=[5]
# d=c # 列表會共用空間而非複製
# d=c.copy() # 所以需要用.copy()才能複製空間，否則依然會動到c
# d[0]=6
# print(c)
     
# dict1={}
# dict2={}
# print("Create dict1:")
# while True:
#     K=input("Key:")
#     if K =="end":
#         break
#     else:
#         V=input("Value:")
#         dict1[K]=V
# print("Create dict2:")
# while True:
#     K=input("Key:")
#     if K =="end":
#         break
#     else:
#         V=input("Value:")
#         dict2[K]=V
# D=dict1|dict2
# for i in sorted(D):
#     print(i,":",D[i])

# D={}
# while True:
#     K= input("Key: ")
#     if K=="end":
#         break
#     else:
#         V=input("Value: ")
#         D[K]=V
# for i in sorted(D):
#     print(i,":",D[i])

# D={}
# while True:
#     K= input("Key: ")
#     if K=="end":
#         break
#     else:
#         V=input("Value: ")
#         D[K]=V
# SK=input("Search key: ")
# if SK in D:
#     print("True")
# else:
#     print("False")

# a=input()
# for i in range(len(a)):
#     print("Index of '%s': %s"%(a[i],i))
# print()
# for i in range(len(a)):
#     print("Index of \'"+a[i]+"\': "+str(i))

# i=input()
# print( ord(i)-ord("A"))

# i = input()
# print(chr((ord(i)+32)))

# a=input()
# s=0
# for i in a:
#     s+=ord(i)
# print(s)

# a=input()
# n= int(input())
# X=""
# for i in a:
#     nuber=ord(i)+n
#     if nuber>90:
#         nuber=nuber-91+65
#         X+=chr(nuber)
#     else:
#         X+=chr(nuber)
# print(X)
        
# a=input()
# X=""
# for i in range(len(a)):
#     if i==0:
#         if ord(a[0])>90:
#             X+=chr(ord(a[0])-32)
#         else:
#             X+=a[0]
#     elif a[i]==" ":
#         X+=a[i]
#         if ord(a[i+1])>90:
#             X+=chr(ord(a[i+1])-32)
#         else:
#             X+=a[i+1]
#     elif a[i-1]!=" ":
#         if 90>=ord(a[i]):
#             X+=chr(ord(a[i])+32)
#         else:
#             X+=a[i]  
# print(X)

# a=input()
# z=input()
# X=[]
# for u in range(ord(a),ord(z)+1):
#     for i in range(1,4):
#         X.append(chr(u)+str(i))
# print(", ".join(X))

# a=input()
# X=[]
# for i in a:
#     print("ASCII code for '%s' is %d"%(i,ord(i)))
#     X.append(ord(i))
# print(sum(X))

# a=input()
# a=a.split(" ")
# u=a[-3:]
# for i in u:
#     print(i,end=" ")

# a=input()
# print(a.upper())
# print(a.title())

# a= input()
# print("|%-10s|"%(a))
# print("|{:^10}|".format(a))
# print("|%10s|"%(a))

# a=input()
# n=input()
# def compute(a,n):
#     T=0
#     for i in a:
#         if i==n:
#             T+=1
#     return T
# print("%s occurs %d time(s)"%(n,compute(a,n)))

# a= input()
# a=a.split()
# s=0
# for i in a:
#     print(i)
#     if i[0]=="-":
#         s-=int(i[1:])
#     else:
#         s+=eval(i)
# print("Total = %d"%s)
# print("Average = %.1f"%(s/5))

# C=input()
# C1=C.replace("\\", "/")
# C2=C1.replace("//","/")
# print(C2)

# a=input()
# kw=input().split(",")
# for i in kw:
#     a=a.replace(i,len(i)*"*")
# print(a)

# a=input().split("-")
# if len(a)!=3:
#     print("Invalid SSN")
# elif len(a[0])!=3 :
#     print("Invalid SSN")
# elif len(a[1])!=2 :
#     print("Invalid SSN")
# elif len(a[2])!=4 :
#     print("Invalid SSN")
# elif len(a)==3:
#     try:
#         a=list(map(int, a))
#     except ValueError:
#         print("Invalid SSN")
# else:
#     print("Valid SSN")

# T=0
# a=input().split(" ")
# for i in a:
#     if i.isupper()==True:
#         T+=1
# print(T)

# password=input()
# re=True
# E=[]
# if len(password)<8:
#     re=False
# if re == True :
#     for i in password:
#         if "a"<=i<="z" or "A"<=i<="Z":
#             E.append(i)
#             password=password.replace(i,"")
# Et=0
# if password.isdigit()==True:
#     for i in E:
#         if "A"<=i<="Z":
#             Et+=1
# if Et>=1 :
#     print("Valid password")
# else:
#     print("Invalid password")

# T=int(input())
# for i in range(T):
#     a=input().split(" ")
#     a=list(map(eval,a))
#     print("%.2f"%(max(a)-min(a)))
         
# f=open("squares.txt","w",encoding="utf-8")
# a=int(input())
# for i in range(1,a+1):
#     f.write("%d:%d\n"%(i,i*i)) 
# f.close()

# a=input().upper()
# b=input().upper()
# c=input().upper()
# f=open("words.txt","w",encoding="utf-8")
# f.write(a+"\n")
# f.write(b+"\n")
# f.write(c)
# f.close()

# f=open("expenses.txt","w",encoding="utf-8")
# f.close()
# S=[]
# while True:
#     a=input()
#     if a!="q" and a!="Q":
#         f=open("expenses.txt","a",encoding="utf-8")
#         f.write(a+"\n")
#         f.close()
#         N_a=a.split(" ")
#         S.append(int(N_a[1]))
#     else:
#         print("Total Expenses: %d"%(sum(S)))
#         break

# f=open("server.log","w",encoding="utf-8")
# f.close()
# T=0
# while True:
#     a=input()
#     if a!="STOP":
#         T+=1
#         f=open("server.log","a",encoding="utf-8")
#         f.write(a+"\n")
#         f.close()
#         l_a=a.lower()
#         N_a=l_a.split(" ")
#         if "error" in N_a: 
#             f=open("server.log","a",encoding="utf-8")
#             f.write("[ALERT] Immediate attention required!\n")
#             f.close()
#             T+=1
#     else:
#         print("Logging stopped.")
#         print("Total new lines appended: %d"%(T))

# f=open("score.txt","r")
# a=f.readlines()
# for i in a:
#     I=i.split(" ")
#     if int(I[1])<60:
#         print(I[0])
# f.close()

# f=open("access.log","r")
# a=f.readlines()
# EC=0
# C=0
# A={}
# for i in a:
#     i=i.strip()
#     I=i.split(" ")
#     print(I)
#     A[I[1]]=A.get(I[1], 0) + 1
#     if I[-1]=="404" or I[-1]=="500":
#         EC+=1
# print("Error count: %d"%(EC))
# print("Most frequent IP:%s (%d times)"%(max(A,key=A.get),A[max(A,key=A.get)]))
# f.close()

# f=open("students.txt","r")
# a=f.readlines()
# A={}
# for i in a:
#     I=i.split(" ")
#     P=[]
#     P.append(int(I[1]))
#     P.append(int(I[2]))
#     P.append(int(I[3]))
#     A[sum(P)]=I[0]
# X=sorted(A,reverse=True)
# x=0
# for u in X:
#     x+=1
#     print("%d. %s - %d"%(x,A[u],u))
# f.close()

# prices = [100,200,150,80,120]
# N_p=[]
# for i,p in enumerate(prices,start=1):
#     if i%2==0:
#         p=p/2
#         print("第 %d 件商品 ( 半價 ) : %s 元"%(i,p))
#         N_p.append(p)
#     else:
#         print("第 %d 件商品 : %s 元"%(i,p))
#         N_p.append(p)
# print("總金額 : %s"%sum(N_p))

# board = [
#     ["O", "X", "O"],
#     ["X", "O", "X"],
#     ["O", "X", "O"]
# ]
# for row,R in enumerate(board):
#     for col,C in enumerate(R):
#         if C=="X":
#             print("Found 'X' at Row %d, Col %d"%(row,col))

# lines = ["python is fun", "i love python", "java is okay", "python generator"]
# search_index={}
# time=[]
# for T,i in enumerate(lines,start=1):
#     if "python" in i:
#         time.append(T)
# search_index["python"]=time
# print(search_index)

# f=open("test.log","r",encoding="utf-8")
# a=f.readlines()
# new_lines = []
# for T,i in enumerate(a,start=1):
#     if "ERROR" in i:
#         new_lines.append("[CRITICAL - Line %d]"%T)
#     new_lines.append(i)
# f=open("test.log", "w", encoding="utf-8") 
# f.writelines(new_lines)
# f.close()

# f=open("students.txt","r+",encoding="utf-8")
# a = f.readlines()
# f.seek(0)
# for i,u in enumerate(a,start=1):
#     f.write("%s. %s"%(i,u))
# f.close()

# f=open("data.txt","r+",encoding="utf-8")
# a=f.read()
# f.seek(0)
# n_a = a.replace("舊","新")
# f.write(n_a)
# f.close()

# n=input()
# f=open("comment.txt","r+",encoding="utf-8")
# a=f.read()
# f.seek(0)
# n_a=a.replace(n,len(n)*"*")
# f.write(n_a)
# f=open("comment.txt","r",encoding="utf-8")
# x=f.read()
# print("=== Updated Content ===")
# print(x)
# f.close()

# n=input().split(" ")
# f=open("config.txt","r+",encoding="utf-8")
# a=f.readlines()
# Al={}
# for i in a:
#     i=i.split("=")
#     Al[i[0]]=i[1]
# Al[n[0]]=str(n[1])+"\n"
# f.seek(0)
# for i in Al:
#     f.write(str(i)+"="+str(Al[i]))
#     print((str(i)+"="+str(Al[i])).strip("\n"))
# f.close()

# with open("status.log","w+",encoding="utf-8") as f:
#     for i in range(3):
#         a=input()
#         f.write(a+"\n")
#     f.seek(0)
#     print(f.read())

# with open("matrix.txt","w+",encoding="utf-8") as f:
#     for i in range(2):
#         a=input()
#         f.write(a+"\n")
#     f.seek(0)
#     A=f.readlines()
#     x=0
#     for i in A:
#         i=i.split(" ")
#         u=list(map(int,i))
#         x+=sum(u)
#     print(x)
    
# with open("num_square.txt","w+",encoding="utf-8") as f:
#     s=[]
#     for i in range(3):
#         a=int(input())
#         A=a*a
#         f.write(str(A)+"\n")
#         s.append(A)
#     print("平方數列 : ",s)
#     print("總和 : %d"%sum(s))

# with open("names2.txt","w+",encoding="utf-8") as f:
#     for i in range(5):
#         a=input()
#         f.write(a+"\n")
#     f.seek(0)
#     a=f.readlines()
#     A=[]
#     for i in sorted(a):
#         A.append(i.strip())
#     print(A)

# with open("matrix.dat","w+",encoding="utf-8") as f:
#     a=int(input())
#     for i in range(a):
#         a=int(input())
#         f.write(str(a)+"\n")
#     f.seek(0)
#     c=f.read()
#     f.seek(0)
#     A=f.readlines()
#     s=[]
#     for i in A:
#         i=int(i.strip())
#         s.append(i)
#     x="[HEADER] MAX:%d, MIN:%d"%(max(s),min(s))
#     print(x)
#     f.seek(0)
#     f.write(x)
#     f.write("\n")
#     f.write(c)

# with open("grade.txt","a+",encoding="utf-8") as f:
#     a=input()
#     b=input()
#     f.write(a+" "+b+"\n")
#     f.seek(0)
#     lines=f.readlines()
#     point=[]
#     for i in lines:
#         i=i.split(" ")
#         point.append(i[1].strip())
#     point=list(map(eval,point))
#     print("目前共 %d 筆成績"%(len(lines)))
#     print("成績列表 : ",point)
#     print("平均成績 : %.2f"%(sum(point)/len(lines)))

# with open("numbers.txt","a+",encoding="utf-8") as f:
#     a=input()
#     f.write(a+"\n")
#     f.seek(0)
#     lines=f.readlines()
#     al=[]
#     for i in lines:
#         al.append(eval(i.strip()))
#     print("Average: %.2f"%(sum(al)/len(lines)))

# with open("shopping_list.txt","a+",encoding="utf-8") as f:
#     while True:
#         SP=input()
#         if SP=="done":
#             break
#         else:
#             f.write(SP+"\n")
#     f.seek(0)
#     lines=f.readlines()
#     print("購物清單共%d項"%len(lines))
#     for i,food in enumerate(lines,start=1):
#         print("%d.%s"%(i,food.strip()))

# with open("chat.log","a+",encoding="utf-8") as f:
#     while True:
#         inter=input()
#         if inter=="END":
#             break
#         else:
#             f.write("[User]: "+inter+"\n")
#     keyword=input()
#     f.seek(0)
#     a=f.readlines()
#     T=0
#     for i in a:
#         if keyword in i:
#             T+=1
#     print("Tatal matching lines in history: %d"%T)

# with open("inventory.log","a+",encoding="utf-8") as f:
#     while True:
#         f.write(input()+"\n")
#         f.seek(0)
#         a=f.readlines()
#         al=0
#         for i in a:
#             al+=int(i.strip())
#         if  al <0:
#             print("[Warning] Stock deficit!")
#             break
#         else:
#             print("Current Stock: %d"%al)

# with open("write.txt","a+",encoding="utf-8") as f:
#     for i in range(5):
#         f.write(input()+"\n")

# with open("read.txt","r",encoding="utf-8") as f:
#     al=0
#     a=f.readlines()
#     for i in a:
#         i=i.split(" ")
#         for i in i:
#             al+=int(i.strip())
#     print(al)

with open("data.txt","a+",encoding="utf-8") as f:
    for i in range(5):
        f.write(input()+"\n")
    print("Append completed!\nContent of \"data.txt\":")
    f.seek(0)
    print(f.read())



