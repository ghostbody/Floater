# Computer Network Cource Project
# 计算机网络课程项目
#FLOATER——陌生人聊天系统

## Team Member

叶嘉祺 Jiaqi Ye

徐庆龙 Qinglong Xu

彭俊杰 Junjie Peng

龙嘉伟 Jiawei Long

## Github Address
[https://github.com/ghostbody/computer-network](https://github.com/ghostbody/computer-network)

## Docs
[Protocol 0.5](https://github.com/ghostbody/computer-network/blob/master/doc/protocolV0.5.md) protocol prototype

## Eviroment Request

Python 2.7
PyQt4
QtWebKit

Any Operating System is available.(Linux have a bug about chinese path name)

## How to Run?
### Step1: config IP address for the server:
Modify the true ip address that the server computer is.
cd $project$/src/server/
edit config.py
```python
# server config
server_name = "192.168.1.159" # this is the server ip
server_port = 8003  # this is the server port
```
Note that if your client or other software has alreay occupied the port, you should change the port to resolve the confilct.

### Step2: config IP address for the client(s)
Modify the true ip address that the client computer is.
cd $project$/src/client/
edit config.py
```python
server_name = "192.168.1.159"   # this should be the same as the ip in server end
server_name_local = "192.168.1.207"  # this should be the ip address of the client ip
server_port = 8001            # this should be the port to communicate with server, the same with server
remote_server_port = 8003   # this is the port for remote client
image_server_port = 8004    # this is the port for image tansfering thread
```
Note that if your client or other software has alreay occupied the port, you should change the port to resolve the confilct.

### Step3: Run Server
Run the server Script
In windows simply click the runServer.bat

### Step4: Run Client
Run the client Script
In windows simply click the runClient.bat



## Notice
### 每次写代码和文档之前请执行git fetch更新fork和源仓库同步

## project plan
###（1）项目分工以及计划进度:
#### 分工:

叶嘉祺  项目构架

徐庆龙  前端编写(使用html5+pyQtWebkit编写前端，要求为单页面应用 ， single page application))

彭俊杰  协议分析设计(编写文档规范FLOATER的应用层通讯协议，在现在已有代码基础改)

龙嘉伟  后台程序编写（合并客户端和服务端功能，也就是说，先向服务端发出登录请求，然后从服务端获取聊天ip，然后再通过ip建立聊天连接）

###（2）计划进度:
 初步定下项目的整体框架和大致功能。对需求进行一定的分析。具体的项目细节和逻辑还需要进一步讨论。

###（3）项目具体需求分析:
 人海茫茫，相逢何必曾相识。在当今社会下，人聊天的欲望增强，陌生人聊天就是一个很好的方式。在我们的项目中，我们随机选取另外一个用户和你搭配一对一的聊天。整个对话是在匿名状态下进行的，当然，这并不会限制你向你的陌生朋友透露你的联系方式以获取更进一步的联络。
大家可以谈天说地，不必要顾及自己身份的高低，不需要顾及很多很多的东西，可以尽管谈天说地，尽情畅聊。

1、用户通过注册登录到聊天系统。

2、用户通过点击“聊一聊”按钮，系统通过服务器给用户返回一个当前在线的陌生人。

3、用户和陌生人开始聊天，系统限制两人对话必须从相互问候你好开始。两个用户之间可以随时断开彼此之间的连接，如果某一方这么做的话，那么系统将另一方的聊天终止。

4、正在聊天的人无法继续获取和其他用户进行聊天，除非断开连接，否则系统不会再重新分配聊天对象。

5、系统分配算法是随机的。

6、如果正在聊天的两个人一直不断开连接，则两个人一直持续聊天状态。

7.聊天过程中可以发送文字和图片内容。

Example:
小明注册了我们的软件FLOATER，然后他登录进了系统，然后点击了聊一聊按钮，系统开始随机分配用户，分配到了用户小红。两个人互相说“你好”，开始聊天，聊得很欢乐。然后小红断开了连接，小明也就返回了初始的界面。

###（4）扩展功能
1. NAT 内网穿透

## Preliminary Design

###(1)功能设计
####1、用户注册登录功能
注册:
   A. 用户填写邮箱、用户名、密码等信息，注册到系统
   B. 用户注册完毕收到确认邮件后激活账户
登录:
   A. 通过填写邮箱和密码进行登录
   B. 登录成功跳转到主页面，不成功则返回错误信息
####2、主页面（随机匹配）
A.主页面有一个按钮就是“聊一聊”，点击后系统计算出返回聊天的用户之后，进入聊天界面。
B.主页面左上方有一个个人设置按钮，点击后进入个人设置。
####3、聊天界面
A.聊天界面中显示对方的用户名，和自己的用户名，同时有两台的窗口
B..聊天界面可以在自己的窗口输入聊天信息，也可以发送图片。
C..点击发送之后，消息被发送，对方可以接收。
D..有一个红色的按钮，表示断开当前聊天，断开后系统提示确认断开，确认后返回主界面。
####4.个人设置页面
可以设置密码和用户名。

###(2)界面设计
![](https://github.com/ghostbody/computer-network/blob/master/doc/UI.png?raw=true)

### (3)协议设计
待定
其中，CS构架（获取用户）
P2P构架（和用户聊天）

基于TCP的CS和P2P架构:
![](https://github.com/ghostbody/computer-network/blob/master/doc/protocol.png?raw=true)

1、客户端A使用其与服务器S的连接向服务器发送请求，要求服务器S协助其连接客户端B。

2、S将B的公网和内网的TCP endpoint返回给A，同时，S将A的公网和内网的endpoint发送给B。

3、客户端A和B使用连接S的端口异步地发起向对方的公网、内网endpoint的TCP连接，同时监听各自的本地TCP端口是否有外部的连接联入。

4、A和B开始等待向外的连接是否成功，检查是否有新连接联入。如果向外的连接由于某种网络错误而失败，如:"连接被重置"或者"节点无法访问"，客户端只需要延迟一小段时间（例如延迟一秒钟），然后重新发起连接即可，延迟的时间和重复连接的次数可以由应用程序编写者来确定。

5、TCP连接建立起来以后，客户端之间应该开始鉴权操作，确保目前联入的连接就是所希望的连接。如果鉴权失败，客户端将关闭连接，并且继续等待新的连接联入。客户端通常采用"先入为主"的策略，只接受第一个通过鉴权操作的客户端，然后将进入p2p通信过程不再继续等待是否有新的连接联入。

####FLOATER协议
请求信息格式:
Request-Method: 请求完成的方法，包括请求接收资源GET和请求发送资源POST。

Host: 指定请求对象的Internet主机名和端口号，必须表示请求对象的原始服务器或网关的位置。

Cache-Control: 指定请求和响应遵循的缓存机制。

Referrer: 允许客户端指定请求对象的源资源地址，这可以允许服务器生成回退链表，可用来登陆、优化cache等。

User-Agent: 包含发出请求的用户的信息。

Range: 请求实体的一个或者多个子范围。

Content:信息实体。响应信息格式:

Version: 协议的版本号。

Date: 当前的GMT时间。

User-Agent: 被请求对象用户的信息。

Content-type: 表示后面的信息属于什么MIME类型。

Last-modified: 信息的最后改动时间。

Content-length: 表示信息实体的长度，以字节为单位。

Content-range: 表示信息实体的范围。

Content:信息实体。 :头部

abc:体部
