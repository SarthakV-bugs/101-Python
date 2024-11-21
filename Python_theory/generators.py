
#
# def generators():
#     yield 1
#     yield 2
#     yield 3
#
#
#     x = generators() #x will be an iterator
#     for i in x:
#         print(next(i))
#         print(next(i))
#         print(next(i))

#generator also referred to as generator expression.
#whenever large files are needed to be processed, generator expression helps to process the file in sections, using yield command
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

def csv_read(file_name):
    for row in open(file_name, "r"):
        yield row




def main():
    csv_gen = csv_reader("comma_sep.txt")
    row_count = 0

    for row in csv_gen:
        row_count += 1
    print(f"Row count is {row_count}")
#use generator on palindrome

if __name__ == "__main__":
        main()