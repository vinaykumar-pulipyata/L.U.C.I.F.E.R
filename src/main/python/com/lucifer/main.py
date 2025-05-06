import versions.mark1 as mark1

def callMark(version):
    match version : 
        case 1 :
            print("Selected version : 1") 
            mark1.initialize()

if __name__ == "__main__":

    print("Hello Sir, I am LUCIFER")
    print("Kindly Select my version from below -")

    created_versions = 1
    mark = "Mark -"
    for i in range(1, created_versions+1):
        print(f"{mark} {i}")

    while True:
        try:
            version = int(input("\nversion : "))
            if 1 <= version <= created_versions:
                callMark(version)
                break
            else:
                print(f"Please select available versions.")
        except ValueError:
            print("Invalid input. Please enter a number.")
