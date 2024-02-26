import numpy as np
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped_image = np.fliplr(image)
        for i in range(len(flipped_image)):
            for j in range(len(flipped_image[i])):
                if flipped_image[i][j] == 0:
                    flipped_image[i][j] = 1
                else:
                    flipped_image[i][j] =0
        return flipped_image