print("Hello Dear user,\n \t\t Welcome to \"Roots Of Quardatic Equation\" aka ROQE ")
def F_QUAR(num,var):                 # defination for printing the equation so that it represent sign and numbers for each case
    if num == 0:                                                        
        return ("") # done for all
    if num > 0:
        if num == 1:   # x²
            if len(var) == 2:
                return (f"{var}")
            if len(var) == 1:
                if a == 0:
                    return (f"{var}")
                else:
                    return (f" + {var}")
            if len(var) == 0:
                return (f" + {num}")
        else:
            if len(var) == 2:
                return (f"{num}{var}")
            if len(var) == 1:
                if a == 0:
                    return (f"{num}{var}")
                else:
                    return (f" + {num}{var}")
            if len(var) == 0:
                return (f" + {num}{var}")
   
    if num < 0:
        if num == -1:
            if len(var) == 2:
                return (f"-{var}")

            if len(var) == 1:
                return (f" -{var}")

            if len(var) == 0:
                return (f" {num}")
        else:
            if len(var) == 2:
                return (f"{num}{var}")

            if len(var) <= 1:
                return (f" {num}{var}")
def F_LINE(num,var):
    if num > 0:
        if num == 1:
            if len(var) == 1:
                return (f"{var}")
            if len(var) == 0:
                return (f" + {num}")
        else:
            if len(var) == 1:
                return (f"{num}{var}")
            if len(var) == 0:
                return (f" + {num}")
    if num < 0:
        if num == -1:
            if len(var) == 1:
                return (f"-{var}")
            if len(var) == 0:
                return (f" {num}")
        else:
            if len(var) == 1:
                return (f"{num}{var}")
            if len(var) <= 0:
                return (f" {num}")
def F_NONE(num):
    return (f"{num}")
def isnum(num):
    try:
        if "." in str(num):
            if (int(str(num).split(".")[1])) == 0:
                return True
            else:
                return False
        else:
            int(num)
            return True
    except ValueError:
        return False
def notfloat(num):
    return (int(str(num).split(".")[0]))
def ran(num):                        # creating range for all a,b1,b2,c to find thier factor in for loop
    num = int(num)
    if num < 0:
        return (num*-1)+1     
    else:
        return num+1
def factor(num):
    factor_num = []
    if isnum(num) == False:
        n = len(str(num).split(".")[1])
        num10 = num*(pow(10,n))
        num = int(num10)

    for i in range(1,ran(num)):
        if num%i == 0:
            factor_num.append(-i)
            factor_num.append(i)
    return factor_num
def com_factor(fac_1,fac_2):
    j = -1
    while j >= -(len(fac_1)):
        k = -1
        while k >= -(len(fac_2)):
            if fac_1[j] == fac_2[k]:
                return (fac_1[j])
            k -= 1
        j -= 1
def factor_all(fac_1,fac_2,fac_3):
    j = -1
    while j >= -(len(fac_1)):
        k = -1
        while k >= -(len(fac_2)):
            l = -1
            while l >= -(len(fac_3)): 
                if fac_1[j] == fac_2[k] == fac_3[l]:
                    return (fac_1[j])
                l -= 1
            k -= 1
        j -= 1
def perfect_sq(num):
    p_sq = []
    for i in range(2,ran(num)):
        j = pow(i,0.5)
        if j.is_integer() == True:
            p_sq.append(i)
    return p_sq
def squareroot(num):
    if (type(num)) == int:
        root_num = num**0.5
        if num == 1:
            return (f"{num}")
        elif num in perfect_sq(num):
            root_num = int(root_num)
            return (f"{root_num}")
        else:
            num_b = num
            num_c = 1
            for i in range (-1,-ran(len(perfect_sq(num))),-1):
                f1 = perfect_sq(num)[i]
                if f1 in factor(num_b):
                    num_b /= f1
                    num_c *= pow((f1),0.5)
            num_c = int(num_c)
            num_b = int(num_b)
            if num_c == 1:
                return (f"√({num_b})")
            else:
                return (f"{num_c}√({num_b})")
    if (type(num)) == float:
        root_num = num**0.5
        n = len(str(num).split(".")[1])
        num10 = num*(pow(10,n))
        num10 = int(num10)
        if num == 1 and n%2 == 0:
            return (f"{root_num}")
        elif num10 in perfect_sq(num10) and n%2 == 0:
            return (f"{root_num}")
        else:
            num_b = num10
            num_c = 1
            for i in range (-1,-ran(len(perfect_sq(num10))),-1):
                f1 = perfect_sq(num10)[i]
                if f1 in factor(num_b):
                    num_b /= f1
                    c = pow((f1),0.5)
                    num_c *= c
            num_c = int(num_c)
            num_b = num_b/(pow(10,n))
            if num_c == 1:
                return (f"√({num_b})")
            else:
                return (f"{num_c}√({num_b})")
