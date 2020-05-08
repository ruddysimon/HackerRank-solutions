def print_formatted(number):
    #Width between columns
    width = len(str(bin(number))[2:])
    for i in range(1,number+1):
        print(str(i).rjust(width,' '), oct(i)[2:].rjust(width,' '), hex(i).upper()[2:].rjust(width,' '), bin(i)[2:].rjust(width,' '))