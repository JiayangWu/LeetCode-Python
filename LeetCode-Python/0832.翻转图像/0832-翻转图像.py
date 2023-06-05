class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(image):
            image[i] = row[::-1]

        for i in range(len(image)):
            for j in range(len(image)):
                image[i][j] = 1 - image[i][j]
        return image