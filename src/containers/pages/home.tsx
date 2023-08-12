import React from 'react'
import { BasicCard } from '../../components/items/basic_card'
import FullWidthLayout from '../../layouts/full_width_layout'

export default function Home() {
  return (
    <FullWidthLayout>
      <div className='flex flex-wrap px-3 py-3 mx-3 my-3 items-center bg-cyan-500'>
        <div className='p-2 w-full sm:w-1/2 md:w-1/3 xl:w-1/4 '>
          <BasicCard/>
        </div>
        <div className='p-2 w-full sm:w-1/2 md:w-1/3 xl:w-1/4 '>
          <BasicCard/>
        </div>
        <div className='p-2 w-full sm:w-1/2 md:w-1/3 xl:w-1/4 '>
          <BasicCard/>
        </div>
        <div className='p-2 w-full sm:w-1/2 md:w-1/3 xl:w-1/4 '>
          <BasicCard/>
        </div>
        <div className='p-2 w-full sm:w-1/2 md:w-1/3 xl:w-1/4 '>
          <BasicCard/>
        </div>
        <div className='p-2 w-full sm:w-1/2 md:w-1/3 xl:w-1/4 '>
          <BasicCard/>
        </div>
      </div>
    </FullWidthLayout>
  )
}
