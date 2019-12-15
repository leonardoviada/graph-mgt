
def errore(errCode, desc):
    print("ERRORE[" + Colori.WARNING + errCode.__str__() + Colori.ENDC + "]" +
          " - " + Colori.FAIL + desc + Colori.ENDC)
    exit(errCode)


class Colori:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
