import numpy as np
from scipy.signal import convolve2d, medfilt2d
from core.domain.helpers.calculus_helper import CalculusHelper
from core.domain.models.color import Color


class Histogram:

    def __init__(self, tasks=['equalize', 'expand_colors', 'set_filter_from_mask_matrix'], id=0, calculus_helper = CalculusHelper(), colors = [], filter=1.0, mask_matrix=[], data_array=[]):
        self.tasks = tasks
        self.id: int = id
        self.m: float = 0.0
        self.b: float = 0.0
        self.width: int = 0
        self.height: int = 0
        self.bits: int = 0
        self.img: str = ''
        self.temporal_frecuency: float = 0.0
        self.colors: list[Color] = colors
        self.pixels: int = 0
        self.calculus_helper: CalculusHelper = calculus_helper
        self.data_array: list[list[int]] = data_array
        self.filter: float = filter
        self.mask_matrix: list[list[float]] = mask_matrix
        self.mask_middle: list = None
        self.mask_sub_array: list[list[int]] = []
        self.median_result_matrix: list[list[int]] = []
        self.avarage_result_matrix: list[list[int]] = []
        self.laplacian_result_matrix: list[list[int]] = []
        self.resize_laplacian_result_matrix: list[list[int]] = []

        if self.width > 0 and self.height > 0:
            self.bits = self.width * self.height

    def to_dict(self):
        return {
            'width': self.width,
            'height': self.height,
            'bits': self.bits,
            'img': self.img,
            'temporal_frecuency': self.temporal_frecuency,
            'colors': [color.to_dict() for color in self.colors],
            'pixels': self.pixels,
            'calculus_helper': self.calculus_helper.to_dict(),
            'm': self.m,
            'b': self.b,
            'id': self.id,
            'filter': self.filter,
            'mask_matrix': self.mask_matrix,
            'median_result_matrix': self.median_result_matrix,
            'data_array': self.data_array,
            'avarage_result_matrix': self.avarage_result_matrix,
            #'mask_middle': self.mask_middle,
            #'mask_sub_array': self.mask_sub_array,
            #'laplacian_result_matrix': self.laplacian_result_matrix,
            #'resize_laplacian_result_matrix': self.resize_laplacian_result_matrix,
        }

    def store_test_colors(self):
        colors = [
            Color(intensity=0, expanded_value=0.0, occurrences=0),
            Color(intensity=1, expanded_value=0.0, occurrences=1),
            Color(intensity=2, expanded_value=0.0, occurrences=2),
            Color(intensity=3, expanded_value=0.0, occurrences=63),
            Color(intensity=4, expanded_value=0.0, occurrences=0),
            Color(intensity=5, expanded_value=0.0, occurrences=45),
            Color(intensity=6, expanded_value=0.0, occurrences=42),
            Color(intensity=7, expanded_value=0.0, occurrences=60),
        ]

        self.colors = colors

    def get_line_order_expanded(self, m):
        b = (m * self.calculus_helper.x1 - self.calculus_helper.y1)*-1
        return b
    
    def expand_colors(self, m, b):
        for color in self.colors:
            y = self.calculus_helper.get_y(m, b, color.intensity)
            if y > 0 and color.occurrences > 0:
                color.expanded_value = round(y)
            else:
                color.expanded_value = 0
        return y
    
    def equalize_colors(self):
        self.temporal_frecuency = 0.0
        for color in self.colors:
            color.relative_frecuency = color.occurrences / self.pixels
            color.equalized_value = round((len(self.colors)-1)*(self.temporal_frecuency + color.relative_frecuency))
            self.temporal_frecuency += color.relative_frecuency

    def get_pixels_count(self):

        for color in self.colors:
            self.pixels += color.occurrences

    def set_median_filter_from_mask_matrix(self, data_matrix=[], filter=1.0, matrix=[[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0,1.0,1.0]]):
        mask = np.array(matrix) * filter
        # Apply convolution
        filtered_matrix = convolve2d(data_matrix, mask, mode='same', boundary='fill', fillvalue=0)
        print("\nFiltered matrix:")
        result = np.round(filtered_matrix).astype(int)
        self.median_result_matrix = result.tolist()

    def get_middle_node(self):
        col = 1
        row = 1
        node = self.mask_matrix[1][1]
        self.mask_middle = node, row, col

    def get_target_array(self, row, col):
        self.get_middle_node()
        mask_middle_node, mask_middle_row, mask_middle_col = self.mask_middle

        mask_matrix_row_variation = len(self.mask_matrix) - (mask_middle_row + 1)
        mask_matrix_col_variation = len(self.mask_matrix[0]) - (mask_middle_col + 1)


        target = self.data_array[row][col]
        right_limit = col + mask_matrix_col_variation
        bottom_limit = row + mask_matrix_row_variation
        left_limit = 0
        top_limit = 0

        if row == 0:
            top_limit = 0
            bottom_limit = row + mask_matrix_row_variation

            pass
        if col == 0:
            left_limit = 0
            bottom_limit = row + mask_matrix_row_variation
            pass
        if col == 0 and row == 0:
            left_limit = 0
            top_limit = 0
            bottom_limit = row + mask_matrix_row_variation
            right_limit = col + mask_matrix_col_variation
        if col == len(self.data_array[0])-1:
            right_limit = len(self.data_array[0])-1
            pass
        if row == len(self.data_array)-1:
            bottom_limit = len(self.data_array)-1
            pass
        if col == len(self.data_array[0])-1 and row == len(self.data_array)-1:
            right_limit = len(self.data_array[0])-1
            bottom_limit = len(self.data_array)-1
            left_limit = col - mask_matrix_col_variation
            top_limit = row - mask_matrix_row_variation
            pass

        # Fetch points inside the coordinates (1,2) to (3,4)
        # sub_array = self.data_array[1:4, 2:5]
        sub_array = [row[left_limit:(right_limit + 1)] for row in self.data_array[top_limit:(bottom_limit + 1)]]
        self.mask_sub_array = sub_array
        # self.
        

    def set_average_filter_from_mask_matrix(self):

        arr_zeros = np.zeros((len(self.data_array), len(self.data_array[0]))).tolist()
        self.avarage_result_matrix = arr_zeros
        for row_index, row in enumerate(self.data_array):
            for col_index, col in enumerate(row):
                self.get_target_array(row_index, col_index)

                sorted_arr = sorted(self.mask_sub_array)

                try:
                    mean = np.mean(sorted_arr)
                    self.avarage_result_matrix[row_index][col_index] = round(mean)
                except:
                    pass    

    def resize_matrix(self):

        old_array = np.array(self.data_array)
        old_max = np.max(old_array)
        old_min = np.min(old_array)

        new_array = np.array(self.laplacian_result_matrix)
        new_max = np.max(new_array)
        new_min = np.min(new_array)

        self.calculus_helper.x1 = new_min
        self.calculus_helper.x2 = new_max
        self.calculus_helper.y1 = old_min
        self.calculus_helper.y2 = old_max

        m = self.calculus_helper.get_line_pendient()

        self.resize_laplacian_result_matrix = np.zeros((len(self.data_array), len(self.data_array[0]))).tolist()

        for row_index, row in enumerate(self.laplacian_result_matrix):
            for col_index, col in enumerate(row):
                b = self.get_line_order_expanded(m)
                y = self.calculus_helper.get_y(m, b, col)
                self.resize_laplacian_result_matrix[row_index][col_index] = round(y)
        
        self.resize_laplacian_result_matrix = np.round(self.resize_laplacian_result_matrix).astype(int)


    def set_laplacian_filter_from_mask_matrix(self):

        # Datos proporcionados
        data = self.data_array

        # Máscara laplaciana
        mask = self.mask_matrix

        # Convertir listas a arrays de NumPy
        data_array = np.array(data)
        mask_array = np.array(mask)

        # Aplicar la convolución con el filtro laplaciano
        result = convolve2d(data_array, mask_array, mode='same', boundary='fill', fillvalue=0)
        result = np.round(result).astype(int)
        self.laplacian_result_matrix = result.tolist()

        self.resize_matrix()

                        