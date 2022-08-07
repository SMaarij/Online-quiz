from abc import ABC , abstractmethod
import Product_Dummy_Class as Profuct
class User(ABC):
    def __init__(self):
        self.name = input('Enter name: ')
        self.mail = input('Enter email')
        self.password = input('enter password: ')
    @abstractmethod
    def SaveToFile(self):
        # with open(x, 'a') as f:
        # f.write(self.name + ',' + self.mail + ',' + self.password + '\n')
        pass

    def CheckInFile(self, y):
        with open(y, 'r') as k:
            lines = k.readlines()
            for record in lines:
                if self.mail in record:
                    return True
                return False


class Customer(User):
    def SaveToFile(self):
        with open('store.txt','a+') as f:
            f.write(self.name + ',' + self.mail + ',' + self.password + '\n')
    def __init__(self):
        super().__init__()
        truth_value = super().CheckInFile('store.txt')
        if truth_value != True:
            self.SaveToFile()
            print('Your account has been created successfully')
        else:
            print('Your account is already present\n')
        self.Address = input('Enter your Address: ')
        self.Cart = ShoppingCart()
    def Show_Choose_And_Print(self):
        self.Cart.Show_Products()
        self.Cart.choose_Product()
        self.Cart.Show_Order()

class ShoppingCart:
    Domain_Products_Dict={}
    Prod_Price_dict = {}
    Choose_Prod_Dict = {}
    Choose_Domain_Dict={}

    def Show_DomainAndProducts(self):
        count = 1
        countt = 1
        S_no=1
        Domain_Product_Dict = ShoppingCart.Give_Domain_Products_Dict()
        for Domains in Domain_Product_Dict:
            print(str(S_no)+Domains)
            ShoppingCart.Choose_Domain_Dict[S_no]=Domains
        #Dictionary me Domain ki jo values hain un me product aur price ki 2d list value banao

        for Pair_Product in Item_List:
            print(str(count) + '.' + Pair_Product[0] + '\t' + 'pkr' + Pair_Product[1])
            count += 1
            ShoppingCart.Prod_Price_dict[Pair_Product[0]] = eval(Pair_Product[1])
        for Product in ShoppingCart.Prod_Price_dict:
            ShoppingCart.Choose_Prod_Dict[countt] = Product
            countt += 1
    @staticmethod
    def Give_Domain_Products_Dict():
        Domain_Product_Dict = {}
        Item_List=[]
        with open('Products.txt', 'r+') as Products:
            lines = Products.readlines()
            for line in lines:
                line = line.strip('\n')
                Domain_Product_List = line.split(';')
                Domain_Product_Dict[Domain_Product_List[0]] = Domain_Product_List[1]
            print(Domain_Product_Dict)
            for Item in Domain_Product_Dict.items():
                Product_Price=Item[1].split(',')
                for Procut_Price_string in Product_Price:
                    ItemAndPrice=Procut_Price_string.split(':')
                    Item_List.append(ItemAndPrice)
                Domain_Product_Dict[Item[0]]=Item_List
            return Domain_Product_Dict
    def choose_Product(self):
        self.Product_Quantity={}
        while True:
            ask_user = int(input('Enter which product number do you want to choose :'))
            if ask_user in ShoppingCart.Choose_Dict:
                final_product = ShoppingCart.Choose_Dict[ask_user]
            # self.Shoppingitems.append(final_product)
                print('Enter the quantity of ',final_product,':',end='')
                self.Product_Quantity[final_product]=int(input())
                print('Do you want to continue shopping?(y/n) ', end='')
                choice = input()
                if choice == 'y' or choice =='Y':
                    continue
                elif choice == 'n' or choice =='N':
                    break
                else:
                    print('Please enter valid choice')
            else:
                print('Enter valid choice')

    def Show_Cart(self):
        print('Item(s) Included in your cart are: ')
        for items in self.Product_Quantity.items():
            print(items[1],str(items[0])+'(s)')

    def Remove_from_Cart(self):
        print('Enter name of product to be removed: ')
        Choice=input()
        Removed_items=self.Product_Quantity.pop(Choice)
        print(str(Removed_items[1]),str(Removed_items[0]),"is removed from your cart")

    def Show_Order(self):
        self.Order=Order()
        self.Order.Order_Printer(self.Product_Quantity,ShoppingCart.Prod_Price_dict)
        self.Order.takefeedback()
class Order:
    def __init__(self):
        


    def Order_Printer(self, shopping_dict, Prod_Price_Dict):
        count = 1
        self.strg_ord = 'Sno.' + '*' * 8 + 'Product' + '*' * 8 + 'Price/unit' + '*' * 8 + 'Quantity' + '*' * 8 + 'Amount\n'
        self.Amount_list = []
        for item in shopping_dict:
            self.strg_ord += ' ' + str(count) + '  ' + '_' * 8 + item + '_' * 8 + str(Prod_Price_Dict[item]) + '    ' + '_' * 8 + str(shopping_dict[item]) + '    ' + '_' * 8 + str(Prod_Price_Dict[item] * shopping_dict[item]) + '\n'
            self.Amount_list.append(shopping_dict[item] * Prod_Price_Dict[item])
            count += 1
        self.strg_ord += str(self.Cal_total_payment())
        # print(self.Amount_list)
        # self.Write_In_File()
        print(self.strg_ord)

    def Write_In_File(self):
        with open('order.txt', 'a+') as l:
            l.write(self.strg_ord)

    def Cal_total_payment(self):
        self.summ_list = sum(self.Amount_list)
        string = 'Your Total Payment is :' + str(self.summ_list) + 'Rs\nTHANK YOU FOR SHOPPING!!'
        return string

    def takefeedback(self):
        print(f'Do you want to give any feedback ?')
        about_feedback = input(f'Your choice (Y) or (N):')
        if about_feedback == 'y' or about_feedback == 'Y':
            feedbackchoice = input(f'a)Did you have a good experience?(a)\n'
                                   f'b)Did you have a bad experience?(b)')
            if feedbackchoice == 'a' or 'A':
                feedback = input('Your feedback: ')
                with open('Goodfeedbacks.txt', 'a+') as f:
                    f.write(feedback + '\n')
                print('Thank you for your feedback')

            elif feedbackchoice == 'b' or 'B':
                feedback = input('Your feedback :')
                with open('Baadfeedbacks.txt', 'a') as f:
                    f.write(feedback + '\n')
                print('Thank you for your feedback')
        elif about_feedback == 'N' or about_feedback == 'n':
            return
        else:
            print('Invalid input')
            return
class Administrator(User):
    def __init__(self):
        super().__init__()
        self.BankAccount = input('Enter your bank account')



