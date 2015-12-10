import socket
import user
import json

def test():
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.bind(("localhost", 8000))
    mySocket.listen(10)
    while True:
        connection, address = mySocket.accept()
        try:
            connection.settimeout(10)
            buf = connection.recv(1024)
            print address

            try:
                data = json.loads(buf)
                if data["action"] == "login":
                    auser = user.user()
                    newUser = auser.login(data["username"], address[0])
                    connection.send(json.dumps(newUser))
                elif data["action"] == "find":
                    auser = user.user()
                    print data["user"]
                    auer.set(data["user"])
                    result = auser.findFellow()
                    print result
                    connection.send(str(result))
            except Exception as e:
                print e

        except socket.timeout:
            print "time out"

if __name__ == "__main__":
    test ()
