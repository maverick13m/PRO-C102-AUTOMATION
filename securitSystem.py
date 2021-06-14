import cv2

def take_screenshot():
    #initializing cv2
    #This will return video from the first webcam on your computer.
    #if you have miultple webcams, each will have a number and you need to mention accordingly
    videoCaptureObject = cv2.VideoCapture(0)
    print("captured")

    result =True
    # used to read the frames
    # read() is used: ret is dummy variable(bool value)- to indicate something is being returned or not
    while(result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObject.read()
        print("done with frame")

        #cv2.imwrite()- to save an image to any storage device
        cv2.imwrite("NewPic44.jpg",frame)
        print("taken new pic")

        result = False

    #release the camera
    videoCaptureObject.release()
    print("cam released")
   
    #close all windows that might be opened while this is processing
    cv2.destroyAllWindows() 
    print("all windows closed")
    
take_screenshot()
