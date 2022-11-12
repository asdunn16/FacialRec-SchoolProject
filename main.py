from PIL import Image, ImageDraw
import face_recognition

# load the jpg file
people = face_recognition.load_image_file('people.jpg')
me = face_recognition.load_image_file('me.jpg')
unknown = face_recognition.load_image_file('check_for_me.jpg')


def show_faces(image):
    # find location of all the faces in the image
    face_locations = face_recognition.face_locations(image)

    # count number of faces
    number_of_faces = len(face_locations)
    print("Found {} face(s) in this picture.".format(number_of_faces))

    # load the image into a Python Image Library object
    pil_image = Image.fromarray(image)

    # copy image to draw
    image_copy = pil_image.copy()

    # loop through faces
    for face_location in face_locations:
        # print the location of each face in this image.
        print('A face is located at pixel location Top: {}, Left {},Bottom: {}, Right: {}'
              .format(face_location[0], face_location[1], face_location[2], face_location[3]))

        # draw a box around the face
        image_copy_draw = ImageDraw.Draw(image_copy)
        image_copy_draw.rectangle([face_location[3], face_location[0], face_location[1], face_location[2]],
                                  outline="red", width=3)

    # display the image on screen
    image_copy.show()


def check_face(encode_image, image):
    face_encoding = face_recognition.face_encodings(encode_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(image)[0]

    results = face_recognition.compare_faces([face_encoding], unknown_face_encoding)

    if results[0]:
        print('That person is in the photo.')
    else:
        print('That person is not in the photo.')


# locate faces
# show_faces(people)
# show_faces(me)
# show_faces(unknown)

# check if face is in photo
check_face(me, unknown)
check_face(me, people)
