import cv2
import numpy as np 

def ex1():
    arr = np.zeros(10)
    print(arr)

def ex2():
    arr = np.zeros(10)
    arr[4] = 1
    print(arr)

def ex3():
    arr = np.arange(10.0, 50.0)
    print(arr)

def ex4():
    arr = np.arange(1, 10)
    arr = arr.reshape((3,3))   
    print(arr)

def ex5():
    arr = np.arange(1, 10)
    arr = arr.reshape((3, 3))  
    arr = np.flip(arr, 1) #flips it vertically by default (0) and horizontally with (1)
    print(arr)

def ex9():
    arr = np.random.randint(0,100,10)
    average = arr.mean()
    print(arr)
    print(average)

def ex10():
    arr = np.ones((5,5))
    arr[1:-1, 1:-1] = 0
    print(arr)

def ex11():
    arr = np.ones((5,5))
    arr += np.arange(5)
    print(arr)

def ex12():
    arr = np.random.randint(0,100,9)
    arr = np.float64(arr.reshape(3,3))
    print(arr)

def ex13():
    arr = np.random.randint(0,100,25)
    arr = arr.reshape(5,5)
    average = arr.mean()
    arr1 = arr - average
    print(arr)
    print(average)
    print(arr1)

def ex14():
    arr = np.random.randint(0,100,25)
    arr = arr.reshape(5,5)
    #(arr[1, :]).mean() IN PROGRESS
    print(arr)
    print(average1)


ex14()