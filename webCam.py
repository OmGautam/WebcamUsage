import cv2
import random
import time
import dropbox

startTime = time.time()

def capture():
    video = cv2.VideoCapture(0)
    result = True
    number = random.randint(1,9)
    while(result):
        ret,frame = video.read()
        imageName = "img" + str(number) + ".png"
        cv2.imwrite(imageName, frame)
        result = False
    return imageName
    print("Video captured")
    video.release()
    cv2.destroyAllWindows()

capture()

def upload(imageName):
    access_token = 'UT63PJLuaAwAAAAAAAAAARPJNcOhx_hSmUMx10iLplZWTJ0nRhl33Ux0QVwMUJZD'
    file = imageName
    fileFrom = file
    fileTo = "/Folder1/" + (imageName)
    dbx = dropbox.Dropbox(access_token)
    with open(fileFrom, 'rb') as f:
        dbx.files_upload(f.read(),fileTo,mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while(True):
        if (time.time()-startTime) >= 5:
            name = capture()
            upload(name)

main()


    