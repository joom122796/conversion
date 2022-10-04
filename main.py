# Use Google to find the formula for converting pounds to kilos and kilos to pounds.  Write a pseudocode algorithm that prompts the user to enter a kilo value and a pound value.  The program will convert the kilos to pounds and the pounds to kilos and output both values. 	
# Formula: 1kg * 2.205 = Value in pounds or 1lb / 2.205 = Value in kilograms

keys = int(input('Enter a value in kilograms: '))
pounds = int(input('Enter a value in pounds: '))

lb = keys*2.205
kg = pounds/2.205

print(f'The values you input were: \n{keys} kilograms \n{pounds} lb \n{keys} kilograms in pounds is {lb} and {pounds} lb in kilograms is {kg}')
