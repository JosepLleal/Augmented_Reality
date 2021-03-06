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
    print(arr)

    m1 = arr[0,:].mean()
    arr[0,:] = arr[0,:] - m1

    m2 = arr[1,:].mean()
    arr[1,:] = arr[1,:] - m2
    
    m3 = arr[2,:].mean()
    arr[2,:] = arr[2,:] - m3

    m4 = arr[3,:].mean()
    arr[3,:] = arr[3,:] - m4

    m5 = arr[4,:].mean()
    arr[4,:] = arr[4,:] - m5

    print(arr)


def ex15():
    arr = np.random.uniform(0,1,(5,5))
    a = 0.5
    index = (np.abs(arr-a)).argmin()
    print(arr)
    arr = arr.flatten()
    print(arr[index])


def ex16():
    arr = np.random.randint(0,10,9)
    arr = arr.reshape(3,3)

    greater = arr[arr>5]
    print(greater)
    print(len(greater))

def ex17():
    arr = np.zeros((64, 64))
    a = np.arange(0,255, 4)
    arr = arr + a
    arr = np.uint8(arr)

    cv2.imshow('Gradient', arr)
    cv2.waitKey(0)


def ex18():
    arr = np.zeros(shape=(64, 64))
    a = np.arange(0,255, 4)
    a = a.reshape((64,1))
    arr = arr + a
    arr = np.uint8(arr)

    cv2.imshow('Gradient', arr)
    cv2.waitKey(0)


def ex19():
    arr = np.zeros(shape=(64, 64, 3))
    arr[:] = 255
    arr[:, :, 0] = 0
    arr = np.uint8(arr)

    cv2.imshow('Yellow', arr)
    cv2.waitKey(0)


def ex20():
    arr = np.zeros(shape=(64, 64, 3))
    arr[:] = 255
    arr[0:31, 0:31, 0] = 0
    arr[32:64, 32:64, 2] = 0
    arr = np.uint8(arr)

    cv2.imshow('Squares', arr)
    k = cv2.waitKey(0)

    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.destroyAllWindows()


def ex21():
    img = cv2.imread('marvel.png', cv2.IMREAD_ANYCOLOR)

    img[::2, :] = 0.0

    cv2.imshow('Lines', img)
    cv2.waitKey(0)

#------------------------------------------------------------------------------------------------

def convolve(img, krn, ksize, krad):

    height, width, depth = img.shape
    
    frm = np.ones((height + krad*2,                   
     width + krad*2,
     depth))
    frm[krad: -krad, krad: -krad] = img

    #filteted image(output)
    filter = np.zeros(img.shape)
    for i in range (0, height):
        for j in range (0,width):
            filter[i,j] = (frm[i:i+ksize, j:j+ksize]*krn[:,:,np.newaxis]).sum(axis=(0,1))


    return filter



def GaussKernel(krad):

    ksize = krad*2+1
    krn = np.zeros((ksize, ksize))
    sigma = krad/3

    for i in range(0, ksize):
        for j in range(0,ksize):
            d = np.sqrt((krad - i)**2 + (krad - j)**2)
            krn[i,j] = np.exp(-(d**2/(2.0*sigma**2)))

    krn /= krn.sum()

    return krn


#Gradients Computation
def GaussianFilter(img):
    ksize = 31
    krad = int(ksize/2)
    krn = GaussKernel(krad)

    return convolve(img, krn, ksize, krad)

def ConvolveGrayScale(img, krn):



    return

def SobelFilter(img):

    hkrn = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]])

    vkrn = np.array([  
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]])
      
    
    Gx = ConvolveGrayScale(img, hkrn)
    Gy = ConvolveGrayScale(img, vkrn)

    return Gx, Gy


def main():
    img = cv2.imread("marvel.png", cv2.IMREAD_ANYCOLOR)
    img = img / 255.0

    filtered = GaussianFilter(img)



    cv2.imshow("Original",img)
    cv2.imshow("Filtered", filtered)

    cv2.waitKey(0)

main()

