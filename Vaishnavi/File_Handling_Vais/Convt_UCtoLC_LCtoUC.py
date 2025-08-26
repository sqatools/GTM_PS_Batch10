#write phython program to convert upper to lower and lower to upper
def convt_case(i_file, o_file):
    with open(i_file, 'r') as file:
        content = file.read()
    convt_cont = content.swapcase()

    with open(o_file, 'w') as outfile:
        outfile.write(convt_cont)

convt_case("read_data12.txt","write_data12.txt")