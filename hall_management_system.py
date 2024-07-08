
class Star_Cinema:
    __hall_list=[]
    def entry_hall(self,hall):
        self.__hall_list.append(hall)
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        super().entry_hall(self) 
    def entry_show(self,id,movie_name,time):
        self.show_list.append([id,movie_name,time])
        seat_allocation = [['0' for _ in range(self.cols)]
                           for _ in range(self.rows)]
        self.seats[id]=seat_allocation
    def book_seats(self,id,seat_pos):
        if id not in self.seats:
            print(f"Show ID {id} not found.")
            return    
        seat_allocation=self.seats[id]
        for row, col in seat_pos:
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if seat_allocation[row][col] == '0':
                    seat_allocation[row][col] = '1' 
                else:
                    print(f"\n\tSeat ({row}, {col}) is already booked.")
                    return
            else:
                print(f"\n\tSeat ({row}, {col}) is out of range.")
                return
            print(f"\n\tSeats booked successfully for Show ID {id}.")
        self.seats[id]=seat_allocation
    def view_show_list(self):
        if not self.show_list:
            print('\n\tno show are currently running')
        else:
            print(f"Shows running in Hall {self.hall_no}:")
            for show in self.show_list:
                id,movie_name,time=show
                print(f"\n\tShow ID:{id}, Movie Name: {movie_name}, Time: {time}") 
    def view_available_seat(self,id):
        if id not in self.seats:
            print(f"Show ID {id} not found.")
            return
        seat_allocation=self.seats[id]
        print(f'available seats for show id {id}')
        for row in range(self.rows):
            for col in range(self.cols):
                if seat_allocation[row][col] == '0':
                     available_seats =[(row,col)]
        if not available_seats:
            print("No available seats.")
        else:
            
            for row in seat_allocation:
                print(' '.join(row)) 
hall1 = Hall(5,5, 'Hall1') 
hall1.entry_show('Show1', 'i love you', '12:00 PM')
hall1.entry_show('Show2', 'tik tik tik', '03:00 PM')                                 
class counter:
    def __init__(self):
        self.halls=Star_Cinema.__hall_list
        
    while True:
            print("Options:\n")
            print("1: view all show today")
            print("2: viw avalabale seat")
            print("3: book ticket")
            print("4: exit")
             
            ch=int(input("\nEnter Option:"))
             
            if ch==1:
              hall1.view_show_list()    
            elif ch==2:
                show_id=input('inter the show_id name: ')
                hall1.view_available_seat(show_id) 
            
            elif ch==3:
                show_id=input('inter the show_id name: ')
                seat_row=int(input('choose seat row: '))
                seat_col=int(input('choose seat col: '))
                hall1.book_seats(show_id,[(seat_row,seat_col)])
            elif ch==4:
                break
             
            else:
                print("\n\t---> !!! Choose Valid Option\n")
                    
                