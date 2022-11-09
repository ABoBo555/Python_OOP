from movie import *

# Home screen start--
class Home:
    def __init__(self):
        print(
            """
        -Welcome from BoBo Cimema- 

        1.Enter 1 to go to Main_page
        2.Enter 2 to go to Admin portal
        3.Enter * to exit
        """
        )
        get_input = input()
        if get_input == "1":
            Main_page()
        elif get_input == "2":
            Admin_portal()
        elif get_input == "*":
            print("Exit")
        else:
            print("Invalid input")
            Home()


# Home screen end--


# Admin-portal screen start--
class Admin_portal:
    def __init__(self):
        print(
            """
        -Welcome from BoBo Cimema-        
          Enter * to see booked tickets
        1.Enter 1 to update ticket info
        2.Enter 2 to delete ticket
        3.Enter 3 to create a movie
        4.Enter 4 to update movie info
        5.Enter 5 to delete a movie
        6.Enter 6 to create a theater
        7.Enter 7 to update theater info
        8.Enter 8 to delete a theater
        9.Enter 9 to go back
        """
        )
        get_input = input()
        if get_input == "*":
            get_ticket()
            Admin_portal()
        elif get_input == "1":
            if len(ticket_list) == 0:
                print("First book a ticket to update, there isn't any ticket.")
                Admin_portal()
            else:
                print("Ticket Booked!")
                for ticket in ticket_list:
                    print(ticket.ticket_serial_no, end="")
                print()
                print(input("Enter Prev ticket no to update : "), end="")
                ticket_no = get_ticket_fun()

                print("Movies which are screened right now")
                for movie in movie_list:
                    print("\t\t", movie.name)
                movie_name = get_movie_fun()

                print("Available Theaters!")
                for theater in theater_list:
                    print("\t\t", theater.theater_name)

                theater_name, theater = get_theater_fun()
                seat_no = input("Enter updated seat no(seperated by comma) : ")

                seat_no_list = get_seat_fun(theater)
                update_ticket(ticket_no, movie_name, theater_name, seat_no_list)
                Admin_portal()

        elif get_input == "2":
            if len(ticket_list) == 0:
                print("There isn't any ticket to delete.")
                Admin_portal()
            else:
                ticket_no = input("Enter ticket no to delete : ")
                delete_ticket(ticket_no)
                Admin_portal()

        elif get_input == "3":
            name = input("Enter movie name : ")
            release_date = input("Enter release date : ")
            screen_date = input("Enter Screen date : ")
            end_date = input("Enter End date : ")
            director = input("Director name : ")
            actor = input("Lead Actor : ")
            actress = input("Lead Actress : ")
            create_movie(
                name, release_date, screen_date, end_date, director, actor, actress
            )
            get_movie(name)
            Admin_portal()

        elif get_input == "4":
            if len(movie_list) == 0:
                print("First create a movie to update, there isn't any movie.")
                Admin_portal()
            else:
                print("Which movie would you like to update?")
                for movie in movie_list:
                    print("\t\t", movie.name)

                prev_name, movie = get_movie_fun()
                new_name = input("Enter updated movie name : ")
                release_date = input("Enter updated release date : ")
                screen_date = input("Enter updated Screen date : ")
                end_date = input("Enter updated End date : ")
                director = input("Enter updated Director name : ")
                actor = input("Enter updated Lead Actor : ")
                actress = input("Enter updated Lead Actress : ")
                update_movie(
                    prev_name,
                    new_name,
                    release_date,
                    screen_date,
                    end_date,
                    director,
                    actor,
                    actress,
                )
                get_movie(new_name)
                Admin_portal()

        elif get_input == "5":
            if len(movie_list) == 0:
                print("There isn't any movie to delete.")
                Admin_portal()
            else:
                get_name = input("Enter movie name to delete : ")
                delete_movie(get_name)
                Admin_portal()

        elif get_input == "6":
            theater_name = input("Enter Theater name : ")
            total_seat = int(input("Enter total seat : "))
            create_theater(theater_name, total_seat)
            Admin_portal()

        elif get_input == "7":
            if len(theater_list) == 0:
                print("First create a theater to update, there isn't any theater.")
                Admin_portal()
            else:
                print("Enter previous Theater name to update.")
                theater_name, theater = get_theater_fun()
                new_theater = input("Enter updated heater name : ")
                total_seat = int(input("Enter total seat : "))
                update_theater(theater_name, new_theater, total_seat)
                Admin_portal()

        elif get_input == "8":
            if len(movie_list) == 0:
                print("There isn't any theater to delete.")
                Admin_portal()
            else:
                t_name = input("Enter theater name to delete : ")
                delete_theater(t_name)
                Admin_portal()

        elif get_input == "9":
            Home()

        else:
            print("Invalid Input")
            Admin_portal()


