import sys
import converter
import subprocess


while True:
    if sys.argv[1] == "run":
        file_name = input("Enter File path: ")
        subprocess.run(f"python.exe rizz_interpreter.py {file_name}")
        exit()

    elif sys.argv[1] == "convert":
        choice = input("What would you like to convert?: ")
        
        if choice == "rizz2bf":
            rizz_file = input("Enter File path: ")
            converter.rizz2bf(rizz_file)
            exit()
        
        elif choice == "bf2rizz":
            bf_file = input("Enter File path")
            converter.bf2rizz(bf_file)
            exit()
        
        elif choice == "rizz2python":
            rizz_file = input("Enter Rizz File Path: ")
            with open(rizz_file, 'r') as rizz_file_to_read:
                read_file = rizz_file_to_read.read()
                converter.rizz_to_python(read_file)
                exit()
        elif choice == "quit":
            exit()
        
        else:
            print("""
rizz2bf -> Allows conversion of rizz code to brainf**k code.
bf2rizz -> Allows conversion of brainf**k code to rizz code.
rizz2python -> Allows conversion of rizz code to python code.
                """)
            continue
    
    elif sys.argv[1] == "help":
        print("""
run -> runs the rizz file
convert -> uses the converter tool to convert your code for you.
""")
    else: print("""
run -> runs the rizz file
convert -> uses the converter tool to convert your code for you.
""")