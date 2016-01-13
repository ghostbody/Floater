import time

def info(message, messtype):
    if messtype == "info":
        print "[FLOATER v1.0 %s] %s : %s" % (time.ctime(time.time()), "INFO", message)
    elif messtype == "warning":
        print "[FLOATER v1.0 %s] %s : %s" % (time.ctime(time.time()), "WARNING", message)
    elif messtype == "error":
        print "[FLOATER v1.0 %s] %s : %s" % (time.ctime(time.time()), "ERROR", message)
