import sys
from rpn_calculator import RPNCalculator

def main():
    if len(sys.argv) != 3:
        print("Usage: python wp5.py instructions.rpn result.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r') as f:
        instructions = f.read().replace('\n', ' ')

    calculator = RPNCalculator()
    result = calculator.evaluate_rpn_expression(instructions)

    with open(output_file, 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
