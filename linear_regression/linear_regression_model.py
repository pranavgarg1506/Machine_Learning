import logging
import numpy as np

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
    theta = [0] * (len(x_point[0]) + 1)
    iterations = 5000
    total = iterations * N
    logging.debug("Value of total is :- %s ", total)
    counter = 0
    for i in range(0, iterations):
        predicted_theta, counter = calculateHypoFn(theta, x_point, y_point, alpha, counter, N)

        for j in range(0, len(theta)):
            theta[j] = predicted_theta[j]

        flag = False
        if int(counter * 10 / total) - (counter * 10 / total) == 0:
            flag = error(theta[1], theta[0], x_point, y_point)
        if flag:
            break
    logging.debug("value of counter final :- %s", counter)
    logging.debug("value of final parameters m is :- %s and b is :- %s ", round(theta[1]), round(theta[0]))
    logging.debug("Exit from function calculateCostFn() ")


def calculateHypoFn(theta, x_point, y_point, alpha, counter, N):
    # initializing the temporary theta with 0
    logging.debug("Enter")
    theta_temp = [0] * len(theta)

    i: int
    for i in range(0, len(y_point)):
        counter = counter + 1
        x = x_point[i]
        y = y_point[i]
        temp_x = list(x)
        temp_x.insert(0, 1)
        for i in range(0, len(temp_x)):
            theta_temp[i] = theta_temp[i] + ((temp_x * np.transpose(theta)) - y)

    predicted_theta = [0] * len(theta)

    for i in range(0, len(theta)):
        predicted_theta[i] = theta[i] - (alpha * 2 * theta_temp[i]) / N

    return [predicted_theta, counter]


calculateCostFn()
