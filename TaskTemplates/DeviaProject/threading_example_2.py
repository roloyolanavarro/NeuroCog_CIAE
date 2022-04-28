import threading
# use Queue for python2
import queue
import random

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
LETTERS = [ x for x in LETTERS ]

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def randoms(k, q):
    result = dict()
    result['letter'] = random.choice(LETTERS)
    result['number'] = random.choice(NUMBERS)
    q.put({k: result})

threads = list()
q = queue.Queue()
results = dict()

for name in ('alpha', 'oscar', 'yankee',):
    threads.append( threading.Thread(target=randoms, args=(name, q)) )
    threads[-1].start()
_ = [ t.join() for t in threads ]
while not q.empty():
    results.update(q.get())

print(results)