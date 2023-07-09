aid = ['admin']  # admin id
apword = ['00_00']  # admin password
rid = ['mjcash']  # receptionist id
rpword = ['b_ill']  # receptionist password
kid = ['mjchef']  # kitchen id
kpword = ['kitc_hen']  # kitchen password
sid = ['mjboy']  # stock id
spword = ['st_ock']  # stock password
order_fin = "Beef Meal (3 ), Coke -m (2 )" #temp. order


def header():
    border()
    print("\t\tWELCOME TO ERP SYSTEM OF MJ Burger Point")
    border()

def erp():
    access = login()
    if access == 'a':  # admin-complete access
        home()
    elif access == 'c':  # customer-counter kiosk access
        counter()
    elif access == 'r':  # salesman-reciept access
        bill(order_fin)
    elif access == 'k':  # chef-kitchen access
        kitchen(order_fin)
    elif access == 's':  # inventory boy-stock access
        stock(order_fin)
    elif access == 0:
        border2()
        l=input("Enter \"l\" if you want to login:").lower()
        if l=='l':
            erp()
        else:
            print("Have  a nice day!")
            border()


def login():
    print("\t\t\t\tLOGIN Here")
    ch = input("\nEnter \"A\" if you've your account (Press any key for the alternative case):").lower()
    if ch == 'a':
        access = already()
    else:
        ch = input("Enter \"C\" if you're a customer:").lower()
        if ch == 'c':
            access = 'c'
        else:
            print("Invalid Command")
            access=0
    return (access)


def logout():
    border()
    print("LOGGED OUT Successfully!")
    access = 0
    border()
    erp()


def already():
    border2()
    id = input("Enter your login ID:")
    if id in aid:
        ind = aid.index(id)
        pword = input("Enter your password:")
        if pword == apword[ind]:
            access = 'a'
            border2()
            print("\t\t\t\tAccess granted")
            border2()
        else:
                while pword != apword[ind]:
                    print("\t\t\t\tInvalid Password!")
                    pword = input("Enter your password:")
                    access = 0
                access = 'a'
                border2()
                print("\t\t\t\tAccess granted")
                border2()
    elif id in rid:
        ind = rid.index(id)
        pword = input("Enter your password:")
        if pword == rpword[ind]:
            access = 'r'
            border2()
            print("\t\t\t\tAccess granted")
            border2()
        else:
            while pword != rpword[ind]:
                print("\t\t\t\tInvalid Password!")
                pword = input("Enter your password:")
                access = 0
            access = 'r'
            border2()
            print("\t\t\t\tAccess granted")
            border2()
    elif id in kid:
        ind = kid.index(id)
        pword = input("Enter your password:")
        if pword == kpword[ind]:
            access = 'k'
            border2()
            print("\t\t\t\tAccess granted")
            border2()
        else:
            while pword != kpword[ind]:
                print("\t\t\t\tInvalid Password!")
                pword = input("Enter your password:")
                access = 0
            access = 'k'
            border2()
            print("\t\t\t\tAccess granted")
            border2()
    elif id in sid:
        ind = sid.index(id)
        pword = input("Enter your password:")
        if pword == spword[ind]:
            access = 's'
            border2()
            print("\t\t\t\tAccess granted")
            border2()
        else:
            while pword != spword[ind]:
                print("\t\t\t\tInvalid Password!")
                pword = input("Enter your password:")
                access = 0
            access = 's'
            border2()
            print("\t\t\tAccess granted")
            border2()
    else:
        print("Invalid ID")
        access = 0
    return (access)


def home():
    print("\t\t\t\t\tHome")
    border()
    print("\n\t\t 1. Employes \n\t\t 2. Counter \n\t\t 3. Stock \n\t\t 4. Kitchen \n\t\t 5. Bill/Reciept")
    border()
    again = 'v'
    while again == 'v':
        cho = input("Select module by entering respective number: ")
        if cho == '1':
            employe()
        elif cho == '2':
            counter()
        elif cho == '3':
            stock(order_fin)
        elif cho == '4':
            kitchen(order_fin)
        elif cho == '5':
            bill(order_fin)
        else:
            print("Invalid Command")
        again = input(
            "Enter \"v\" if you want to visit any other module (Press any key for the alternative case): ").lower()
    else:
        log = input("Enter \"o\" to logout:").lower()
        if log == 'o':
            logout()
        else:
            print("Invalid Command")
            home()


