import React, { useState } from 'react'
import FullWidthLayout from '../../../layouts/full_width_layout'
import { PreviewDataTable } from './components/preview_data_table'
import { Test } from './interfaces'
import InsertForm from './components/insert_form';


export default function Cmath() {
  
  const [test, setTest] = useState<Test | null>(null);

  const handleFormSubmit = (data:Test) => {
    setTest(data)
  }

  return (
    <FullWidthLayout>
      <div className='flex flex-wrap px-0 py-3 mx-3 my-3 items-center'>
        <div className='w-full py-1'>
          <InsertForm handleFormSubmit={handleFormSubmit}/>
        </div>
        <div className='w-full py-1'>
          <PreviewDataTable selectedRow={0} test={test}/>
        </div> 
      </div>
    </FullWidthLayout>
  )
}