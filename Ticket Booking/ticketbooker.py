from passenger import Passenger

class TicketBooker:
    
    total_ticket = 5
    available_lower = 1
    available_middle = 1
    available_upper = 1
    available_rac = 1
    available_waiting = 1
    
    rac_list = []
    waiting_list = []
    booked_ticket_list = []
    
    lower_position = [i for i in range(1,available_lower + 1)]
    middle_position = [i for i in range(1,available_middle + 1)]
    upper_position = [i for i in range(1,available_upper + 1)]
    rac_position = [i for i in range(1,available_rac + 1)]
    waiting_position = [i for i in range(1,available_waiting + 1)]
    
    passengers = {}
    
    def bookTicket(self, p, berth_info, alloted_berth):
        p.number = berth_info
        p.alloted = alloted_berth
        TicketBooker.passengers[p.passenger_id] = p
        TicketBooker.booked_ticket_list.append(p.passenger_id)
        print("--------------------------Booked Successfully")
        
    def cancelTicket(self,pas_id):
        p = TicketBooker.passengers.get(pas_id)
        if not p:
            print("No Details Found ---")
            return
        
        TicketBooker.passengers.pop(pas_id)
        TicketBooker.booked_ticket_list.remove(pas_id)
        pos_bok = p.number
        
        if p.alloted == 'L':
            TicketBooker.available_lower += 1
            TicketBooker.lower_position.append(pos_bok)
        elif p.alloted == 'M':
            TicketBooker.available_middle += 1
            TicketBooker.middle_position.append(pos_bok)
        elif p.alloted == 'U':
            TicketBooker.available_upper += 1
            TicketBooker.upper_position.append(pos_bok)
        
        if TicketBooker.rac_list:
            pas_from_rac = TicketBooker.passengers[TicketBooker.rac_list.pop(0)]
            TicketBooker.rac_position.append(pas_from_rac.number)
            TicketBooker.available_rac += 1
            
            if TicketBooker.waiting_list:
                pas_from_wai = TicketBooker.passengers[TicketBooker.waiting_list.pop(0)]
                # TicketBooker.waiting_position.append(pas_from_wai.number)
                TicketBooker.available_waiting += 1
                
                pas_from_wai.number = TicketBooker.rac_position.pop(0)
                pas_from_wai.alloted = "RAC"
                
                TicketBooker.rac_list.append(pas_from_wai.passenger_id)
                TicketBooker.available_rac -= 1
            from main import book_ticket
            book_ticket(pas_from_rac)
            
        TicketBooker.total_ticket += 1
        
        
    def add_to_rac(self,p,rac_info,alloted_rac):
        p.number = rac_info
        p.alloted = alloted_rac
        TicketBooker.passengers[p.passenger_id] = p
        TicketBooker.booked_ticket_list.append(p.passenger_id)
        TicketBooker.rac_list.append(p.passenger_id)
        TicketBooker.available_rac -= 1
        print("--------------------------Added to RAC Successfully")
        
    def add_to_waiting(self,p,wai_info,alloted_wai):
        p.number = wai_info
        p.alloted = alloted_wai
        TicketBooker.passengers[p.passenger_id] = p
        TicketBooker.booked_ticket_list.append(p.passenger_id)
        TicketBooker.waiting_list.append(p.passenger_id)
        TicketBooker.available_waiting -= 1
        print("--------------------------Added to Waiting List Successfully")
        
    def print_available(self):
        print("Total ticket:",TicketBooker.total_ticket)
        print("Lower Ticket:",TicketBooker.available_lower)
        print("Middle Ticket:",TicketBooker.available_middle)
        print("Upper Ticket:",TicketBooker.available_upper)
        print("RAC Ticket:",TicketBooker.available_rac)
        print("Waiting Ticket:",TicketBooker.available_waiting)
        print("--------------------------")
        
    def booked_tickets(self):
        
        if not TicketBooker.passengers:
            print("No details of passengers")
            return
        for p in TicketBooker.passengers.values():
            print(f"PASSENGER ID: {p.passenger_id}")
            print(f"Name: {p.name}")
            print(f"Age: {p.age}")
            print(f"Status: {p.number} {p.alloted}")
            print("--------------------------")
        
        
    
    