def employe():
    border2()
    print("\t\t\t\t\tEMPLOYE")
    stay='y'
    while stay=='y':
        cr_e = input("Enter \"1\" if you want to create an employe account and \"2\" if you want to view ID's of previous employes: ")
        if cr_e == '1':
            print("\n Employe's Posts: \n 1. Salesman/Receptionist \n 2. Chef/Kitchen worker \n 3. Inventory boy/Stock Manager ")
            border2()
            cho = input(" Select Employe's post (by entering respective number):")
            if cho == '1':
                i = 'ag'
                while i == 'ag':
                    nrid = input("Create user ID:")
                    if (nrid not in aid) and (nrid not in rid) and (nrid not in kid) and (nrid not in sid):
                        if len(nrid)>=4:
                            j = 'ag'
                            while j == 'ag':
                                print("Make sure your password must have \'_\' and is of atleast 4 characters")
                                nrpword = input("Create user Password:")
                                l=len(nrpword)
                                if ('_' not in nrpword) or (l<4): 
                                    j = 'ag'
                                else:
                                    j = 'nag'
                            border2()
                            print("\t\tEmploye Account Successfully Created")
                            border2()
                            rid.append(nrid)
                            rpword.append(nrpword)
                            i = 'nag'
                        else:
                                print("ID must be of atleast 4 characters")
                                i = 'ag'
                    else:
                        print("ID already taken")
                        i = 'ag'
            elif cho == '2':
                i = 'ag'
                while i == 'ag':
                    nkid = input("Create user ID:")
                    if (nkid not in aid) and (nkid not in rid) and (nkid not in kid) and (nkid not in sid):
                        if len(nkid)>=4:
                            j = 'ag'
                            while j == 'ag':
                                print("Make sure your password must have \'_\' and is of atleast 4 characters")
                                nkpword = input("Create user Password:")
                                l=len(nkpword)
                                if ('_' not in nkpword) or (l<4):
                                    j = 'ag'
                                else:
                                    j = 'nag'
                            border2()
                            print("\t\tEmploye Account Successfully Created")
                            border2()
                            kid.append(nkid)
                            kpword.append(nkpword)
                            i = 'nag'
                        else:
                            print("ID must be of atleast 4 characters")
                            i = 'ag'
                    else:
                        print("ID already taken")
                        i = 'ag'
            elif cho == '3':
                i = 'ag'
                while i == 'ag':
                    nsid = input("Create user ID:")
                    if (nsid not in aid) and (nsid not in rid) and (nsid not in kid) and (nsid not in sid):
                        if len(nsid)>=4:
                            j = 'ag'
                            while j == 'ag':
                                print("Make sure your password must have \'_\' and is of atleast 4 characters")
                                nspword = input("Create user Password:")
                                l=len(nspword)
                                if ('_' not in nspword) or (l<4):
                                    j = 'ag'
                                else:
                                    j = 'nag'
                            border2()
                            print("\t\tEmploye Account Successfully Created")
                            border2()
                            sid.append(nsid)
                            spword.append(nspword)
                            i = 'nag'
                        else:
                                print("ID must be of atleast 4 characters")
                                i = 'ag'
                    else:
                        print("ID already taken")
                        i = 'ag'
            else:
                print("Post Unavailable")
        elif cr_e =='2':
            print("\n|-------------------------------MJ Burger Point Employe-----------------------------|\n\n|-----------------------------------Salemen's IDs-----------------------------------|\n")
            nr = len(rid)
            j = 1
            for i in range(0, nr):
                print("\tSalesman", j, "...................", rid[i])
                j += 1
            print("\n|--------------------------------------Chef's IDs-----------------------------------|\n")
            nk = len(kid)
            j = 1
            for i in range(0, nk):
                print("\tChef", j, ".......................", kid[i])
                j += 1
            print("\n|----------------------------------Stock Manager's IDs-------------------------------|\n")
            ns = len(sid)
            j = 1
            for i in range(0, ns):
                print("\tStock Manager", j, "...............", sid[i])
                j += 1
            print("\n|------------------------------------------------------------------------------------|\n")
        else:
            print("Invalid Command")
        stay=input("Enter \"Y\" if you want to stay in Employe Module (Press any key for the alternative case):").lower()


