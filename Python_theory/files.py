from cloudinit.atomic_helper import json_dumps


def main():
    """open, read, write, delete the file, modify the content, search and SEEK(jump to a specific position in the file), close the file
    Mode of a file:
    1.read only .r
    2.read and write
    3.append,etc
    """
    #fileobj = open(filename , mode)

    text = ('testing the files prop, more of the bytes being written'
            'second line being read or not1')


    fout = open('python.txt', 'wt') #fout is referred to as file handle which is a reference to that file
    bytes_written = fout.write(text)
    print(bytes_written)
    fout.close()


    #write in chunks
    fout = open('python.txt','wt')
    size = len(text)
    offset =  0
    chunk = 100
    while True:
        if offset > size:
            break
        bytes_written = fout.write(text[offset:offset+chunk])
        print(bytes_written)
        offset+=chunk
    fout.close()
    #
    # fout = open('python.txt', 'wa')
    # size = len(text)
    # offset = 0
    # chunk = 100
    # while True:
    #     if offset > size:
    #         break
    #     bytes_written = fout.write(text[offset:offset + chunk])
    #     print(bytes_written)
    #     offset += chunk
    # fout.close()

    #mode x to prevent overwriting
    try:
        fout = open('python.txt', 'xt')
        fout.write('Python libraries')
    except FileExistsError:
        print('pyhtomn.txt already exists')
        #return none
    finally:    #housekeeping job before we exit out of except block
        print('x mode prevented overwriting!')



    #Read a Textfile with read(), readline(), or readlines
    fin = open('python.txt', 'rt')
    ftext= fin.read()
    fin.close()
    print(len(ftext))

    #readlines()
    fin = open('python.txt', 'rt')
    lines = fin.readlines()
    # print(type(lines))
    fin.close()
    print(len(lines), 'lines read')
    for line in lines:
        print(lines, end='')

    #Binary files
    # bdata = bytes(range(0,250))

    #with command automatically closes the files

    with open('python.txt', 'wt') as fout:
        fout.write(text)

    #seek()- change position
    #tell()- tells the exact position

    ''' json files- javascript object notation,
        csv- comma,separated values files, 
        xml- extended markup lang files'''

    '''json files- 
    '''


    import csv

    players = [
        ['Rohit','Sachin'],
        ['shubham','Suresh'],
        ['Raina', 'Gambhir'],
        ['Dhoni','DRavid']

    ]

    with open('players.txt', 'wt')as fout:
        csvout = csv.writer(fout)
        csvout.writerows(players)



    #read from a csv files
    with open('players.txt','rt')as fin:
        cin = csv.reader(fin)
        p = [row for row in cin]
        print(p)


    #write using dict writer, dict reader for dict



    #structure of xml files
    #xml.dom
    #xml.sax

    #json files
    '''key-value, dicitonary like representation'''

    import json
    # continuing in the next line
    menu = \
    {
        "breakfast":{
            "hours":"7-11",
            "items":{
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
            }
        },
    }

    menu_json = json_dumps(menu)
    print(menu_json)

    menu2= json.loads(menu_json)
    print(menu2)

###serialize using pickle
import pickle
import datetime
now1 = datetime.datetime.utcnow()
print(now1)
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
print(now2)

if __name__ == "__main__":
    main()
