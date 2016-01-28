class bcolors:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    end = '\033[0m'

    # Bold
    bblack="\033[1;30m"
    bred="\033[1;31m"
    bgreen="\033[1;32m"
    byellow="\033[1;33m"
    bblue="\033[1;34m"
    bmagenta="\033[1;35m"
    bcyan="\033[1;36m"
    bwhite="\033[1;37m"

    def disable(self):
        self.black = ''
        self.red = ''
        self.green = ''
        self.yellow = ''
        self.blue = ''
        self.magenta = ''
        self.cyan = ''
        self.white = ''
        self.bblack = ''
        self.bred = ''
        self.bgreen = ''
        self.byellow = ''
        self.bblue = ''
        self.bmagenta = ''
        self.bcyan = ''
        self.bwhite = ''
        self.end = ''
