import sys
from os import path
import cv2
import numpy as np


IMG_SIZE = 256

KERNELS = {
    "blur": np.array([[0.0625, 0.125, 0.0625], [0.125, 0.25, 0.125], [0.0625, 0.125, 0.0625]]),
    "emboss": np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]),
    "outline": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]),
    "sharpen": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
}


def apply_kernel(image, kernel):
    def get_matrix(x, y):
        return np.array(
            [
                [image[x - 1][y - 1], image[x - 1][y], image[x - 1][y + 1]],
                [image[x][y - 1], image[x][y], image[x][y + 1]],
                [image[x + 1][y - 1], image[x + 1][y], image[x + 1][y + 1]],
            ]
        )

    after_image = np.zeros((IMG_SIZE, IMG_SIZE))

    for i in range(1, IMG_SIZE - 1):
        for j in range(1, IMG_SIZE - 1):
            after_image[i][j] = np.sum(get_matrix(i, j) * kernel) / 255

    return after_image


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Error: Please provide the correct number of arguments to the program.")
        sys.exit(1)

    img_path = sys.argv[1]
    kernel = KERNELS.get(sys.argv[2].lower())

    if not path.isfile(img_path):
        print("Error: File could not be found. Please provide a valid file path.")
        sys.exit(1)

    if kernel is None:
        print("Error: Please provide a valid kernel to apply to the image.")
        sys.exit(1)

    resulting_img_path = "resulting_image.jpg"
    img = cv2.imread(img_path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    after_img = apply_kernel(
        img,
        kernel,
    )

    compare_img = np.zeros((IMG_SIZE, IMG_SIZE * 2))
    for i in range(0, IMG_SIZE):
        for j in range(0, IMG_SIZE * 2):
            compare_img[i][j] = img[i][j] / 255 if j < IMG_SIZE else after_img[i][j - IMG_SIZE]

    cv2.imshow("Before", img)
    cv2.waitKey(0)

    cv2.imshow("After", after_img)
    cv2.waitKey(0)

    cv2.imshow("Comparison", compare_img)
    cv2.waitKey(0)

    cv2.imwrite("example_image.jpg", img)
    cv2.imwrite(resulting_img_path, after_img * 255)

    cv2.destroyAllWindows()
