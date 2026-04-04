
def evaluate_polynomial(poly_dict, x):
    result = 0
    for i, c_i in poly_dict.items():
        result += c_i * x**i
    return result
my_poly = {0: -10, 2: 3, 4: 1}
x1 = 2
x2 = -1.5
result1 = evaluate_polynomial(my_poly, x1)
result2 = evaluate_polynomial(my_poly, x)
print(f'Result: {result1}, Result: {result2}')