def counter():
    order_fin = ""
    border2()
    print("\t\t\t\t\tCOUNTER")
    print("\n \t Menu Options: \nEnter \'B\' to view Burger Menu \nEnter \'E\' to view Extra Menu \nEnter \'S\' to view Sauce Menu \nEnter \'D\' to view Drink Menu \nEnter \'M\' to view Meal Menu")
    w = 'y'
    while w == 'y':
        Menu = input("\nEnter your Menu Choice here:").lower()
        if Menu == 'b':
            order_fin = BMenu(order_fin)
        elif Menu == 'e':
            order_fin = EMenu(order_fin)
        elif Menu == 's':
            order_fin = SMenu(order_fin)
        elif Menu == 'd':
            order_fin = DMenu(order_fin)
        elif Menu == 'm':
            order_fin = MMenu(order_fin)
        else:
            print("Choose valid")
        w = input(
            "\nIf you want to select another menu, press \'Y\' (Press any key for the alternative case): ").lower()
    sure = '1'
    while sure == '1':
        n = len(order_fin)-1
        order_fin = (order_fin[:n])
        order_f=order_fin
        print("You odered: \n", order_fin)
        approve = input("\nEnter \'A\' to approve the order (Press any key for the alternative case): ").lower()
        if approve == 'a':
            border()
            print("\t\t\tOrder Placed!")
            border()
            sure = '0'
        else:
            approve = input("\nEnter \'C\' if you are sure, you want to cancel the order:").lower()
            if approve == 'c':
                border()
                print("\tOrder Cancelled!")
                border()
                sure = '0'
            else:
                print("Invalid")
    bill(order_fin)
    kitchen(order_fin)
    ad_s=input("Enter \"a\" if you're an admin to view stock (Press any key for the alternative case): ").lower()
    if ad_s=='a':
        id = input("Enter your login ID:")
        if id in aid:
            ind = aid.index(id)
            pword = input("Enter your password:")
            if pword == apword[ind]:
                access = 'a'
                border2()
                print("\t\t\t\tAccess granted")
                border2()
            else:
                    while pword != apword[ind]:
                        print("\t\t\t\tInvalid Password!")
                        pword = input("Enter your password:")
                        access = 0
                    access = 'a'
                    border2()
                    print("\t\t\t\tAccess granted")
                    border2()
        else:
            print("Invalid ID")
            access = 0
        if access =='a':
            stock(order_f)
            acess='c'
        else:
            border2()
            print("\t\t\t\tAccess Denied!")
            border2()
            print("Have a Good Day!")    
    else:
        print("Have a Good Day!")
    print("\t\tThanks")
    if access == 'c':
        header()
        main()


def border():
    print("|-----------------------------------------------------------------------------------|")


def border2():
    print(" -----------------------------------------------------------------------------------")


def BMenu(order_fin):
    BMenu = ["Chicken Burger ", " Chicken CheeseBurger ",
             " Beef Burger ", " Beef CheeseBurger "]
    BPrice = ['450', '500', '600', '650']
    border()
    print("\tBurger Menu: \n1.", BMenu[0], "\t\t", BPrice[0], "/-\n2.", BMenu[1], "\t", BPrice[1],
          "/-\n3.", BMenu[2], "\t\t", BPrice[2], "/-\n4.", BMenu[3], "\t\t", BPrice[3], "/-")
    border()
    choice = input(
        "\nIf you want to place an order, press \'Y\' (Press any key for the alternative case):  ").lower()
    while choice == "y":
        order = input(
            "\nPlace your order (by entering respective number) based on the menu shown above: ")
        if order == '1':
            qty = input("Enter the quantity: ")
            order_men = BMenu[0] + "(" + qty + " ) "
        elif order == '2':
            qty = input("Enter the quantity: ")
            order_men = BMenu[1] + "(" + qty + " ) "
        elif order == '3':
            qty = input("Enter the quantity: ")
            order_men = BMenu[2] + "(" + qty + " ) "
        elif order == '4':
            qty = input("Enter the quantity: ")
            order_men = BMenu[3] + "(" + qty + " ) "
        else:
            print("Invalid")
            order_men = " "
        if order_men != " ":
            order_fin += (order_men + ',')
        else:
            order_fin += order_men
        choice = input("\nIf you want to order more from this menu, press \'Y\'  (Press any key for the alternative case):  ").lower()
    n = len(order_fin)
    order_fin = (order_fin[:n])
    return (order_fin)


def EMenu(order_fin):
    EMenu = [' Crispy chicken Piece ', ' Chicken Nuggets ', ' Fries ']
    EPrice = ['100', '25', '150', '220', '300']
    border()
    print("\tExtras Menu: \n1.", EMenu[0], "\t", EPrice[0], "\n2.", EMenu[1],
          "\t\t", EPrice[1], "\n3.", EMenu[2], "\t\tR:150/-  M:220/-  L:300/-")
    border()
    choice = input(
        "\nIf you want to place an order, press \'Y\' (Press any key for the alternative case): ").lower()
    while choice == "y":
        order = input(
            "\nPlace your order (by entering respective number) based on the menu shown above: ")
        if order == '1':
            qty = input("Enter the quantity: ")
            order_men = EMenu[0] + "(" + qty + " ) "
        elif order == '2':
            qty = input("Enter the quantity: ")
            order_men = EMenu[1] + "(" + qty + " ) "
        elif order == '3':
            for i in range(3):
                size = input(
                    "Choose 'R' for regular, 'M' for medium, 'L' for Large: ").lower()
                if size == 'r' or size == 'm' or size == 'l':
                    qty = input("Enter the quantity: ")
                    order_men = EMenu[2] + "-" + size + " (" + qty + " ) "
                    break
                else:
                    print("Unavailable Size!")
        else:
            print("Invalid")
            order_men = " "
        if order_men != " ":
            order_fin += (order_men + ',')
        else:
            order_fin += order_men
        choice = input("\nIf you want to order more from this menu, press \'Y\' (Press any key for the alternative case):  ").lower()
    n = len(order_fin)
    order_fin = (order_fin[:n])
    return (order_fin)


