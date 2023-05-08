import time
import webbrowser
import pyautogui


# abdo_lazez ©
# TikTok = abdo_lazez

def User():
    #Say Hello For User 
    #قل مرحبا لي المستخدم

    global name_user
    name_user = input('Hello Welcome In \'Mcdonalds\' Enter Your Name : ').capitalize()
    print(f'Hello { name_user } ')

    #Take A Message Form User And Handling
    #قم يأخذ الرساله من المستخدم وقم بتحليلها والرد عليها

    help_user = input('how can i help you today..?  ').lower()
    print('--------------------------------------')
    if 'order' in help_user:
            pass
    elif 'location' in help_user:
            webbrowser.open('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
            time.sleep(2)
            pyautogui.typewrite('https://bit.ly/3LMyeUI')
            time.sleep(1)
            pyautogui.press('enter')
    elif 'menu' in help_user:
            webbrowser.open('https://www.mcdonalds.eg/eat/menu/page/full-menu')
    else:
        print("Sorry, I don't understand what you want")
        help_user = input('Please how can i help you today..? ')
User()

# Sugeest For User
#اقترح الطعام علي المستخدم
def sugeest():

    # Food And Price
    food = {"burger": 10,
            "pipsi": 40,
            "cafe": 20,
            "chicken": 20,
            }
    
    print(name_user + ' , I think this will impress you')
    for x in food:
        p = [x]
        print(f" [{', '.join(p)}] ", end="")

#Take Order From User
#قم بأخذ الطلب من المستخدم

    def take_order():

        food_order = input('\n what would you like to order : ').lower()
        print(food_order)
        messge = input(name_user + ' Are you sure you want to order: \n' + food_order + '\t' 'Yes Or No...' '\t' ).lower()
        print(messge)
        for x in messge:
            if x == "yes":
                pass
            elif x == "no":
                food_order = input('\n what would you like to order : ')
            else:
                break

        #Show A Receipt
        #اظهر فاتوره الشراء

        for i in food:
            if i == food_order:
                price = food[food_order]
                print(f'{name_user} your Add a ' + i)
                print(f'And price are {price}$')
                print('------------Thank you, your order has been placed------------')
                time.sleep(2)
    take_order()

sugeest()

while True:
     User()

