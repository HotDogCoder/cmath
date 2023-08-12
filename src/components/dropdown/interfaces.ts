export interface DropdownProps {
    title: string;
    options: string[];
    selectedOption: string;
    onChange: (option: string) => void;
}