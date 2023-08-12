import React, { useState } from 'react'
import { Test } from '../interfaces';
import axios from 'axios';

type Props = {
  handleFormSubmit: (data:any) => void,
}

const InsertForm = ({handleFormSubmit}: Props) => {

  const initialRequestData: Test = {
    id: 0,
    type: '',
    list: []
  };

  const [requestData, setRequestData] = useState<Test>(initialRequestData);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setRequestData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };
  
  const handleSelectChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const { name, value } = event.target;
    setRequestData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const run_test = () => {
    axios.post(process.env.REACT_APP_API_URL+'/api/monitoreo/test-cmath', requestData)
      .then(response => {
        console.log(response.data);
        handleFormSubmit(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  };

  return (
    <>
      <div className="flex flex-wrap">
        <div className="w-full md:w-1/2">
          <hr />
          <h1 className='p-3'>No logeados</h1>
          <hr />
          <ul className="list-none">
            <li className="hover:bg-gray-200 rounded-md py-2 px-4 cursor-pointer" onClick={run_test}>Run Test</li>
          </ul>
        </div>
      </div>
      
    </>
  );
}

export default InsertForm