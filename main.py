import cv2
import numpy as np


IMG_SIZE = 256
BLUR = np.array(
    [[0.0625, 0.125, 0.0625], [0.125, 0.25, 0.125], [0.0625, 0.125, 0.0625]]
)
EMBOSS = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
OUTLINE = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
SHARPEN = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])


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
    img_path = "sample_image.jpg"

    img = cv2.imread(img_path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    after_img = apply_kernel(
        img,
        OUTLINE,
    )

    cv2.imshow("Before", img)
    cv2.waitKey(0)

    cv2.imshow("After", after_img)
    cv2.waitKey(0)
