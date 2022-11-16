import cv2 as cv

def main(video):
    
    vid = cv.VideoCapture(video) 
    count = 0
    ret = 1
  
    while ret: 

        ret, frame = vid.read() 
        path = "your directory up to this point/Akliss/images"
        cv.imwrite(str(path) + "/frame%d.jpg" % count, frame)
        type(frame)
        count += 1
  
if __name__ == '__main__': 
    main("your video name")