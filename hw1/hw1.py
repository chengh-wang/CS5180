import numpy as np

#Boundarie constrains
x_limit = 10
y_limit = 10

#Wall constrains
wall = np.array([(0,5), (2,5), (3,5), (4,5), (5,0), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,9), (5,10), (6,4), (7,4), (9,4), (10,4)])

#actions
actionList = np.array(["LEFT","DOWN","RIGHT","UP"])
action = np.array([(-1, 0),  (0, -1), (1, 0), (0, 1)])

def moveOneStep(s, a):
    
    if a == "LEFT":
        a = np.random.choice(actionList, 1,p = [0.8, 0.1, 0, 0.1])
    elif a == "DOWN":
        a = np.random.choice(actionList, 1,p = [0.1, 0.8, 0.1, 0])
    elif a == "RIGHT":
        a = np.random.choice(actionList, 1,p = [0, 0.1, 0.8, 0.1])
    elif a == "UP":
        a = np.random.choice(actionList, 1,p = [0.1, 0, 0.1, 0.8])

    a_ = np.where(actionList == a)
    a_ = action[a_[0]]

    # print(s)
    s_ = np.add(s, a_)
    print(s_)

    print(np.any(wall[:, :] == s_))

    if np.any(wall[:, :] == s_):
        s_ = s
    
        

    print(s_)
    return s_


def main():
    print(moveOneStep((10,10),"UP"))

if __name__ == "__main__":
    main()




# def simulate(s, a):



