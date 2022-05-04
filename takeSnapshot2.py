import cv2, time, dropbox, random

startTime = time.time()


def takeSnapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    number = random.randint(0,100)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        imageName = "image"+ str(number)+".png"
        cv2.imwrite(imageName, frame)
        startTime = time.time
        result = False
    print("Snapshot has been captured")
    return imageName
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def uploadFile(image_name):
    access_token = "H8jWXv_2zeYAAAAAAAAAATDzBIAES5vlM-jl28vMjYOpJW1YIszJAS-ERM0DhfZE"
    file = image_name
    file_from = file
    file_to = "/myWebCamStream/" + (image_name)
    dbx = dropbox.Dropbox(access_token)
    
    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print ("File has been uploaded")


def main():
    while(True):
        if((time.time()) - startTime >= 5):
            name = takeSnapshot()
            uploadFile(name)


main()