import logging
import threading
import time
import random
#import pylink


def thread_function(name):
    logging.info("Thread %s: starting", name)
    while True:
        random_end = random.random()
        if random_end < 0.5:
            print('ending')
            break
    #d = pylink.getEYELINK().getNextData()
    # if d == end saccade
    #
    logging.info("Thread %s: finishing", name)
    return 'found end saccade'


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")