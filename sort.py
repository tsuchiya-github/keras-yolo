import glob


def sort():
    global cnt
    cnt = -1
    global image
    image = []
    global path

    path = sorted(glob.glob("/users/tsuchiya/satreps/public/picture/bangkok/*.jpg"))

    for i in path:
        cnt+=1
        image.append(path[cnt].replace("/users/tsuchiya/satreps/public/picture/bangkok/", ""))

    return image, path