
from ticketbooker import TicketBooker
from passenger import Passenger

def book_ticket(p):
    tb = TicketBooker()
    if tb.total_ticket == 0:
        print("\n -- No ticket available --")
        return
    
    if (p.berth_preference == 'L' and tb.available_lower > 0) or (p.berth_preference == 'M' and tb.available_middle > 0) or (p.berth_preference == 'U' and tb.available_upper > 0):
        if p.berth_preference == 'L':
            tb.bookTicket(p,tb.lower_position.pop(0),'L')
            TicketBooker.available_lower -= 1
        elif p.berth_preference == 'M':
            tb.bookTicket(p,tb.middle_position.pop(0),'M')
            TicketBooker.available_middle -= 1
        else:
            tb.bookTicket(p,tb.upper_position.pop(0),'U')
            TicketBooker.available_upper -= 1
    elif tb.available_lower > 0:
        tb.bookTicket(p,tb.lower_position.pop(0),'L')
        TicketBooker.available_lower -= 1
    elif tb.available_middle > 0:
        tb.bookTicket(p,tb.middle_position.pop(0),'M')
        TicketBooker.available_middle -= 1
    elif tb.available_upper > 0:
        tb.bookTicket(p,tb.upper_position.pop(0),'U')
        TicketBooker.available_upper -= 1
    elif tb.available_rac > 0:
        tb.add_to_rac(p,tb.rac_position.pop(0),"RAC")
    else:
        tb.add_to_waiting(p,tb.waiting_position.pop(0),"WL")
    TicketBooker.total_ticket -= 1
    
def cancel_ticket(pas_id):
    if  (pas_id not in TicketBooker.passengers):
        print("No Passengers found")
        return
    tb = TicketBooker()
    tb.cancelTicket(pas_id)
    
    
    
while(True):
    
    print("\n ---Train Ticket Reservation---")
    print("1. Book Ticket \n2. Cancel Ticket \n3. Available Tickets \n4. Booked Tickets \n5. Exit")
    
    choice = int(input("Enter Choice: "))
    
    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        berth_preference = input("Enter berth prefernce( L or M or U ): ")
        p = Passenger(name,age,berth_preference)
        book_ticket(p)
    elif choice == 2:
        pas_id = int(input("Enter Passenger Id: "))
        cancel_ticket(pas_id)
    elif choice == 3:
        TicketBooker().print_available()
    elif choice == 4:
        TicketBooker().booked_tickets()
    elif choice == 5:
        print("--- Thank you for using our service! ---")
        break
    else:
        print("Enter the valid option")