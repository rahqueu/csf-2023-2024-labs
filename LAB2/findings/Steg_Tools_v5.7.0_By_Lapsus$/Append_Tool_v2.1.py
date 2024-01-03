import sys
import os

def add_files(file1, file2, outputFile):

    f1 = open(file1, "rb")
    f1_data =  f1.read()
    f1.close()

    f2 = open(file2, "rb")
    f2_data = f2.read()
    f2.close()

    path = "Output"
    # Create Output directory if needed
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

    with open(path + "/" + outputFile, "wb") as out_file:
        out_file.write(f1_data)
        out_file.write(f2_data)
        

def usage(prog_name):
    print("Add file1 and file2 to the output file")
    print("Usage:")
    print("{program_name} <file_name1> <file_name2_to_hide> <outputFile_name>".format(program_name=prog_name))
    sys.exit()


if __name__ == "__main__":  
    if len(sys.argv) < 4:
        usage(sys.argv[0])
    else:
        add_files(sys.argv[1], sys.argv[2], sys.argv[3])