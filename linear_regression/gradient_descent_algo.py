import logging
import numpy as np


# calculate parameter for Linear Regression
# only for one input feature
# return theta0, theta1, increment variable
#
def calculateHypoFn(theta, x_point, y_point, alpha, counter, N):
    # initializing the temporary theta with 0
    logging.debug("Enter")
    theta_temp = [0] * len(theta)

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
