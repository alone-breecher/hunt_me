#! /usr/bin/env python3

"""
hunt_me: Find Usernames Across Social Networks Module
This module contains the main logic to search for usernames at social
networks.
"""
logo = """\033[33m
 █████╗  ██╗ ██████╗ ███╗   ██╗███████╗    ██████╗ ██████╗ ███████╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗███║██╔═████╗████╗  ██║██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██╔════╝██╔══██╗
███████║╚██║██║██╔██║██╔██╗ ██║█████╗      ██████╔╝██████╔╝█████╗  █████╗  ██║     ███████║█████╗  ██████╔╝
██╔══██║ ██║████╔╝██║██║╚██╗██║██╔══╝      ██╔══██╗██╔══██╗██╔══╝  ██╔══╝  ██║     ██╔══██║██╔══╝  ██╔══██╗
██║  ██║ ██║╚██████╔╝██║ ╚████║███████╗    ██████╔╝██║  ██║███████╗███████╗╚██████╗██║  ██║███████╗██║  ██║
╚═╝  ╚═╝ ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                                                                                            
                            \033[34m[✔] https://github.com/alonebreecher/a10n3_8633CH36       [✔]
                            \033[34m[✔]                      Version 1.1.0                    [✔]
                            \033[91m[X]      Please Don't Use For illegal Activity            [X]
                            \033[34m[✔]   specialthanks to AN712U CYB12 5OU1 , A10N3 8633CH36 [✔]
\033[97m """

import sys


if __name__ == "__main__":
    # Checking if the user is using the correct version of Python
    # Reference:
    #  If Python version is 3.6.5
    #               major --^
    #               minor ----^
    #               micro ------^
    major = sys.version_info[0]
    minor = sys.version_info[1]

    python_version = str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])

    if major != 3 or major == 3 and minor < 6:
        print("hunt_me requires Python 3.6+\nYou are using Python %s, which is not supported by hunt_me" % (python_version))
        sys.exit(1)

    import hunt_me
    hunt_me.main()
