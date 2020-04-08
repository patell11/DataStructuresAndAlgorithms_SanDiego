import numpy as np

def gradeintDescent(x,y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.01

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        #print("y_predicted {}".format(y_predicted))
        cost = (1.0/n) * sum([val**2 for val in (y-y_predicted)])
        #print(y-y_predicted, x * (y-y_predicted), sum(x * (y-y_predicted)), 2.0/n)
        dm = -(2.0/n) * sum( x * (y-y_predicted))
        dy = -(2.0/n) * sum( y - y_predicted)
        m_curr = m_curr - learning_rate * dm
        b_curr = b_curr - learning_rate * dy
        #print("dm {}, dy {}, m_curr {}, b_curr {}".format(dm,dy,m_curr, b_curr))
        print ("m {}, b {}, cost {} ,iteration {}".format(m_curr,b_curr,cost,i))
        print("--------------------------------------")

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
gradeintDescent(x,y)

