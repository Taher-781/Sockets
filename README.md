# Sockets
OSI or TCP/IP
2 layer models applied to networking :-
7 layer OSI model 
4 layer TCP/IP

_______ The Application layer:-
highest level of the model, the application layer, is the closest to the user.
Networked applications such as web browsers, email clients, and online video games all operate at this level.
 HTTP,FTTP,DHCP,Telnet,FTP,Ping

___________The transport layer :-
The second layer deals with the transport of the data, and its accompanying application protocol. 
This layer will wrap the data in a way specified by a transport protocol.

TCP- transmission control protocol
UDP- user datagram protocol

___________The network layer

There are two types of IP address. Internet Protocol version 4 (IPv4) addresses are 32-bit numbers usually written as 
four numbers in the range 0–255 (that is, 8-bit numbers) separated by dots, 
for example 127.5.64.87.
In 1998, these IP addresses were starting to run out, so Internet Protocol version 6 was created, 
which uses 128-bit number addresses usually written as 8 hexadecimal numbers, for example 2001:db8:0:0:0:ff00:42:8329.

___________The Data Link layer
The final layer of the model deals with individual connections between machines. 
The protocols used here can vary, both in the type of connection (wired or not) and 
the type of network (local or wide area networks).

This also includes the initial connection between a user’s machine and the internet, 
whether by UTP cable (commonly referred to as an Ethernet cable) or a wireless connection such as WiFi.



+++++Sockets++++
Sockets come in pairs, and a simple analogy is to imagine a tube with a port at either end.
Whatever is put into one end of the tube can be taken out of the other end of the tube, and vice versa.

In recent times, 
socket has almost exclusively been used to refer to a socket that uses the Internet Protocol (IP) and 
in particular the Transmission Control Protocol (TCP).

There are many types of socket; the type used is determined by the protocol used by the network

To use sockets in your programs, an application programming interface (API) is required.
An API is a mechanism for talking to different programs, or to a piece of software.
This could be functions, processes, or a set of rules; the API defines how you, as the programmer, must use the software.

While many socket APIs exist, the Berkeley sockets API is the most widely used 
and a version exists in most general-purpose programming languages.

++Server socket
A socket that waits for a connection to be made is typically used by server programs.
Servers are always waiting; when a client connects, the server deals with the request and sends a response.

To create a socket for use in a server you would follow these steps:

1.First create a socket of a specific type (protocol)
2.Then bind the socket to the network address where connections will be made
3.Set the socket to listen for a client to make a connection
4.Wait for a connection, accept it, and create a new socket to manage the connection between the server and this client;
  every client that connects to the server will get its own connection socket
5.Then send and receive (recv) data over the connection socket
6.Finally, close the socket when new connections are no longer needed


++Client socket
Once a server socket is waiting for connections, a client socket can connect to it.

Creating a client socket is a simpler process, but there are still defined steps:

First create a socket that is of the same type as the socket you wish to connect to
Then connect the socket to the network address of the server socket
You then send and receive (recv) data over the socket
Finally, close the connection when complete

++++ Using Sockets in Python
The parameters socket.AF_INET and socket.SOCK_STREAM determine the type of socket and
protocol to be used.

In this case, AF_INET specifies Internet Protocol version 4 and SOCK_STREAM denotes TCP,
so a TCP/IP socket is created.

Ports are typically used to identify the purpose of the connection and can be any number
between 0 and 65535. 
Ports 0 to 1023 are well known ports that are usually restricted for specific uses: 
for example, port 80 is HTTP and shouldn’t really be used.

When server_socket.accept() is called, your program will wait for a connection to be made.

When a new client connects, two parameters are returned:

A new socket, which I have called connection_socket and is the connection to the client
The network address of the client that connected, including its IP address and port


++Sending And receiving Data
Now you can connect a pair of sockets, the next step is to use them to communicate and 
send data back and forth.
This is done using the send and recv(receive) functions of the sockets.


