def evaluateHelper(result_map: dict, input_expression: str)-> List[int]:
    result = []
    if '*' not in input_expression and '-' not in input_expression and '+' not in input_expression:
        result.append(int(input_expression))
    else:
        for i in range(len(input_expression)):
            if input_expression[i] in '+-*':
                left_part = evaluateHelper(result_map, input_expression[:i])
                right_part = evaluateHelper(result_map, input_expression[i+1:])
                for left in left_part:
                    for right in right_part:
                        if input_expression[i] == "+":
                            result.append(left + right)
                        elif input_expression[i] == '-':
                            result.append(left - right)
                        elif input_expression[i] == '*':
                            result.append(left*right)
    result_map[input_expression] = result
    return result

def evaluateExpression(expression: str)-> List[int]:
    return evaluateHelper({}, expression)

def test():
    print(evaluateExpression("18*2-3+5"))
    print(evaluateExpression("2*3-4-5"))
test()