def floatcheck(num1,num2,num3):
    global a, b, c
    if isnum(num1) == True:
        if "." in num1:
            if (int(str(num1).split(".")[1])) == 0:
                a  = notfloat(num1)
        else:
            a = int(num1)
    else:
        a = float(num1)
    if isnum(num2) == True:
        if "." in num2:
            if (int(str(num2).split(".")[1])) == 0:
                b  = notfloat(num2)
        else:
            b = int(num2)
    else:
        b = float(num2)
    if isnum(num3) == True:
        if "." in num3:
            if (int(str(num3).split(".")[1])) == 0:
                c  = notfloat(num3)
        else:
            c = int(num3)
    else:
        c = float(num3)
def max(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num3:
        return num2
    else:
        return num3
def convert(num1,num2,num3):
    global a, b, c
    if float in [type(num1), type(num2), type(num3)]:
        f_a = 0
        f_b = 0
        f_c = 0
        if type(num1) == float:
            f_a = len(str(num1).split(".")[1])
        if type(num2) == float:
            f_b = len(str(num2).split(".")[1])
        if type(num3) == float:
            f_c = len(str(num3).split(".")[1])
        f_abc = pow(10,max(f_a,f_b,f_c))
        
        if f_abc != 0:
            a *= f_abc
            b *= f_abc
            c *= f_abc
        a = int(a)
        b = int(b)
        c = int(c)
        print (F_QUAR(a,"x²") + F_QUAR(b,"x") + F_QUAR(c,"") + " = 0\n")
def ter(num):
    count = 0
    for i in range (len(factor(num))):
        j = factor(num)[i]
        if j%5 == 0 or j%2 == 0 or j == 1 or j == -1:
            count = count
        else:
            count += 1
    if count >= 1:
        return False
    else:
        return True
def frac(num1,num2):
    div = num1/num2
    if isnum(div) == False:
        if ter(num2) == True:
            return [div,1]
        else:
            com_a_b = com_factor(factor(num1), factor(num2)) 
            if com_a_b > 1:
                num1 /= com_a_b
                num2 /= com_a_b
            num1 = int(num1)
            num2 = int(num2)
            return [num1,num2]
    else:
        return [int(div),1]
def pfrac(frac_list):
    if frac_list[1] == 1:
        return frac_list[0]
    else:
        return (f"{frac_list[0]}/{frac_list[1]}")
def frac_sq(frac_list):
    n1 = frac_list[0]
    d1 = frac_list[1]
    root_n1 = n1**0.5
    root_d1 = d1**0.5
    if d1 in perfect_sq(d1):
        if n1 in perfect_sq(n1):
            return [int(root_n1),int(root_d1),1,1,0]
        else:
            n1_b = n1
            n1_c = 1
            for i in range (-1,-ran(len(perfect_sq(n1))),-1):
                f1 = perfect_sq(n1)[i]
                if f1 in factor(n1_b):
                    n1_b /= f1
                    n1_c *= pow((f1),0.5)
            return [int(n1_b),1,int(n1_c),int(root_d1)]
    else:
        if n1 in perfect_sq(n1):
            d1_b = d1
            d1_c = 1
            for i in range (-1,-ran(len(perfect_sq(d1))),-1):
                f1 = perfect_sq(d1)[i]
                if f1 in factor(d1_b):
                    d1_b /= f1
                    d1_c *= pow((f1),0.5)
            return [1,int(d1_b),int(root_n1),int(d1_c)]
        else:
            n1_b = n1
            n1_c = 1
            d1_b = d1
            d1_c = 1
            for i in range (-1,-ran(len(perfect_sq(n1))),-1):
                f1 = perfect_sq(n1)[i]
                if f1 in factor(n1_b):
                    n1_b /= f1
                    n1_c *= pow((f1),0.5)
            for i in range (-1,-ran(len(perfect_sq(d1))),-1):
                f1 = perfect_sq(d1)[i]
                if f1 in factor(d1_b):
                    d1_b /= f1
                    d1_c *= pow((f1),0.5)
            return [int(n1_b),int(d1_b),int(n1_c),int(d1_c)]
def pfrac_sq(frac):
    if len(frac) == 4:
        if frac[2] == 1 and frac[3] == 1:
            return (f"√({frac[0]}/{frac[1]})")

        elif frac[3] == 1:
            return (f"{frac[2]} √({frac[0]}/{frac[1]})")

        elif frac[3] != 1:
            if frac[1] == 1:
                return (f"{frac[2]}/{frac[3]} √({frac[0]})")
            else:
                return (f"{frac[2]}/{frac[3]} √({frac[0]}/{frac[1]})")
    else:
        return (f"{frac[0]}/{frac[1]}")
def D_sq(num):
    num_b = num
    num_c = 1
    for i in range (-1,-ran(len(perfect_sq(num))),-1):
        f1 = perfect_sq(num)[i]
        if f1 in factor(num_b):
            num_b /= f1
            num_c *= pow((f1),0.5)
    num_c = int(num_c)
    num_b = int(num_b)
    return [num_c,num_b]
def p_D_sq(Dlist):
    if Dlist[1] == 1:
        return (Dlist[0])
    else:
        if Dlist[0] == 1:
            return (f"√({Dlist[1]})")
        else:
            return (f"{Dlist[0]} √({Dlist[1]})")
def answer_roots(num1,num2):
    print("The roots of the given equation is :")
    print(f"x = {num1}")
    print(f"x = {num2}\n")
    if num1 == num2:
        print("NATURE OF ROOTS ARE REAL AND EQUAL")
    else:
        print("NATURE OF ROOTS ARE REAL AND NOT EQUAL")
def answer_roots_1(num1):
    print("The roots of the given equation is :")
    print(f"x = {num1}\n")
    print("Since the given is is linear not quardatic")
    print("NATURE OF ROOT IS REAL")

while True:    # made a loop so that it can be repeat after it

    a = str(input("Enter the cofficient of x² :"))
    b = str(input("Enter the cofficient of x :"))
    c = str(input("Enter the constant :"))

    if ('0' == a and '0' == b):         # special case when a=0, b=0, c=?
        print("\nThe given equation does not have a variable please input the value correctly")
        continue
    floatcheck(a,b,c)
    print (F_QUAR(a,"x²") + F_QUAR(b,"x") + F_QUAR(c,"") + " = 0")

    # choice = input("Is this the equation you want to choose? (y/n): \n").lower()
    choice = 'y'
    if choice == "n" :
        continue
    if choice == "y" :
        convert(a,b,c)
        if (pow(b,2) - 4*a*c) < 0:
            print("Roots are not real, since D is smaller than 0. \n")

            choice_2 = input("Do you want to find an another one? (y/n): ")
        
            if choice_2 == "y":
                continue
            if choice_2 == "n":
                break
            else:
                print("Invalid Input")
                break
        else:
            if (c == 0):
                print (F_QUAR(a,"x²") + F_QUAR(b,"x") + " = 0\n")

                if a < 0:                          # if the equation starts with -ive then change all signs
                    a *= -1
                    b *= -1
                    c *= -1
                    print (F_QUAR(a,"x²") + F_QUAR(b,"x") + F_QUAR(c,"") + " = 0\n")

                if (b == 0): # 3x² = 0      when c=0 and b=0
                    if a != 1:
                        print(F_QUAR(1,"x²") + " = 0\n")

                    r1 = 0
                    r2 = 0
                    answer_roots(r1,r2)

                    choice_2 = input("Do you want to find an another one? (y/n): ")
                    choice_2 = choice_2.lower()
                    if choice_2 == "y":
                        continue
                    if choice_2 == "n":
                        break
                    else:
                        print("Invalid Input")
                        break

                if (a == 0): # 12x = 0      wheh c=0 and a=0

                    if b < 0:                          # if the equation starts with -ive then change all signs
                        b *= -1
                        c *= -1
                        print (F_QUAR(a,"x²") + F_QUAR(b,"x") + F_QUAR(c,"") + " = 0\n")

                    if b != 1:
                        print(F_LINE(1,"x") + " = 0\n")

                    r = 0
                    answer_roots_1(r)

                    choice_2 = input("Do you want to find an another one? (y/n): ")
                    choice_2 = choice_2.lower()
                    if choice_2 == "y":
                        continue
                    if choice_2 == "n":
                        break
                    else:
                        print("Invalid Input")
                        break

                else:        # 3x² + 12x = 0     

                    # isfloat

                    com_2_a_b = com_factor(factor(a),factor(b))
                    if com_2_a_b > 1:
                        a = int(a/ com_2_a_b)
                        b = int(b/ com_2_a_b)
    
                        print (F_QUAR(a,"x²") + F_QUAR(b,"x") + F_QUAR(c,"") + " = 0\n")

                    print("(" + F_LINE(1,"x") + ")" + "(" + F_LINE(a,"x") + F_LINE(b,"") + ")" + " = 0\n")

                    r1 = 0
                    r2 = -(pfrac(frac(b,a)))
                    answer_roots(r1,r2)

                    choice_2 = input("Do you want to find an another one? (y/n): ")
                    choice_2 = choice_2.lower()
                    if choice_2 == "y":
                        continue
                    if choice_2 == "n":
                        break
                    else:
                        print("Invalid Input")
                        break
            
            if (b == 0):     # 4x² -1 = 0
                print (F_QUAR(a,"x²") + F_QUAR(c,"") + " = 0\n")

                if a < 0:                          # if the equation starts with -ive then change all signs
                    a *= -1
                    c *= -1
                    print (F_QUAR(a,"x²") + F_QUAR(b,"x") + F_QUAR(c,"") + " = 0\n")

                com_2_a_c = com_factor(factor(a),factor(c))
                if com_2_a_c > 1:
                    a = int(a/com_2_a_c)
                    c = int(c/com_2_a_c)
                    print (F_QUAR(a,"x²") + F_QUAR(b,"x") + F_QUAR(c,"") + " = 0\n")

                c *= -1
                print(F_QUAR(a,"x²") + " = " + F_NONE(c) + "\n") # 4x² = 1
     
                if a > 1:
                    cc = frac(c,a)
                    c = pfrac(cc)
                    a = 1
                    print(F_QUAR(a,"x²") + " = " + F_NONE(c) + "\n") # x² = 0.25 --   x² = 121/4

                print(F_LINE(a,"x") + " = " + "√" + "(" + F_NONE(c) + ")\n") # x = √(0.25) --   x = √(121/4)
                if type(c) != str:
                    c = squareroot(c)
                else:
                    c = pfrac_sq(frac_sq(cc))

                print(F_LINE(a,"x") + " = " + "± " + F_NONE(c) + "\n") #x = ±0.5
                r1 = c
                r2 = (f"-{c}")
                answer_roots(r1,r2)

                choice_2 = input("Do you want to find an another one? (y/n): ")
                choice_2 = choice_2.lower()
                if choice_2 == "y":
                    continue
                if choice_2 == "n":
                    break
                else:
                    print("Invalid Input")
                    break
    
            if (a == 0):     # 5x -10 = 0

                print (F_QUAR(a,"x²") + F_QUAR(b,"x") + F_QUAR(c,"") + " = 0\n")  # 5x = 10
                com_2_b_c = com_factor(factor(b),factor(c))

                if com_2_b_c > 1:
                    b = int(b/com_2_b_c)
                    c = int(c/com_2_b_c)
                    print (F_QUAR(a,"x²") + F_QUAR(b,"x") + F_QUAR(c,"") + " = 0\n")  
                              
                c *= -1
                print(F_LINE(b,"x") + " = " + F_LINE(c,"") + "\n") # x = 2

                r = c
                answer_roots_1(r)

                choice_2 = input("Do you want to find an another one? (y/n): ")
                choice_2 = choice_2.lower()
                if choice_2 == "y":
                    continue
                if choice_2 == "n":
                    break
                else:
                    print("Invalid Input")
                    break

            if ((a!=0) and (b!=0) and (c!=0)):
                print (F_QUAR(a,"x²") + F_QUAR(b,"x") + F_QUAR(c,"") + " = 0\n")

                if a < 0:                          # if the equation starts with -ive then change all signs
                    a *= -1
                    b *= -1
                    c *= -1
                    print (F_QUAR(a,"x²") + F_QUAR(b,"x") + F_QUAR(c,"") + " = 0\n")

                com_3 = factor_all(factor(a),factor(b),factor(c))

                if com_3 > 1:
                    a = int(a/com_3)
                    b = int(b/com_3)
                    c = int(c/com_3)
                    print (F_QUAR(a,"x²") + F_QUAR(b,"x") + F_QUAR(c,"") + " = 0\n")
#-------------------------------------------------------------------------------------------------------------------------------------------
                b1 = 0
                b2 = 0
                for j in range (len(factor(a*c))):    # find the common factors of ac whose sum is equals to b
                    for k in range (len(factor(a*c))):
                        if ((factor(a*c)[j] + factor(a*c)[k]) == b) and (factor(a*c)[j]*factor(a*c)[k]==a*c):
                            b1 = factor(a*c)[j]
                            b2 = factor(a*c)[k]
                            break  
#------------------------------------------------------------------------------------------------------------------------------------------

                if b1 == 0: # for fraction 
                    D = b**2 - 4*a*c
                    print("Using Discriment formula\n")

                    print(f"x = [-b + √(D)]/ 2*a\n")
                    print(f"x = [-({b}) + √({D})]/ 2*{a}\n")
                    a *= 2
                    b *= -1

                    print(f"x = [{b} ± {p_D_sq(D_sq(D))}]/{a}\n")
                    com_a_b_D = factor_all(factor(a),factor(b),factor(D_sq(D)[0]))

                    if com_a_b_D > 1:
                        a = int(a/com_a_b_D)
                        b = int(b/com_a_b_D)
                        D = int(D/(com_a_b_D**2))
                    D = p_D_sq(D_sq(D))
                    if a == 1:
                        print(f"x = {b} ± {D}\n")
                        if type(D) == int:
                            r1 = (f"{b + D}")
                            r2 = (f"{b - D}")
                        else:
                            r1 = (f"{b} + {D}")
                            r2 = (f"{b} - {D}")

                    else:
                        print(f"x = [{b} ± {D}]/{a}\n")
                        if type(D) != int:
                            r1 = (f"[{b} + {D}]/{a}")
                            r2 = (f"[{b} - {D}]/{a}") 
                        else:
                            D1 = b - D
                            D2 = b + D

                            r1 = (f"{D1}/{a}")
                            r2 = (f"{D2}/{a}")
                            print(f"x = {r1}")
                            print(f"x = {r2}\n")

                            if com_factor(factor(D1),factor(a)) > 1:
                                r1 = pfrac(frac(D1,a))
                            if com_factor(factor(D2),factor(a)) > 1:
                                r2 = pfrac(frac(D2,a))

                    answer_roots(r1,r2)

                    choice_2 = input("Do you want to find an another one? (y/n): ")
                    choice_2 = choice_2.lower()
                    if choice_2 == "y":
                        continue
                    if choice_2 == "n":
                        break
                    else:
                        print("Invalid Input")
                        break

                print (F_QUAR(a,"x²") + F_QUAR(b1,"x") + F_QUAR(b2,"x") + F_QUAR(c,"") + " = 0\n")

                v2 = com_factor(factor(a),factor(b1))
                c2 = com_factor(factor(c),factor(b2))

                if b2 < 0:
                    c2 *= -1

                v1 = int(a/v2)
                c1 = int(c/c2)

                brac_1 = ("(" + F_LINE(v1,"x") + F_LINE(c1,"") + ")")
                brac_2 = ("(" + F_LINE(v2,"x") + F_LINE(c2,"") + ")")

                print(F_LINE(v2,"x") + brac_1 + F_LINE(c2,"") + brac_1 + " = 0\n")

                print(brac_1 + brac_2 + " = 0\n")

                r1 = -(pfrac(frac(c1,v1)))
                r2 = -(pfrac(frac(c2,v2)))
                answer_roots(r1,r2)

                choice_2 = input("Do you want to find an another one? (y/n): ")
                choice_2 = choice_2.lower()
                if choice_2 == "y":
                    continue
                if choice_2 == "n":
                    break
                else:
                    print("Invalid Input")
                    break
    else:
        print("Invalid Input")
        continue
bye = input("\nThank you foor using ROQE 1.5\n©Copyright VK_BRAWLER aka VARUN KHARKWAL\nEnter any key to exit")

