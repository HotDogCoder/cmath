import React from "react"
import { HiChevronDoubleDown, HiChevronDown, HiOutlineTrash, HiSearch } from "react-icons/hi"
import Dropdown from "../dropdown/dropdown"
import DropdownList from "../dropdown/dropdown_list"

export const BasicCard = () => {


    return (
        <>
        
            <div className="w-full flex bordered bg-blue-200 flex-wrap">
                <div className="w-full bg-red-200">
                    <div className="h-40 w-full">
                        <img className="h-full w-full object-fit bg-blue-100" src="" alt="" />
                    </div>
                </div>
                <div className="w-full bg-green-200 flex flex-col">
                    <div className="p-2 flex items-center flex-col">
                        <label className="w-full"><strong>Comida en paquetes: </strong></label>
                        <p>
                            Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
                            Exercitationem dignissimos harum aliquam doloremque
                        </p>
                    </div>
                    <div className="w-full">
                        <Dropdown 
                            title="Caracteristicas"
                            options={[
                                "Encendido rapido",
                                "Bateria de larga duración"
                            ]} 
                            selectedOption={""} 
                            onChange={function (option: string): void {
                                console.log('option selected', option)
                            } }
                        />
                        <DropdownList 
                            title="Caracteristicas"
                            options={[
                                "Encendido rapido",
                                "Bateria de larga duración"
                            ]} 
                            selectedOption={""} 
                            onChange={function (option: string): void {
                                console.log('option selected', option)
                            } }
                        />
                        <td className="py-3">
                            <div className="flex items-center">
                            <button className="text-gray-500 hover:text-gray-700" onClick={() =>
                                { 
                                    console.log('must delete', "")
                                }
                            }>
                                <HiOutlineTrash />
                            </button>
                            <div className="mx-4">{""}</div>
                            <button className="text-gray-500 hover:text-gray-700">
                                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                                </svg>
                            </button>
                            </div>
                        </td>
                    </div>
                </div>
            </div>

        </>
    )
}