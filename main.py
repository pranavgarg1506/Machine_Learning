#!/usr/bin/python3
import logging

log_format = "%(asctime)s::"\
             "%(lineno)d::%(message)s"

logging.basicConfig(filename='mylogs.log', filemode='w', level='DEBUG', format=log_format)


def calculateHypoFn(m, b, x_point, y_point, alpha, counter, N):
    m_temp = 0
    b_temp = 0

    for i in range(0, len(x_point)):
        counter = counter + 1
        x = x_point[i]
        y = y_point[i]
        m_temp = m_temp + (x * ((m * x + b) - y))
        b_temp = b_temp + (((m * x) + b) - y)

    m_new = m - (alpha * 2 * m_temp) / N
    b_new = b - (alpha * 2 * b_temp) / N
    return [m_new, b_new, counter]


def error(m, b, x_point, y_point):
    logging.debug("entering into function error")
    totalerror = 0
    result = [0]
    for i in range(0, len(x_point)):
        ydash = m * x_point[i] + b
        totalerror = totalerror + pow((ydash - y_point[i]), 2)
    result.append(totalerror)
    logging.debug("difference is :- %s", "{0:.7f}".format(result[-1] - result[-2]))
    if ("{0:.7f}".format(result[-1] - result[-2])) == "0.0000000":
        logging.debug("Exit from error function with flag as true")
        return True
    else:
        logging.debug("Exit from error function flag as false")
        return False


def calculateCostFn():
    logging.debug("Entering into function calculateCostFn")
    N = 7
    x_point = [1, 2, 3, 4, 5, 6, 7]
    y_point = [3, 4, 5, 6, 7, 8, 9]
    alpha = 0.01
    m = 0
    b = 0
    iterations = 5000
    total = iterations * N
    logging.debug("Value of total is :- %s ", total)
    counter = 0
    for i in range(0, iterations):
        m_trans, b_trans, counter = calculateHypoFn(m, b, x_point, y_point, alpha, counter, N)
        m = m_trans
        b = b_trans
        flag = False
        if int(counter * 10 / total) - (counter * 10 / total) == 0:
            # print("value of counter",counter)
            flag = error(m, b, x_point, y_point)
        if flag:
            break
    logging.debug("value of counter final :- %s", counter)
    logging.debug("value of final parameters m is :- %s and b is :- %s ", round(m), round(b))
    logging.debug("Exit from function calculateCostFn() ")


calculateCostFn()
