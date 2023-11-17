from utilities.temperature import temperature
from utilities.coords import coords
from utilities.ping import ping
from utilities.whois import whois
from utilities.traceroute import traceroute
from interface import main_menu
from os import system
from time import sleep


class program:
    def main(self):
        try:
            main_menu.logo()
            main_menu.options()
            choice = input("> ")

            match choice:
                case "1":
                    system("cls")
                    coords.CWD()
                    sleep(2)
                    self.main() 
                case "2":
                    system("cls")
                    temperature.weather()
                    sleep(2)
                    self.main()
                case "3":
                    system("cls")
                    ping.pingg()
                    sleep(2)
                    self.main()
                case "4":
                    system("cls")
                    whois.whois()
                    sleep(2)
                    self.main()
                case "5":
                    system("cls")
                    traceroute.tracer()
                    sleep(2)
                    self.main()
                case "0":
                    system("cls")
                    system("exit")
                case _:
                    system("cls")
                    print("ERROR: invalid option")
                    sleep(2)
                    system('cls')
                    self.main()   
                    
        except KeyError:
            system("cls")
            print("ERROR: city name is incorrect")
            sleep(2)
            system('cls')
            self.main()

        except KeyboardInterrupt:
            system("cls")
            print("ERROR: program closed")
            sleep(2)
            system('cls')


if __name__ == "__main__":
    programm = program()
    programm.main()
