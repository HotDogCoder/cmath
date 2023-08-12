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
        self.median_result_matrix: list[list[int]] = []
        self.avarage_result_matrix: list[list[int]] = []

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
            'avarage_result_matrix': self.avarage_result_matrix
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

    def set_average_filter_from_mask_matrix(self, data_matrix=[]):
        # Apply average or mean filter
        filtered_matrix = medfilt2d(np.array(data_matrix), kernel_size=3)
        print("\nFiltered matrix:")
        self.avarage_result_matrix = filtered_matrix.tolist()