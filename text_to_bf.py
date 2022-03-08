from sys import argv

class TextToBrainfuck(object):
    """
        Class to convert text to brainfuck
    """
    def text_to_brainfuck(self, text, output_file_name=None):
        """
        :param text: Text to convert
        :return: Brainfuck code
        """
        code = ""
        symbols = len(set([char for char in text]))
        num_of_cells = max(max([ord(char) for char in text]) // symbols, 1)

        # Creating memory arrays
        cells = [(i + 1) * num_of_cells for i in range(symbols)]
        code += "+" * num_of_cells + "["
        code += "".join([">" + ("+" * (i + 1)) for i in range(1, symbols)])
        code += "<" * (symbols - 1) + "-]"
        code += "+" * num_of_cells

        # Convert the characters to brainfuck by moving the memory pointer to the closest memory position and print the character
        current_cell = 0
        for char in text:
            new_cell = [abs(ord(char) -c) for c in cells].index(min([abs(ord(char) - c) for c in cells]))
        
            sym = ""
            if new_cell - current_cell > 0:
                sym = ">"
            else:
                sym = "<"

            code += sym * abs(new_cell - current_cell)

            if ord(char) - cells[new_cell] > 0:
                sym = "+"
            else:
                sym = "-"

            code += sym * abs(ord(char) - cells[new_cell]) + "."

            current_cell = new_cell
            cells[new_cell] = ord(char)
        
        if output_file_name is None:
            return code
        else:
            with open(output_file_name, "w") as f:
                f.write(code)
                print("Brainfuck code saved to " + output_file_name)

if __name__ == "__main__":
    # Check if argument is valid
    if len(argv) > 2:
        print("Usage: python text_to_bf.py filename.bf")
        exit(0)
    
    # Input
    text = input("Enter text to be translated: ")
    text_to_bf = TextToBrainfuck()
    if len(argv) == 1:
        print(text_to_bf.text_to_brainfuck(text))
    else:
        output_file_name = argv[1]
        text_to_bf.text_to_brainfuck(text, output_file_name)