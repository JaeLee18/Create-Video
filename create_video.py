import cv2
import os
image_folder = '/path/folder'
video_name = '/path/for/video'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
images.sort(key=lambda x: int(x.split(".")[0]))

for image in images:
    img_name = os.path.join(image_folder, image)
    load_img = cv2.imread(img_name)
    try:
        a = 1
    except:
        print("X ", img_name)
        os.remove(img_name)

for image in images:
    img_name = os.path.join(image_folder, image)
    print("Resizing ", img_name, " to 512 X 512")
    load_img = cv2.imread(img_name)
    resized_image = cv2.resize(load_img, (512, 512))

    cv2.imwrite(img_name, resized_image)


frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
FrameSize = (frame.shape[1], frame.shape[0])
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*"MJPG"), 24, (512, 512))

for image in images:
    img_name = os.path.join(image_folder, image)
    video.write(cv2.imread(img_name))
cv2.destroyAllWindows()
print("release video")
video.release()


