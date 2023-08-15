export interface Color {
    id: number;
    intensity: number;
    expanded_value: number;
    occurrences: number;
    relative_frecuency: number;
    equalized_value: number;
}

export interface CalculusHelper {
    x1: number;
    y1: number;
    x2: number;
    y2: number;
}

export interface Histogram {
    tasks: string[];
    id: number;
    m: number;
    b: number;
    width: number;
    height: number;
    bits: number;
    img: string;
    temporal_frecuency: number;
    colors: Color[];
    pixels: number;
    calculus_helper: CalculusHelper;
    data_array: number[][];
    filter: number;
    mask_matrix: number[][];
    median_result_matrix: number[][];
    avarage_result_matrix: number[][];
    laplacian_result_matrix: number[][];
    resize_laplacian_result_matrix: number[][];
}

export interface Test {
    id?: number;
    name?: string;
    list: Histogram[];
    type?: string;
}
