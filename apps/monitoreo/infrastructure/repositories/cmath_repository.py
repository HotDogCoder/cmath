from apps.monitoreo.application.repositories_interfaces.cmath_repository_interface import CmathRepositoryInterface
from apps.monitoreo.domain.models.cmath_model import CmathModel
from core.domain.helpers.calculus_helper import CalculusHelper
from core.domain.models.color import Color
from core.domain.models.histogram import Histogram
class CmathRepository(CmathRepositoryInterface):
    def __init__(self):
        super().__init__()

    def test_cmath(self, cmath_model: CmathModel):
        for index, histogram in enumerate(cmath_model.list, start=0):

            print("--------------")
            print(f"test {index + 1}")
            print("--------------")
            
            

            
            if 'expand' in histogram.tasks:

                if histogram.pixels == 0:
                    histogram.get_pixels_count()
                print(f'pixels: {histogram.pixels}')

                histogram.m = histogram.calculus_helper.get_line_pendient()
                # imprime la pendiente y la ordenada al origen
                print(f'pendiente: {histogram.m}')

                histogram.b = histogram.get_line_order_expanded(histogram.m)
                
                print(f'ordenada al origen: {histogram.b}')

                histogram.expand_colors(
                    m=histogram.m,
                    b=histogram.b
                )

                if 'equalize' in histogram.tasks:

                    histogram.equalize_colors()

            if len(histogram.data_array) > 0 and 'set_median_filter_from_mask_matrix' in histogram.tasks:
                histogram.set_median_filter_from_mask_matrix(
                    data_matrix=histogram.data_array,
                    filter=histogram.filter,
                    matrix=histogram.mask_matrix
                )

            if len(histogram.data_array) > 0 and 'set_average_filter_from_mask_matrix' in histogram.tasks:
                histogram.set_average_filter_from_mask_matrix()


            if len(histogram.data_array) > 0 and 'set_laplacian_filter_from_mask_matrix' in histogram.tasks:
                histogram.set_laplacian_filter_from_mask_matrix()

        return cmath_model

    def set_test_list(self, cmath_model: CmathModel):
        cmath_model.list = [
            
            Histogram(
                tasks=['equalize', 'expand'],
                id=2,
                colors = [
                    Color(id=1, intensity=0, expanded_value=0.0, occurrences=0),
                    Color(id=2, intensity=1, expanded_value=0.0, occurrences=25),
                    Color(id=3, intensity=2, expanded_value=0.0, occurrences=24),
                    Color(id=4, intensity=3, expanded_value=0.0, occurrences=30),
                    Color(id=5, intensity=4, expanded_value=0.0, occurrences=50),
                    Color(id=6, intensity=5, expanded_value=0.0, occurrences=15),
                    Color(id=7, intensity=6, expanded_value=0.0, occurrences=0),
                    Color(id=8, intensity=7, expanded_value=0.0, occurrences=0),
                ],
                calculus_helper=CalculusHelper(x1=3, y1=1, x2=7, y2=7)
            ),
            Histogram(
                tasks=['equalize', 'expand'],
                id=1,
                colors = [
                    Color(id=1, intensity=0, expanded_value=0.0, occurrences=12),
                    Color(id=2, intensity=1, expanded_value=0.0, occurrences=6),
                    Color(id=3, intensity=2, expanded_value=0.0, occurrences=36),
                    Color(id=4, intensity=3, expanded_value=0.0, occurrences=12),
                    Color(id=5, intensity=4, expanded_value=0.0, occurrences=48),
                    Color(id=6, intensity=5, expanded_value=0.0, occurrences=24),
                    Color(id=7, intensity=6, expanded_value=0.0, occurrences=6),
                    Color(id=8, intensity=7, expanded_value=0.0, occurrences=6),
                ],
                calculus_helper=CalculusHelper(x1=3, y1=1, x2=7, y2=7)
            ),
            Histogram(
                mask_matrix=[
                    [1, 2, 1],
                    [2, 4, 2],
                    [1, 2, 1]
                ],
                filter=1/16,
                tasks=['set_median_filter_from_mask_matrix', 'set_average_filter_from_mask_matrix'],
                id=3,
                data_array=[
                    [5,	4,	6,	6,	1],
                    [3,	3,	1,	0,	1],
                    [6,	0,	0,	1,	1],
                    [2,	2,	2,	3,	3],
                    [4,	4,	0,	2,	1]

                ]
            )
            # Histogram(
            #     mask_matrix=[
            #         [1,1,1],
            #         [1,8,1],
            #         [1,1,1]
            #     ],
            #     filter=1,
            #     tasks=['set_laplacian_filter_from_mask_matrix'],
            #     id=4,
            #     data_array=[
            #         [4,4,3,2],
            #         [7,7,6,6],
            #         [4,1,2,3],
            #         [2,5,1,2]
            #     ]
            # )
        ]

