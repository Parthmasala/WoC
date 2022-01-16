class ContactDetail: 
    def __init__(self, name,Cont_No):
        self.name = name
        self.Contact_No = [Cont_No]

print(f"\nEnter : \n1.New Contact \n2.Add to Existing Contact \n3.Search Existing \n4.View all \n5.Exit")
List = []   #Empty List to store data

while(1):
    choice = int(input(f"\nEnter your choice : "))
    if choice == 1:
        name = input("Name : ")
        check = 0
        for ExistingCont in List:
            if ExistingCont.name == name :
                print("Contact already exists.")
                check=1
                break
        if check == 0:
            Contact_no = int(input("Enter Number : "))
            new_contact = ContactDetail(name,Contact_no)
            List.append(new_contact)
            List.sort(key=lambda x: x.name)     #sorted the list in alphabetical order of their names
    elif choice == 2:
        name = input("Name : ")
        check = 0
        for ExistingCont in List:
            if ExistingCont.name == name :
                Contact_no = int(input("Enter another Number : "))
                ExistingCont.Contact_No.append(Contact_no)#append contact in it
                check=1
                break
        if check == 0:
            print("Contact doesn't exist")
    elif choice == 3:
        keyword = input("Enter a keyword : ")
        index = 0
        ListWithKeyword = []
        for ExistingCont in List:
            if keyword in ExistingCont.name :
                index = index + 1
                tmp = str(index)
                print(tmp + ". " +ExistingCont.name)
                ListWithKeyword.append(ExistingCont)
        if index == 0 :
            print("Contact not found")
        else:
            choose = int(input("Enter Your Choice of index : "))
            print(ListWithKeyword[choose-1].name , ListWithKeyword[choose-1].Contact_No)
    elif choice == 4:
        for cont in List:
            print(cont.name, cont.Contact_No)
    else:
        break

for cont in List:
    print(cont.name, cont.Contact_No)