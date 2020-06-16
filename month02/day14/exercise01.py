from threading import Thread
from time import sleep

tickets = ["T" + str(i) for i in range(1, 501)]


def booking_tickets(i):
    while tickets:
        ticket = tickets.pop(0)
        print(f"w{i}----{ticket}")
        sleep(0.1)


jobs = []
for i in range(1, 11):
    t = Thread(target=booking_tickets, args=(i,))
    jobs.append(t)
    t.start()

for t in jobs:
    t.join()
