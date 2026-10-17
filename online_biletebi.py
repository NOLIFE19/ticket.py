# import sys
# print(sys.version)
# უნდა დაწეროთ პითონის სკრიპტი, რომელიც ახორციელებს კ
# ინოთეატრის ბილეთების ჯავშნის ავტომატურ შემოწმებას და დამუშავებას მომხმარებლის მიერ ერთ ხაზზე

# ეს ჩემი ვერსიაში   კლიენტს ვაწერინებ  3  ციფრს.  Minda 3cali bileti, bileti ghirs 15 lari maqvs qeshi    60 lari "  
import re


ticket = input("enter the text: ")
ticketdigit= re.findall(r"\d+", ticket)

try:

    ticketcheck = int(ticketdigit[0])
    ticketprice_one = int(ticketdigit[1])
    changeprice_one=float(ticketdigit[2])
    ticketprice=ticketcheck*ticketprice_one
    if ticketcheck <= 0:
        raise ValueError("Ticket quantity must be minimum 1")

    if ticketprice_one <= 0:
        raise ZeroDivisionError("the amount is not enough")
    if changeprice_one <ticketprice:
        raise ValueError("amount paid not enough")

 
except IndexError:
    print("We cannot analyze your request: not enough numbers.")

except ValueError as error:
    print(f"Error: {error}")
else:
    changeprice=changeprice_one-ticketprice
    print(f"Number of tickets {ticketprice} ")
    print(f"One Ticket Price {ticketprice_one}  GEL")
    print(f"Total pirce {ticketprice}  GEL") 
    print(f"Amount Paid {changeprice_one}  GEL") 
    print(f"Change: {changeprice:.2f} GEL")


finally:

    print("Transaction attempt completed!") 




