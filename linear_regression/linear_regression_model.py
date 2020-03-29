import logging
from gradient_descent_algo import *

log_format = "%(asctime)s::" \
             "%(lineno)d::%(message)s"

logging.basicConfig(filename='mylogs.log', filemode='w', level='DEBUG', format=log_format)


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
    x_point = [[1], [2], [3], [4], [5], [6], [7]]
    y_point = [3, 4, 5, 6, 7, 8, 9]
    alpha = 0.01
    # equation of line y = mx + b => y(o/p) =  m(0).x(0) + m(1).x(1)  assumption x(0) = 0
    theta = [0] * (len(x_point[0])+1)
    iterations = 5000
    total = iterations * N
    logging.debug("Value of total is :- %s ", total)
    counter = 0
    for i in range(0, iterations):
        predicted_theta, counter = calculateHypoFn(theta, x_point, y_point, alpha, counter, N)

        for i in range(0, len(theta)):
            theta[i] = predicted_theta[i]

        flag = False
        if int(counter * 10 / total) - (counter * 10 / total) == 0:
            flag = error(theta[1], theta[0], x_point, y_point)
        if flag:
            break
    logging.debug("value of counter final :- %s", counter)
    logging.debug("value of final parameters m is :- %s and b is :- %s ", round(theta[1]), round(theta[0]))
    logging.debug("Exit from function calculateCostFn() ")


calculateCostFn()
