from datetime import date

# class section start--
class Ticket:
    __ticket_serial_no = 1

    def __init__(self, movie_obj, theater_obj, seat_no_list):
        print("Ticket Created")
        self.present_date = date.today()
        self.ticket_serial_no = Ticket.__ticket_serial_no
        Ticket.__ticket_serial_no += 1
        self.movie_name = movie_obj.name
        self.theater_name = theater_obj.theater_name
        self.seat_list = seat_no_list
        self.seat = str(seat_no_list).replace("[", "").replace("]", "")
        for theater in theater_list:
            if theater == theater_obj:
                for seat_no in seat_no_list:
                    theater.seat_list[int(seat_no) - 1] = "Booked"

        self.cost = 0
        for seat in self.seat_list:
            if int(seat) <= 15:
                self.cost += 3000
            elif int(seat) <= 30:
                self.cost += 4000
            elif int(seat) <= 45:
                self.cost += 5000
            elif int(seat) <= 60:
                self.cost += 6000
            elif int(seat) <= 75:
                self.cost += 7000
            elif int(seat) <= 90:
                self.cost += 8000
            elif int(seat) <= 105:
                self.cost += 9000
            else:
                self.cost += 12000

    def show_ticket_info(self):
        print("Date : ", self.present_date)
        print("Ticket_no : ", self.ticket_serial_no)
        print("Movie : ", self.movie_name)
        print("Theater : ", self.theater_name)
        print("Seat : ", self.seat)
        print("Total amount : ", self.cost)


class Movie:
    def __init__(
        self, name, release_date, screen_date, end_date, director, actor, actress
    ):
        print("Movie Added.")
        self.name = name
        self.release_date = release_date
        self.screen_date = screen_date
        self.end_date = end_date
        self.director = director
        self.actor = actor
        self.actress = actress

    def show_movie_info(self):
        print("***Movie Info***\n")
        print("Movie name : ", self.name)
        print("Release date : ", self.release_date)
        print("Screen date : ", self.screen_date)
        print("End date : ", self.end_date)
        print("Director :", self.director)
        print("Actor : ", self.actor)
        print("Actress : ", self.actress)


class Theater:
    def __init__(self, t_name, no_of_seat=100):
        print("Theater Added.")
        self.theater_name = t_name
        self.no_of_seat = no_of_seat
        self.seat_list = [i for i in range(1, self.no_of_seat + 1)]


# class section end--

movie_list, theater_list, ticket_list = [], [], []


def create_ticket(movie_obj, theater_obj, seat_no_list):
    ticket_obj = Ticket(movie_obj, theater_obj, seat_no_list)
    ticket_list.append(ticket_obj)


def update_ticket(ticket_no, movie_name, theater_name, seat_no_list):
    for ticket in ticket_list:
        if ticket.ticket_serial_no == ticket_no:
            # First reset the previous booked Seat
            for theater in theater_list:
                if theater.theater_name == ticket.theater_name:
                    for seat in ticket.seat_list:
                        theater.seat_list[int(seat) - 1] = seat
            # then assign updated values
            ticket.movie_name = movie_name
            ticket.theater_name = theater_name
            ticket.seat_no_list = seat_no_list
            for theater in theater_list:
                if theater.theater_name == theater_name:
                    for seat in ticket.seat_no_list:
                        theater.seat_list[int(seat) - 1] = "Booked"


def delete_ticket(ticket_no):
    for ticket in ticket_list:
        if ticket.ticket_serial_no == ticket_no:
            ticket_list.remove(ticket)
            Ticket.__ticket_serial_no -= 1  # decrese auto:inc tickest serial to


def get_ticket(seat_no=None):
    if seat_no is None:
        for ticket in ticket_list:
            ticket.show_ticket_info()
    else:
        ticket_list[-1].show_ticket_info()


def create_movie(name, release_date, screen_date, end_date, director, actor, actress):
    movie_obj = Movie(
        name, release_date, screen_date, end_date, director, actor, actress
    )
    movie_list.append(movie_obj)


def update_movie(
    old_name, new_name, release_date, screen_date, end_date, director, actor, actress
):
    for movie in movie_list:
        if movie.name == old_name:
            movie.name = new_name
            movie.release_date = release_date
            movie.screen_date = screen_date
            movie.end_date = end_date
            movie.director = director
            movie.actor = actor
            movie.actress = actress


def delete_movie(name):
    for movie in movie_list:
        if movie.name == name:
            movie_list.remove(movie)


def get_movie(name=None):
    if name is None:
        for movie in movie_list:
            movie.show_movie_info()
    else:
        for movie in movie_list:
            if movie.name == name:
                movie.show_movie_info()


def create_theater(t_name, t_seat):
    t_obj = Theater(t_name, t_seat)
    theater_list.append(t_obj)


def update_theater(old_t_name, t_name, t_seat):
    for theater in theater_list:
        if theater.theater_name == old_t_name:
            theater.theater_name = t_name
            theater.no_of_seat = t_seat
            # create a list to mark already booked or not
            theater.seat_list = [i for i in range(1, theater.no_of_seat + 1)]


def get_theater():
    for theater in theater_list:
        print(theater.theater_name)
        print(theater.no_of_seat)
        # print(theater.seat_list)
        seat_list = theater.seat_list
        cost = 3000
        for i in range(1, len(seat_list) + 1):
            if i % 15 == 0 or i == len(seat_list):
                print(seat_list[i - 1], end="")
                if i > 105:
                    print("   (rate => ", 12000, " mmk)")
                else:
                    print("   (rate => ", cost, " mmk)")
                cost += 1000
            else:
                print(seat_list[i - 1], "  ", end="")


def delete_theater(t_name):
    for theater in theater_list:
        if theater.theater_name == t_name:
            theater_list.remove(theater)
