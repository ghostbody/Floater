import time

def info(message, messtype):
    if messtype == "info":
        print "\033[32m[FLOATER v1.0 %s]\033[0m %s : %s" % (time.ctime(time.time()), "INFO", message)
    elif messtype == "warning":
        print "\033[32m[FLOATER v1.0 %s]\033[0m %s : %s" % (time.ctime(time.time()), "WARNING", message)
    elif messtype == "error":
        print "\033[32m[FLOATER v1.0 %s]\033[0m %s : %s" % (time.ctime(time.time()), "ERROR", message)
