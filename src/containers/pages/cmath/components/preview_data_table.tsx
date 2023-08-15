import classNames from 'classnames'
import React, { useState } from 'react'
import { Color, CalculusHelper, Histogram, Test } from '../interfaces'
import { HiCheck, HiX } from 'react-icons/hi'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';  // <-- Import the chart type you want
import MatrixDisplay from './matrix_display';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

type Props = {
  selectedRow: number,
  test: Test | null
}

export const PreviewDataTable = ({test, selectedRow}: Props) => {

  const [isOpen, setIsOpen] = useState(false);
  
  const handleColorClick = (color: Color) => {
    setIsOpen(false)
  };

  const handleHistogramClick = (histogram: Histogram) => {
    setIsOpen(false)
  };

  const options : any = {
    legend: {
      display: true,
      position: 'top',
      labels: {
        fontColor: 'rgb(0, 0, 0)'
      }
    }
  };

  const createChartData = (colors: Color[], value: keyof Color, key: keyof Color) => {

    // aqui ordeno los colores por intensidad
    
    colors = colors.sort((a, b) => a[key] - b[key])
    
    

    // aqui busco si algun color tiene la misma intensidad y si es asi le sumo la ocurrencia
    // colors = colors.reduce((acc: Color[], color: Color) => {
    //   const index = acc.findIndex(c => c.intensity === color.intensity)
    //   if (index === -1) {
    //     acc.push(color)
    //   } else {
    //     acc[index].occurrences += color.occurrences
    //   }
    //   return acc
    // }, [])

    return {
      labels: colors.map(color => `C${color.intensity}`),
      datasets: [
        { 
          label: 'Ocurriencias',
          key: colors.map(color => color['intensity']),
          data: colors.map(color => color[value]),
          backgroundColor: 'rgba(75,192,192,0.2)',
          borderColor: 'rgba(75,192,192,1)',
          borderWidth: 1
        }
      ]
    };
  }

  return (
    <>
      <div className="p-3 bg-gray-300 text-center">
        <h2 className="text-2xl font-bold">{test?.name}</h2>
        <p className="mt-2">free text space</p>
      </div>

      <hr className='pt-5'/>

      {test?.list.map((histogram: Histogram, index: number) => (
        <div className='pt-5 flex flex-wrap' key={index}>
          {/* ... Rest of your code inside map */}
          {histogram.colors.length > 0 ? (
            <div className='w-full md:w-1/2 pt-5 flex flex-wrap'>
              <div className="w-full md:w-1/2 p-4">
                <h3 className="text-xl font-bold mb-4">Intensity Chart</h3>
                <Bar options={options} data={createChartData(histogram.colors, 'occurrences', 'intensity')} />
              </div>

              <div className="w-full md:w-1/2 p-4">
                <h3 className="text-xl font-bold mb-4">Expanded Value Chart</h3>
                <Bar options={options} data={createChartData(histogram.colors, 'occurrences', 'expanded_value')} />
              </div>
          </div>
          ): <></>}

          {(histogram.data_array.length > 0 && histogram.median_result_matrix.length > 0) ? (
            <div className='w-full md:w-1/2 pt-5 flex flex-wrap'>
              <h1>MEDIANA</h1>
              <div className='w-full flex flex-wrap'>
                <div className="w-full md:w-1/2 p-4">
                  <h3 className="text-xl font-bold mb-4">Original Colors</h3>
                  <MatrixDisplay matrix={histogram.data_array} /> 
                </div>

                <div className="w-full md:w-1/2 p-4">
                  <h3 className="text-xl font-bold mb-4">Filtered</h3>
                  <MatrixDisplay matrix={histogram.median_result_matrix} />             
                </div>
              </div>
              
            </div>
          ): <></>}

          {(histogram.data_array.length > 0 && histogram.avarage_result_matrix.length > 0) ? (
            
            <div className='w-full md:w-1/2 pt-5 flex flex-wrap'>
              <h1>LA MEDIA</h1>
              <div className='w-full flex flex-wrap'>
                <div className="w-full md:w-1/2 p-4">
                  <h3 className="text-xl font-bold mb-4">Original Colors</h3>
                  <MatrixDisplay matrix={histogram.data_array} /> 
                </div>

                <div className="w-full md:w-1/2 p-4">
                  <h3 className="text-xl font-bold mb-4">Filtered</h3>
                  <MatrixDisplay matrix={histogram.avarage_result_matrix} />             
                </div>
              </div>
              
            </div>
          ): <></>}

          {(histogram.data_array.length > 0 && histogram.laplacian_result_matrix.length > 0) ? (
            
            <div className='w-full md:w-1/2 pt-5 flex flex-wrap'>
              <h1>LA LAPLACIAN</h1>
              <div className='w-full flex flex-wrap'>
                <div className="w-full md:w-1/2 p-4">
                  <h3 className="text-xl font-bold mb-4">Original Colors</h3>
                  <MatrixDisplay matrix={histogram.data_array} /> 
                </div>

                <div className="w-full md:w-1/2 p-4">
                  <h3 className="text-xl font-bold mb-4">Filtered</h3>
                  <MatrixDisplay matrix={histogram.laplacian_result_matrix} />             
                </div>

                <div className="w-full md:w-1/2 p-4">
                  <h3 className="text-xl font-bold mb-4">Resized</h3>
                  <MatrixDisplay matrix={histogram.resize_laplacian_result_matrix} />             
                </div>
              </div>
              
            </div>
          ): <></>}
          
          
          {/* ... Rest of your code inside map */}
          {histogram.colors.length > 0 ? (
          <div className='w-full md:w-1/2 pt-5'>
            <div className="p-3 bg-gray-300 text-center">
              <h2 className="text-2xl font-bold">Histogram {index}</h2>
            </div>
            <div key={histogram.id} className="overflow-x-scroll">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Intensidad
                    </th>
                    <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Frecuencia relativa
                    </th>
                    <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Ocurrencias
                    </th>
                    <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Valor expandido
                    </th>
                    <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Valor ecualizado
                    </th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {histogram.colors.map((color: Color) => (
                    <tr
                      key={color.id}
                      onClick={() => handleColorClick(color)}
                    >
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">C{color.intensity}</td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{color.relative_frecuency}</td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{color.occurrences}</td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{color.expanded_value}</td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{color.equalized_value}</td>
                      
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

          </div>
          ): <></>}
        </div>
      ))}
    </>
  )
}