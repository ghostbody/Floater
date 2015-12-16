# Protocol
## Floater v0.5

<br>

## Abstract
Protocol Floater v0.5 use Json as the switching data type between peers.
There two types of protocols, client-server and client-client(know as peer to peer).

## 1. Server and Client
The server is only responsible for getting a fellow to chat with.
### Packet switching type
```json
{"type":"Request"}
{"type":"Reply"}
```

### Packet actions
```json
{"action":"login"}
```
When the client send a login action to the server, it will send its user name as well. Then the server will insert a record to the user list.

```json
{
  "uid" : 0,
  "username": "admin",
  "ip": "192.168.1.1",
}
```
Notice that, the user in the user list means that it has not found a fellow to chat.

```json
{"action":"find"}
```

## 2. Client and Client
When the address get a fellow from the server, it know the fellow's ip address. Then the client will send a message to the fellow's client.
The client can be treated a server.

This is an example:
```json
{
  "type":"Request",
  "username":"Bob",
  "action" : "hello",
  "ip":"192.168.1.1"
}
```

```Json
{
  "type":"Reply",
  "username":"Alice",
  "action":"hi",
  "ip":"192.168.1.2"
}
```

Alice can also reject the connection.

```Json
{
  "type":"Reply",
  "username":"Unknown",
  "action":"reject",
  "ip":"192.168.1.2"
}
```

If Alice accept the connection:
Both Alice and Bob will start two threads, for sending message and receiving message. 

```json
{
  "type":"Chat",
  "username":"Bob",
  "ip":"192.168.1.1",
  "message":"It's a nice day, isn't it?"
}
```
Then Alice can reply
```json
{
  "type":"Chat",
  "username":"Bob",
  "ip":"192.168.1.1",
  "message":"Yes, and I feel so warm."
}
```

At any time, the two people can leave and break up the conversation.
```json
{
  "type":"Bye",
  "username":"Bob",
  "ip":"192.168.1.1",
}
```
