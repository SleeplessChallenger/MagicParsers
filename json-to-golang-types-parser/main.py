import json
from ast import literal_eval
from typing import List


def start_data_conversion() -> None:
    data = open("/Users/daniilslobodeniuk/Downloads/Telegram Desktop/binary-tree-preorder-traversal.json")
    read_data: str = data.read()
    json_data = json.loads(read_data)

    full_final_input_string: str = "[][]NilInt{"
    full_final_output_string: str = "[][]int{"

    for input_output in json_data:
        input: str = input_output["input"]
        output: str = input_output["output"]

        input = input.replace("null", "None")

        parsed_input_as_array: List = literal_eval(input)
        parsed_output_as_array: List = literal_eval(output)

        full_final_input_string: str = convert_input_to_golang_types(full_final_input_string, parsed_input_as_array)
        full_final_output_string: str = convert_output_to_golang_types(full_final_output_string, parsed_output_as_array)

    full_final_input_string += "}"
    full_final_output_string += "}"

    print(full_final_input_string)
    print(full_final_output_string)


def convert_input_to_golang_types(full_final_string: str, data: List) -> str:
    full_final_string += ","
    full_final_string += "{"

    if len(data) == 0:
        full_final_string += "}"
        return full_final_string

    for ele in data:
        converted_ele = None
        if type(ele) is int:
            converted_ele: str = f"NewInt({ele})"
        if ele is None:
            converted_ele: str = "NewNil()"

        if converted_ele is None:
            raise RuntimeError("Bitch, there is some error during converting to golang types in INPUT")

        full_final_string += converted_ele
        full_final_string += ","

    k = full_final_string.rfind(",")
    full_final_string = full_final_string[:k]

    full_final_string += "}"

    return full_final_string


def convert_output_to_golang_types(full_final_string: str, data: List):
    full_final_string += ","

    if len(data) == 0:
        # here return nil
        full_final_string += "{}"
        return full_final_string

    full_final_string += "{"

    for ele in data:
        converted_ele = None
        if type(ele) is int:
            converted_ele: int = ele

        if converted_ele is None:
            raise RuntimeError("Bitch, there is some error during converting to golang types in OUTPUT")

        full_final_string += str(converted_ele)
        full_final_string += ","

    k = full_final_string.rfind(",")
    full_final_string = full_final_string[:k]
    full_final_string += "}"
    return full_final_string


if __name__ == '__main__':
    """
    * remove one `,` in [][]NilInt{, and [][]int{,
    """
    start_data_conversion()
