// MatrixDisplay.tsx

import React from 'react';

type MatrixProps = {
    matrix: number[][];
};

const MatrixDisplay: React.FC<MatrixProps> = ({ matrix }) => {
    return (
        <div className="border">
            {matrix.map((row, rowIndex) => (
                <div key={rowIndex} className="flex">
                    {row.map((value, colIndex) => (
                        <div
                            key={colIndex}
                            className="w-12 h-12 flex items-center justify-center border"
                            style={{ backgroundColor: `rgba(255, 255, 255, ${value / 7})` }}
                        >
                            {value}
                        </div>
                    ))}
                </div>
            ))}
        </div>
    );
}

export default MatrixDisplay;
