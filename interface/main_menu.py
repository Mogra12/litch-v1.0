from colorama import Fore


def logo():
   logo = """

        ▄█        ▄█      ███      ▄████████    ▄█    █▄    
        ███       ███  ▀█████████▄ ███    ███   ███    ███   
        ███       ███▌    ▀███▀▀██ ███    █▀    ███    ███   
        ███       ███▌     ███   ▀ ███         ▄███▄▄▄
        ███       ███▌     ███     ███        ▀▀███▀▀▀▀███▀  
        ███       ███      ███     ███    █▄    ███    ███   
        ███▌    ▄ ███      ███     ███    ███   ███    ███   
        █████▄▄██ █▀      ▄████▀   ████████▀    ███    █▀    
        ▀                                                    
        
        """
   print(logo)


def options():
    options = """
    1 - Cordinates
    2 - Temperature
    3 - Ping IP/Domain
    4 - Whois
    5 - Traceroute
    
    0 - Exit
          """
    print(options)
