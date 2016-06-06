class bcolors:
    @staticmethod
    def black(data):
        return '\033[30m'+ data + '\033[0m'
    @staticmethod
    def red(data):
        return '\033[31m'+ data + '\033[0m'
    @staticmethod
    def green(data):
        return '\033[32m'+ data + '\033[0m'
    @staticmethod
    def yellow(data):
        return '\033[33m'+ data + '\033[0m'
    @staticmethod
    def blue(data):
        return '\033[34m'+ data + '\033[0m'
    @staticmethod
    def magenta(data):
        return '\033[35m'+ data + '\033[0m'
    @staticmethod
    def cyan(data):
        return '\033[36m'+ data + '\033[0m'
    @staticmethod
    def white(data):
        return '\033[37m'+ data + '\033[0m'

    # Bold

    @staticmethod
    def bblack(data):
        return '\033[1;30m'+ data + '\033[0m'
    @staticmethod
    def bred(data):
        return '\033[1;31m'+ data + '\033[0m'
    @staticmethod
    def bgreen(data):
        return '\033[1;32m'+ data + '\033[0m'
    @staticmethod
    def byellow(data):
        return '\033[1;33m'+ data + '\033[0m'
    @staticmethod
    def bblue(data):
        return '\033[1;34m'+ data + '\033[0m'
    @staticmethod
    def bmagenta(data):
        return '\033[1;35m'+ data + '\033[0m'
    @staticmethod
    def bcyan(data):
        return '\033[1;36m'+ data + '\033[0m'
    @staticmethod
    def bwhite(data):
        return '\033[1;37m'+ data + '\033[0m'


    @classmethod
    def info(cls,data):
        return cls.bblue('[*] ') + data
    @classmethod
    def success(cls,data):
        return cls.bgreen('[+] ') + data
    @classmethod
    def warning(cls,data):
        return cls.byellow('[!] ') + data
    @classmethod
    def error(cls,data):
        return cls.bred('[ERROR] ') + data


