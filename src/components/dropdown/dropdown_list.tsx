import classNames from "classnames";
import { useState } from "react";
import { HiChevronDown, HiChevronUp } from "react-icons/hi";
import { DropdownProps } from "./interfaces";

const DropdownList: React.FC<DropdownProps> = ({
    title,
    options,
    selectedOption,
    onChange,
}) => {
  const [isOpen, setIsOpen] = useState(false);

  const handleOptionClick = (option: string) => {
    setIsOpen(false);
    onChange(option);
  };

  return (
    <div className="relative">
      <button
        type="button"
        className="
        relative z-10 block w-full pl-3 
        pr-10 py-2 text-left text-base font-medium 
        text-gray-700 bg-white border border-gray-300 
        shadow-sm focus:outline-none 
        focus:ring-1 focus:ring-blue-500 
        focus:border-blue-500 sm:text-sm flex"
        onClick={() => setIsOpen(!isOpen)}
      >
        {title}
        {isOpen ? 
            (
                <HiChevronDown
                    className="h-5 w-5"
                    aria-hidden="true"
                />
            ) :
            (
                <HiChevronUp
                    className="h-5 w-5"
                    aria-hidden="true"
                />
            )
        }

      </button>
      {isOpen && (
        <div className="z-10 mt-1 w-full bg-white shadow-lg">
          <ul
            className="max-h-60 py-1 text-base ring-1 ring-black ring-opacity-5 overflow-auto focus:outline-none sm:text-sm"
            tabIndex={-1}
          >
            {options.map((option) => (
              <li
                key={option}
                className={classNames(
                  "px-4 py-2 text-gray-700 cursor-pointer select-none",
                  {
                    "bg-gray-100": option === selectedOption,
                  }
                )}
                onClick={() => handleOptionClick(option)}
              >
                {option}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default DropdownList;
