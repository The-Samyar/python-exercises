from math import pow

'''
Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
'''


# converts a list of decimal numbers to binary
def DecToBin(bit):

    binaries = []

    for decimal in range(0, int(pow(2, bit))):

        binary = ""

        # keeps dividing decimal by 2 and record the remainder until dividing the decimal by zero yields quotient of 0. note that this will convert the number in binary, but in reverse
        while decimal > 0 :
            binary += str(decimal % 2)
            decimal = int(decimal / 2)

        # reverses the converted number (which is now in binary) and adds a number of zeros before it so it matches the input bits
        binary = ('0' * (bit - len(binary))) + binary[::-1]
        binaries.append(binary)

    return binaries


# converts a list of binary numbers to a list grey codes
def BinToGrey(binaries):

    greys = []

    for binary in binaries:
        # the most significant bit (MSB) of a binary number is same as the MSB of its gray code
        grey = binary[0]
        
        # for the rest of the bits, every bit is 'XOR'ed with its previous bit, for example if bit 1 of the binary number is equal to bit 0, then bit 1 of gray code would be 0, otherwise if they are not the same then bit 1 of gray code would be 1
        for i in range(1, len(binary)):
            if binary[i] == binary[i - 1]:
                next = '0'
            
            else:
                next = '1'

            grey += next
        greys.append(grey)
    
    return greys



n = 4
print(BinToGrey(DecToBin(n)))
