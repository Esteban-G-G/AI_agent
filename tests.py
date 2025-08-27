from functions.get_files_info import get_files_info

if __name__ == "__main__":
    # Test 1: Current directory
    print('Result for current directory:')
    print(get_files_info("calculator", "."))
    print()

    # Test 2: pkg directory
    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))
    print()

    # Test 3: absolute path outside working dir
    print("Result for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))
    print()

    # Test 4: relative path outside working dir
    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"))
