
import sys
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# server config
server_name = "192.168.1.207"
server_port = 8001

system_path = ("file:///%s/front/" % sys.path[0])
