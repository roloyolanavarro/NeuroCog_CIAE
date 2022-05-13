import psychopy.parallel as lpt


def create_lpt(lpt_status, lpt_port):
    if lpt_status:
        lpt.setPortAddress(lpt_port)


def lpt_set_data(lpt_signal, lpt_status):
    #print('LPT_SIGNAL:' + str(lpt_signal))
    if lpt_status:
        lpt.setData(lpt_signal)