def SMenu(order_fin):
    SMenu = [' Mustard Sauce ', ' Chilli Sauce ',
             ' Grarlic Sauce ', ' Garlic Mayo ', ' Tomato Ketchup ']
    SPrice = ['20', '20', '20', '20', '20']
    border()
    print("\tSauce Menu: \n1.", SMenu[0], "\t\t", SPrice[0], "/-\n2.", SMenu[1], "\t\t", SPrice[1], "/-\n3.",
          SMenu[2], "\t\t", SPrice[2], "/-\n4.", SMenu[3], "\t\t", SPrice[3], "/-\n5.", SMenu[4], "\t", SPrice[4], "/-")
    border()
    choice = input(
        "\nIf you want to place an order, press \'Y\' (Press any key for the alternative case): ").lower()
    while choice == "y":
        order = input(
            "\nPlace your order (by entering respective number) based on the menu shown above: ")
        if order == '1':
            qty = input("Enter the quantity: ")
            order_men = SMenu[0] + "(" + qty + " ) "
        elif order == '2':
            qty = input("Enter the quantity: ")
            order_men = SMenu[1] + "(" + qty + " ) "
        elif order == '3':
            qty = input("Enter the quantity: ")
            order_men = SMenu[2] + "(" + qty + " ) "
        elif order == '4':
            qty = input("Enter the quantity: ")
            order_men = SMenu[3] + "(" + qty + " ) "
        elif order == '5':
            qty = input("Enter the quantity: ")
            order_men = SMenu[4] + "(" + qty + " ) "
        else:
            print("Invalid")
            order_men = " "
        if order_men != " ":
            order_fin += (order_men + ',')
        else:
            order_fin += order_men
        choice = input(
            "\nIf you want to order more from this menu, press \'Y\' (Press any key for the alternative case): ").lower()
    n = len(order_fin)
    order_fin = (order_fin[:n])
    return (order_fin)


def DMenu(order_fin):
    DMenu = [' Coke ', ' Sprite ', ' Marinda ']
    DPrice = ['100', '160', '220']
    border()
    print("\tDrink Menu: \n1.", DMenu[0], "\t\tR:100/-  M:160/-  L:220/-", "\n2.", DMenu[1],
          "\t\tR:100/-  M:160/-  L:220/-", "\n3.", DMenu[2], "\t\tR:100/-  M:160/-  L:220/-")
    border()
    choice = input(
        "\nIf you want to place an order, press \'Y\' (Press any key for the alternative case):  ").lower()
    while choice == "y":
        order = input(
            "\nPlace your order (by entering respective number) based on the menu shown above: ")
        if order == '1':
            for i in range(3):
                size = input(
                    "Choose 'R' for regular, 'M' for medium, 'L' for Large: ").lower()
                if size == 'r' or size == 'm' or size == 'l':
                    qty = input("Enter the quantity: ")
                    order_men = DMenu[0] + "-" + size + " (" + qty + " ) "
                    break
                else:
                    print("Unavailable Size!")
        elif order == '2':
            for i in range(3):
                size = input(
                    "Choose 'R' for regular, 'M' for medium, 'L' for Large: ").lower()
                if size == 'r' or size == 'm' or size == 'l':
                    qty = input("Enter the quantity: ")
                    order_men = DMenu[1] + "-" + size + " (" + qty + " ) "
                    break
                else:
                    print("Unavailable Size!")
        elif order == '3':
            for i in range(3):
                size = input(
                    "Choose 'R' for regular, 'M' for medium, 'L' for Large: ").lower()
                if size == 'r' or size == 'm' or size == 'l':
                    qty = input("Enter the quantity: ")
                    order_men = DMenu[2] + "-" + size + " (" + qty + " ) "
                    break
                else:
                    print("Unavailable Size!")
        else:
            print("Invalid")
            order_men = " "
        if order_men != " ":
            order_fin += (order_men + ',')
        else:
            order_fin += order_men
        choice = input(
            "\nIf you want to order more from this menu, press \'Y\' (Press any key for the alternative case): ").lower()
    n = len(order_fin)
    order_fin = (order_fin[:n])
    return (order_fin)


def MMenu(order_fin):
    MMenu = [' Chicken Meal ', ' Chicken CheeseMeal ',
             ' Beef Meal ', ' Beef CheeseMeal ']
    MPrice = ['800', '850', '950', '1000']
    border()
    print("\tMeal Menu: \n(Burger, R-Fries, R-Coke, Tomato Ketchup(2), Garlic Mayo(1))")
    print("1.", MMenu[0], "\t\t", MPrice[0], "/-\n2.", MMenu[1], "\t", MPrice[1],
          "/-\n3.", MMenu[2], "\t\t\t", MPrice[2], "/-\n4.", MMenu[3], "\t\t", MPrice[3], "/-")
    border()
    choice = input(
        "\nIf you want to place an order, press \'Y\' (Press any key for the alternative case): ").lower()
    while choice == "y":
        order = input(
            "\nPlace your order (by entering respective number) based on the menu shown above: ")
        if order == '1':
            qty = input("Enter the quantity: ")
            order_men = MMenu[0] + "(" + qty + " ) "
        elif order == '2':
            qty = input("Enter the quantity: ")
            order_men = MMenu[1] + "(" + qty + " ) "
        elif order == '3':
            qty = input("Enter the quantity: ")
            order_men = MMenu[2] + "(" + qty + " ) "
        elif order == '4':
            qty = input("Enter the quantity: ")
            order_men = MMenu[3] + "(" + qty + " ) "
        else:
            print("Invalid")
            order_men = " "
        if order_men != " ":
            order_fin += (order_men + ',')
        else:
            order_fin += order_men
        choice = input(
            "\nIf you want to order more from this menu, press \'Y\' (Press any key for the alternative case): ").lower()
    n = len(order_fin)
    order_fin = (order_fin[:n])
    return (order_fin)


