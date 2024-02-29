num = input('Enter a number (decimal only): ')
# type your code here

# dp = len(num.split(".")[1])    #soltuion 1

dp  = len(num[num.index(".")+1:])    #solution 2

# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
