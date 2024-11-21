
import re
import sys

from sympy import print_tree
from xdg.Locale import regex

source = '''I wish I may, I wish I might Have a dish of fish tonight.'''
def regex1():
# Find I followed by wish:
    m = re.findall('I (?=wish)', source)
    if m:
        print(m)
    # wish preceded by I:
    m = re.findall('(?<=I) wish', source)
    if m:
        print(m)


    print(re.findall('\bfish' , source))
    print(re.findall('\\bfish' , source)) #extra backspace to escape the escape character


    print(re.findall(r'\bfish', source)) #r means use it as a raw string


    DNA_sequence = 'AATGAAGGGCCGCTACGATAAGGAACTTCGTAATTTCAG'
    print('DNA_sequence:' , DNA_sequence)

    motif = r'ATG.*?TAA'
    motif = r'ATG.*TAA'  #? is NOT redundant
    #motif = r[ATG.*?TAA' invalid regular expression
    print("motif", motif)

# Checking if motif is a valid regular expression
    try:
        re.compile(motif)
    except:
        print('Invalid regular expression, exiting the program!')
        sys.exit()

    match = re.search(motif, DNA_sequence)

    if match:
        print('Found the motif   :', match.group())
        print('Starting at index :', match.start())
        print('Ending at index   :', match.end())
    else:
        print('Did not find the motif.')


    s= 'foo123bar'
    print(re.search('123', s))

    print(re.search('[0-9],[0-9],[0-9]', s))


regex1()