def bill(order_fin):
    border()
    print("|-------------------------------------RECEIPT---------------------------------------|")
    border()
    order_price = 0
    total_sub = 0
    BPrice = ['450', '500', '600', '650']
    EPrice = ['100', '25', '150', '220', '300']
    SPrice = ['20', '20', '20', '20', '20']
    DPrice = ['100', '160', '220']
    MPrice = ['800', '850', '950', '1000']
    print("\t\t\tQty \t\t Item \t\t Cost")
    border2()
    to = order_fin.split(",")
    n = len(to)
    i = 0
    while i < (n):
        a = 1
        o = to[i].split()
        ordered = o[0]+" "+o[1]
        b = o[2]
        x = b[1:3]
        z=x
        q = int(z)
        if ordered == 'Chicken Burger':
            print("\t\t\t",q, "\t", ordered, "\t\t", BPrice[0])
            while a <= q:
                order_price += int(BPrice[0])
                a = a+1
        elif ordered == 'Chicken CheeseBurger':
            print("\t\t\t",q, "\t", ordered, "\t\t", BPrice[0])
            while a <= q:
                order_price += int(BPrice[0])
                a = a+1
        elif ordered == 'Beef Burger':
            print("\t\t\t",q, "\t", ordered, "\t\t\t", BPrice[0])
            while a <= q:
                order_price += int(BPrice[0])
                a = a+1
        elif ordered == 'Beef CheeseBurger':
            print("\t\t\t",q, "\t", ordered, "\t\t", BPrice[0])
            while a <= q:
                order_price += int(BPrice[0])
                a = a+1
        elif ordered == 'Crispy Chicken':
            print("\t\t\t",q, "\t", ordered, "\t\t", EPrice[0])
            while a <= q:
                order_price += int(EPrice[0])
                a = a+1
        elif ordered == 'Chicken Nuggets':
            print("\t\t\t",q, "\t", ordered, "\t\t", EPrice[1])
            while a <= q:
                order_price += int(EPrice[1])
                a = a+1
        elif ordered == 'Fries -R' or ordered == 'Fries -r':
            print("\t\t\t",q, "\t", ordered, "\t\t", EPrice[2])
            while a <= q:
                order_price += int(EPrice[2])
                a = a+1
        elif ordered == 'Fries -M' or ordered == 'Fries -m':
            print("\t\t\t",q, "\t", ordered, "\t\t", EPrice[3])
            while a <= q:
                order_price += int(EPrice[3])
                a = a+1
        elif ordered == 'Fries -L' or ordered == 'Fries -l':
            print("\t\t\t",q, "\t", ordered, "\t\t", EPrice[4])
            while a <= q:
                order_price += int(EPrice[4])
                a = a+1
        elif ordered == 'Mustard Sause':
            print("\t\t\t",q, "\t", ordered, "\t\t", SPrice[0])
            while a <= q:
                order_price += int(SPrice[0])
                a = a+1
        elif ordered == 'Chilli Sauce':
            print("\t\t\t",q, "\t", ordered, "\t\t", SPrice[1])
            while a <= q:
                order_price += int(SPrice[1])
                a = a+1
        elif ordered == 'Garlic Sauce':
            print("\t\t\t",q, "\t", ordered, "\t\t", SPrice[2])
            while a <= q:
                order_price += int(SPrice[2])
                a = a+1
        elif ordered == 'Garlic Mayo':
            print("\t\t\t",q, "\t", ordered, "\t\t", SPrice[3])
            while a <= q:
                order_price += int(SPrice[3])
                a = a+1
        elif ordered == 'Tomato Ketchup':
            print("\t\t\t",q, "\t", ordered, "\t\t", SPrice[4])
            while a <= q:
                order_price += int(SPrice[4])
                a = a+1
        elif ordered == 'Coke -R' or ordered == 'Coke -r':
            print("\t\t\t",q, "\t", ordered, "\t\t", DPrice[0])
            while a <= q:
                order_price += int(DPrice[0])
                a = a+1
        elif ordered == 'Coke -M' or ordered == 'Coke -m':
            print("\t\t\t",q, "\t", ordered, "\t\t", DPrice[1])
            while a <= q:
                order_price += int(DPrice[1])
                a = a+1
        elif ordered == 'Coke -L' or ordered == 'Coke -l':
            print("\t\t\t",q, "\t", ordered, "\t\t", DPrice[2])
            while a <= q:
                order_price += int(DPrice[2])
                a = a+1
        elif ordered == 'Sprite -R' or ordered == 'Sprite -r':
            print("\t\t\t",q, "\t", ordered, "\t\t", DPrice[0])
            while a <= q:
                order_price += int(DPrice[0])
                a = a+1
        elif ordered == 'Sprite -M' or ordered == 'Sprite -m':
            print("\t\t\t",q, "\t", ordered, "\t\t", DPrice[1])
            while a <= q:
                order_price += int(DPrice[1])
                a = a+1
        elif ordered == 'Sprite -L' or ordered == 'Sprite -l':
            print("\t\t\t",q, "\t", ordered, "\t\t", DPrice[2])
            while a <= q:
                order_price += int(DPrice[2])
                a = a+1
        elif ordered == 'Marinda -R' or ordered == 'Marinda -r':
            print("\t\t\t",q, "\t", ordered, "\t\t", DPrice[0])
            while a <= q:
                order_price += int(DPrice[0])
                a = a+1
        elif ordered == 'Marinda -M' or ordered == 'Marinda -m':
            print("\t\t\t",q, "\t", ordered, "\t\t", DPrice[1])
            while a <= q:
                order_price += int(DPrice[1])
                a = a+1
        elif ordered == 'Marinda -L' or ordered == 'Marinda -l':
            print("\t\t\t",q, "\t", ordered, "\t\t", DPrice[2])
            while a <= q:
                order_price += int(DPrice[2])
                a = a+1
        elif ordered == 'Chicken Meal':
            print("\t\t\t",q, "\t", ordered, "\t\t", MPrice[0])
            while a <= q:
                order_price += int(MPrice[0])
                a = a+1
        elif ordered == 'Chicken CheeseMeal':
            print("\t\t\t",q, "\t", ordered, "\t\t", MPrice[1])
            while a <= q:
                order_price += int(MPrice[1])
                a = a+1
        elif ordered == 'Beef Meal':
            print("\t\t\t",q, "\t", ordered, "\t\t\t", MPrice[2])
            while a <= q:
                order_price += int(MPrice[2])
                a = a+1
        elif ordered == 'Beef CheeseMeal':
            print("\t\t\t",q, "\t", ordered, "\t\t", MPrice[3])
            while a <= q:
                order_price += int(MPrice[3])
                a = a+1
        i = i+1

    total_sub += order_price
    sales_tax = int((0.03)*total_sub)
    border2()
    print("\t\t\t SubTotal =", total_sub)
    print("\t\t\t Sales Tax=", sales_tax)
    border2()
    total_price = total_sub + sales_tax
    print("\t\t\t Total    =", total_price)
    border2()
    if total_price != 0:
        print("You've to pay", total_price, "/- in total.")
        bill=1
        while bill==1:
            am = input("Enter amount to pay the bill: ")
            if am.isdigit():
                if int(am)>=total_price:
                    bill=0
                    back = int(am)-total_price
                    if back != 0:
                        print("Remaining Amount=", back)
                        print("Collect your remaining amount")
                        border2()
                else:
                    print("You entered amount less than your total bill!")
                    bill=1
            else:
                print("Enter digits only!")
                bill=1
    else:
        print("There's no order in the queue to pe paid!")
        border2()


