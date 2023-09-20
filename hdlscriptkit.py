import utility

directories = ["rtl", ".xilinx", ".xilinx_verilog", "tb", "tb_verilog", "tcl"]

def setup_scriptkit(filedirname):
    # Find all directories of interest and categorize them.
    print("Initiating test procedures...")
    rtl_exists = utility.find_rtl_directory(filedirname)

    print("Finding xilinx VHDL functional simulation directory ('.xilinx')...")
    xilinx_exists = utility.find_xilinx_directory(filedirname)
    if xilinx_exists:
        print("Note: '.xilinx' directory found. Xilinx functional tests will be performed after standard functional tests.")
    else:
        print("Note: no '.xilinx' directory found. No Xilinx functional simulation will be performed.")
    
    print("Finding xilinx Verilog timing simulation directory ('.xilinx_verilog')...")
    xilinx_exists = utility.find_xilinx_directory(filedirname)
    if xilinx_exists:
        print("Note: '.xilinx_verilog' directory found. Xilinx timing tests will be performed after standard functional tests.")
    else:
        print("Note: no '.xilinx_verilog' directory found. No Xilinx timing simulation will be performed.")