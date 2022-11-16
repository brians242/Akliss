import cv2 as cv

def main(video):
    
    vid = cv.VideoCapture(video) 
    count = 0
    ret = 1
  
    while ret: 

        ret, frame = vid.read() 
        path = "enter pwd into your terminal, should end with /Akliss/images and replace this"
        cv.imwrite(str(path) + "/frame%d.jpg" % count, frame)
        type(frame)
        count += 1
  
if __name__ == '__main__': 
    main("your video name")