def stock(order_fin):
    count_bun = 200  # Qty of bun
    count_chpatty = 100  # Qty of chicken patties
    count_bfpatty = 100  # Qty of beef patties
    count_cheslice = 200  # Qty of cheese slice
    count_chpiece = 100  # Qty of chicken pieces
    count_chnug = 200  # Qty of chicken nuggets
    count_fr = 150  # Qty of Frozen Fries Reg Pack
    count_fm = 150  # Qty of Frozen Fries Med Pack
    count_fl = 150  # Qty of Frozen Fries Lar Pack
    count_ss = 20  # Qty of Special Sauce
    count_ms = 200  # Qty of Mustatd Sauce
    count_cs = 200  # Qty of Chilli Sauce
    count_gs = 200  # Qty of Garlic Sauce
    count_gms = 200  # Qty of Garlic Mayo
    count_tks = 200  # Qty of Tomato Ketchup
    count_cr = 150  # Qty of Coke Reg
    count_cm = 150  # Qty of Coke Med
    count_cl = 150  # Qty of Coke Lar
    count_sr = 150  # Qty of Sprite Reg
    count_sm = 150  # Qty of Sprite Med
    count_sl = 150  # Qty of Sprite Lar
    count_mr = 150  # Qty of Marinda Reg
    count_mm = 150  # Qty of Marinda Med
    count_ml = 150  # Qty of Marinda Lar

    to = order_fin.split(",")
    n = len(to)
    i = 0
    while i < (n):
        a = 1
        o = to[i].split()
        ordered = o[0]+" "+o[1]
        b = o[2]
        x = b[1:3]
        z=x
        q = int(z)
        if ordered == 'Chicken Burger':
            while a <= q:
                count_bun -= 1
                count_chpatty -= 1
                count_ss -= 0.25
                x
                a = a+1

        elif ordered == 'Chicken CheeseBurger':
            while a <= q:
                count_bun -= 1
                count_chpatty -= 1
                count_cheslice -= 1
                count_ss -= 0.25
                a = a+1

        elif ordered == 'Beef Burger':
            while a <= q:
                count_bun -= 1
                count_bfpatty -= 1
                count_ss -= 0.25
                a = a+1

        elif ordered == 'Beef CheeseBurger':
            while a <= q:
                count_bun -= 1
                count_bfpatty -= 1
                count_cheslice -= 1
                count_ss -= 0.25
                a = a+1
        elif ordered == 'Crispy Chicken':

            while a <= q:
                count_chpiece -= 1
                a = a+1
        elif ordered == 'Chicken Nuggets':

            while a <= q:
                count_chnug = 1
                a = a+1
        elif ordered == 'Fries -R' or ordered == 'Fries -r':

            while a <= q:
                count_fr -= 1
                a = a+1
        elif ordered == 'Fries -M' or ordered == 'Fries -m':

            while a <= q:
                count_fm -= 1
                a = a+1
        elif ordered == 'Fries -L' or ordered == 'Fries -l':

            while a <= q:
                count_fl -= 1
                a = a+1
        elif ordered == 'Mustard Sause':

            while a <= q:
                count_ms -= 1
                a = a+1
        elif ordered == 'Chilli Sauce':

            while a <= q:
                count_cs -= 1
                a = a+1
        elif ordered == 'Garlic Sauce':

            while a <= q:
                count_gs -= 1
                a = a+1
        elif ordered == 'Garlic Mayo':

            while a <= q:
                count_gms -= 1
                a = a+1
        elif ordered == 'Tomato Ketchup':

            while a <= q:
                count_tks -= 1
                a = a+1
        elif ordered == 'Coke -R' or ordered == 'Coke -r':

            while a <= q:
                count_cr -= 1
                a = a+1
        elif ordered == 'Coke -M' or ordered == 'Coke -m':

            while a <= q:
                count_cm -= 1
                a = a+1
        elif ordered == 'Coke -L' or ordered == 'Coke -l':

            while a <= q:
                count_cl -= 1
                a = a+1
        elif ordered == 'Sprite -R' or ordered == 'Sprite -r':

            while a <= q:
                count_sr -= 1
                a = a+1
        elif ordered == 'Sprite -M' or ordered == 'Sprite -m':

            while a <= q:
                count_sm -= 1
                a = a+1
        elif ordered == 'Sprite -L' or ordered == 'Sprite -l':

            while a <= q:
                count_sl -= 1
                a = a+1
        elif ordered == 'Marinda -R' or ordered == 'Marinda -r':
            while a <= q:
                count_mr -= 1
                a = a+1

        elif ordered == 'Marinda -M' or ordered == 'Marinda -m':

            while a <= q:
                count_mm -= 1
                a = a+1
        elif ordered == 'Marinda -L' or ordered == 'Marinda -l':

            while a <= q:
                count_ml -= 1
                a = a+1
        elif ordered == 'Chicken Meal':

            while a <= q:
                count_bun -= 1
                count_chpatty -= 1
                count_ss -= 0.25
                count_fr -= 1
                count_tks -= 2
                count_gms -= 1
                a = a+1
        elif ordered == 'Chicken CheeseMeal':

            while a <= q:
                count_bun -= 1
                count_chpatty -= 1
                count_cheslice -= 1
                count_ss -= 0.25
                count_fr -= 1
                count_tks -= 2
                count_gms -= 1
                a = a+1
        elif ordered == 'Beef Meal':

            while a <= q:
                count_bun -= 1
                count_bfpatty -= 1
                count_ss -= 0.25
                count_fr -= 1
                count_tks -= 2
                count_gms -= 1
                a = a+1
        elif ordered == 'Beaf CheeseMeal':

            while a <= q:
                count_bun -= 1
                count_bfpatty -= 1
                count_cheslice -= 1
                count_ss -= 0.25
                count_fr -= 1
                count_tks -= 2
                count_gms -= 1
                a = a+1
        i = i+1
    print("Stock Updated.")
    dis = input(
        "Enter \"Y\" if you want to view stock (Press any key for the alternative case): ").lower()
    if dis == 'y':
        print(f"""
    |---------------------------MJ Burger Point Stock----------------------------------|
    |------------------------------Burger Ing.-----------------------------------------|
      Bun                   : {count_bun} Pairs                               
      Chicken Patties       : {count_chpatty} Pcs                            
      Beef Patties          : {count_bfpatty} Pcs       
      Cheese                : {count_cheslice} Slices    
      Special Sauce         : {count_ss}
    |----------------------------------------------------------------------------------|
    |-------------------------------Frozen Extras--------------------------------------|
      Chicken Pieces        : {count_chpiece} Pcs                 
      Chicken Nuggets       : {count_chnug} Pcs                   
      Fries (Regular Pack)  : {count_fr} Packets
      Fries (Medium Pack)   : {count_fm} Packets
      Fries (Large Pack)    : {count_fl} Packets                   
    | ---------------------------------------------------------------------------------|
    |--------------------------------Sauces--------------------------------------------|
      Chilli Sause          : {count_cs}                    
      Garlic Sause          : {count_gs}                    
      Mayo                  : {count_ms}                    
      Garlic Mayo Sause     : {count_gms}                    
      Tomato Ketchup        : {count_tks}                                            
    |----------------------------------------------------------------------------------|
    |---------------------------------Drinks-------------------------------------------|
      Coke    (Regular)     : {count_cr} Bottles
      Coke    (Medium)      : {count_cm} Bottles
      Coke    (Large)       : {count_cl} Bottles
      Sprite  (Regular)     : {count_fr} Bottles 
      Sprite  (Medium)      : {count_fm} Bottles
      Sprite  (Large)       : {count_fl} Bottles 
      Marinda (Regular)     : {count_fr} Bottles 
      Marinda (Medium)      : {count_fm} Bottles
      Marinda (Large)       : {count_fl} Bottles                              
    |-----------------------------------------------------------------------------------|
    """)
    else:
        print("You are at Stock Inventory!")
    border2()



