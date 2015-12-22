# Client Document V0.5


## 文件结构
```
+---
  + front
    - index.html   # 前端界面
  - config.py      # 配置文件
  - login.py       # 登陆模块（与服务器交互）
  - chat.py        # 聊天模块（客户端聊天的两个线程函数）
  - GUI.py         # 图形界面模块
  - main.py        # 主模块
```

## 总体思路

图形界面采用QtWebkit技术，是本地化的技术。图形界面采用HTML5+CSS+JavaScript的web网页框架。图形界面中的事件响应，由JavaScript调用pyObj的方法，实现跨语言的调用。pyObj是python语言在JavaScript的接口。

聊天功能，有两个线程，一个接受线程和一个发送线程。系统启动时即开启这两个线程。其中接受线程负责将远处peer传来的消息放入接受队列中，发送线程负责将发送队列中的消息取出发给远端。

GUI每500ms扫描接受队列一次，发现有接受的消息就显示在GUI大屏幕上。当用户点击GUI发送按钮时候，GUI调用JavaScript的send方法，在这其中调用python的send方法，传递message作为参数，python负责将这个message放入发送队列。

与服务器交流采用CS架构，客户端向远程服务端发送消息请求，等待远程服务器响应，响应聊天对象的。


## 实时聊天模块
```python
send_queue = Queue.Queue()
receive_queue = Queue.Queue()
```

以上两个队列为消息收发队列。

### 接受线程
当接受线程被创建之后，这个线程会创建一个socket通讯的监听，等待远方连接。当远方连接建立之后，线程进入工作状态，不断地接受远程的消息，并且将接收到的消息放入接受队列之中。

### 发送线程
当发送线程被创建之后，这个线程会创建一个socket，尝试连接远方的peer。当连接建立之后，线程进入工作状态，处理发送队列。当发送队列处于空状态时候，线程被阻塞。


## GUI 模块

这里主要负责GUI的核心部分，对JS的接口。Floater给出的是pyObj也就是JavaScript调用python的接口。
这里就是写python的javascript接口。

其中，注意，python的接口函数不能通过返回值直接返回给JavaScript，而是需要将返回值转为类的属性再返回到JavaScript。

```
receiveMsg = QtCore.pyqtProperty(str, fget=receive)
```

## 存在的问题

1. 协议乱七不糟，非常不规范，需要修正。
如：
```python
print "[FLOATER ERROR] send message to remote"
```
这样的消息格式需要规范到一个协议的类中。另外还有相互通信时候的隐式数据：
```python
mySocket.send(message)
```

2. 前端界面需要优化，需要考虑页面之间切换

3. 错误处理能力非常弱，远程如果关闭服务器之后，就死掉了

4. 。。。