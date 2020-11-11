import socket
import queue
import select

buffer = 1024
available_connections = 1000
server = socket.socket()
server.bind(('localhost', 8888))
server.listen(available_connections)
server.setblocking(False)
message_redirect = {}
inputs = [server, ]
outputs = []


def add_readable(readable):
    global buffer
    global inputs
    global outputs
    global server
    global message_redirect
    for r in readable:
        if r is server:
            conn, addr = server.accept()
            inputs.append(conn)
            message_redirect[conn] = queue.Queue()
        else:
            data = r.recv(buffer)
            message_redirect[r].put(data)
            outputs.append(r)


def add_writable(writeable):
    global outputs
    global message_redirect
    for w in writeable:
        data_to_client = message_redirect[w].get()
        w.send(data_to_client)
        outputs.remove(w)


def exception_handler():
    global inputs
    global outputs
    global message_redirect
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del message_redirect[e]


while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    add_readable(readable)
    add_writable(writeable)
    exception_handler()