def kitchen(order_fin):
    order_time = 0  # time to prepare certain item
    time_req = 0  # total time to complete final order
    BTime = ['20', '20', '30', '30']
    ETime = ['15', '15']
    STime = ['1', '1', '1', '1', '1']
    DTime = ['1', '1', '1', '1', '1']
    MTime = ['25', '25', '35', '35']
    to = order_fin.split(",")
    n = len(to)
    i = 0
    while i < (n):
        o = to[i].split()
        ordered = o[0]+" "+o[1]
        if ordered == 'Chicken Burger':
                order_time += int(BTime[0])
        elif ordered == 'Chicken Cheese':
                order_time += int(BTime[0])
        elif ordered == 'Beef Burger':
                order_time += int(BTime[0])
        elif ordered == 'Beef Cheese':
                order_time += int(BTime[0])
        elif ordered == 'Crispy Chicken':
                order_time += int(ETime[0])
        elif ordered == 'Chicken Nuggets':
                order_time += int(ETime[1])
        elif ordered == 'Fries -R' or ordered == 'Fries -r':
                order_time += 15
        elif ordered == 'Fries -M' or ordered == 'Fries -m':
                order_time += 20
        elif ordered == 'Fries -L' or ordered == 'Fries -l':
                order_time += 25
        elif ordered == 'Mustard Sause':
                order_time += int(STime[0])
        elif ordered == 'Chilli Sauce':
                order_time += int(STime[1])
        elif ordered == 'Garlic Sauce':
                order_time += int(STime[2])
        elif ordered == 'Garlic Mayo':
                order_time += int(STime[3])
        elif ordered == 'Tomato Ketchup':
                order_time += int(STime[4])
        elif ordered == 'Coke -R' or ordered == 'Coke -r':
                order_time += int(DTime[0])
        elif ordered == 'Coke -M' or ordered == 'Coke -m':
                order_time += int(DTime[0])
        elif ordered == 'Coke -L' or ordered == 'Coke -l':
                order_time += int(DTime[0])
        elif ordered == 'Sprite -R' or ordered == 'Sprite -r':
                order_time += int(DTime[1])
        elif ordered == 'Sprite -M' or ordered == 'Sprite -m':
                order_time += int(DTime[1])
        elif ordered == 'Sprite -L' or ordered == 'Sprite -l':
                order_time += int(DTime[1])
        elif ordered == 'Marinda -R' or ordered == 'Marinda -r':
                order_time += int(DTime[2])
        elif ordered == 'Marinda -M' or ordered == 'Marinda -m':
                order_time += int(DTime[2])
        elif ordered == 'Marinda -L' or ordered == 'Marinda -l':
                order_time += int(DTime[2])
        elif ordered == 'Chicken Meal':
                order_time += int(MTime[0])
        elif ordered == 'Chicken CheeseMeal':
                order_time += int(MTime[1])
        elif ordered == 'Beef Meal':
                order_time += int(MTime[2])
        elif ordered == 'Beaf CheeseMeal':
                order_time += int(MTime[3])
        i = i+1
    time_req += int(order_time)
    border2()
    print(order_fin)
    if time_req != 0:
        print("Your order will be ready in ", time_req, "minutes!")
    else:
        print("There's no order in the queue to get ready!")
    border2()


# starts here
header()
erp()