# Admin-portal screen end--

# Main screen start--
class Main_page:
    def __init__(self):
        print(
            """
        -Welcome from BoBo Cimema-        

        1.Enter 1 to buy ticket
        2.Enter 2 to see screened movies
        3.Enter 3 to see available seats
        4.Enter 4 to go to back
        """
        )
        get_input = input()

        if get_input == "1":
            if len(movie_list) == 0 or len(theater_list) == 0:
                print("Either 'Theater' or 'Movie' hasn't been created yet!")
                Main_page()
            else:
                print("Which movie would you like to watch?")
                for movie in movie_list:
                    print("\t\t", movie.name)

                movie_name, movie_obj = get_movie_fun()

                theater_name, theater_obj = get_theater_fun()

                seat_no_list = get_seat_fun(theater_obj)

                create_ticket(movie_obj, theater_obj, seat_no_list)
                get_ticket(1)
                Main_page()

        elif get_input == "2":
            if len(movie_list) == 0:
                print("'Movie' hasn't been created yet!")
                Main_page()
            else:
                get_movie()
                Main_page()

        elif get_input == "3":
            if len(theater_list) == 0:
                print("'Theater' hasn't been created yet!")
                Main_page()
            else:
                get_theater()
                Main_page()

        elif get_input == "4":
            Home()

        else:
            print("Invalid Input!")
            Main_page()


# Main screen end--


def get_ticket_fun():
    prev_ticket = input("Enter")
    action = True
    while action == True:
        for ticket in ticket_list:
            if ticket.ticket_serial_no == prev_ticket:
                action = False
                break
        else:
            prev_ticket = input("Plz Enter the screen movie only! : ")
    return prev_ticket


def get_movie_fun():
    prev_movie_name = input("Enter movie name : ")
    action = True
    while action == True:
        for movie in movie_list:
            if movie.name == prev_movie_name:
                action = False
                break
        else:
            prev_movie_name = input("Plz Enter the avaliable movie only! : ")
    return prev_movie_name, movie


def get_theater_fun():
    prev_theater_name = input("Enter theater name : ")
    action = True
    while action == True:
        for theater in theater_list:
            if theater.theater_name == prev_theater_name:
                action = False
                break
        else:
            prev_theater_name = input("Plz Enter available theater only! : ")
    return prev_theater_name, theater


def get_seat_fun(theater_obj):
    seat_no = input("Type seat no to book(seperated by comma) : ")
    seat_no_list = seat_no.split(",")

    action = True
    while action == True:
        cause = None
        if len(seat_no_list) != len(set(seat_no_list)):
            seat_no = input("Seats are duplicate, plz enter again : ")
            seat_no_list = seat_no.split(",")
        else:
            try:
                for seat_no in seat_no_list:
                    seat_no = int(seat_no)
                    if seat_no > len(theater_obj.seat_list) or seat_no < 1:
                        cause = 1
                        action = True
                        break
                    elif theater_obj.seat_list[seat_no - 1] == "Booked":
                        cause = 2
                        action = True
                        break
                    else:
                        action = False

                if cause == 1:
                    seat_no = input(
                        "Type available seat no to book(seperated by comma) : "
                    )
                    seat_no_list = seat_no.split(",")

                elif cause == 2:
                    seat_no = input(
                        "Seat {} already booked,choose other seat(seperated by comma) : ".format(
                            seat_no
                        )
                    )
                    seat_no_list = seat_no.split(",")

            except ValueError:
                seat_no = input("Type only numeric value for seats : ".format(seat_no))
                seat_no_list = seat_no.split(",")

    return seat_no_list


if __name__ == "__main__":
    Home()
