import versions.mark1 as m1
import versions.mark2 as m2

def callMark(version):
    match version : 
        case 1 :
            m1.initialize()
        case 2 :
            m2.initialize()


if __name__ == "__main__":

    while True:
        
        print("Kindly Select my version from below -")
        created_versions = 2
        mark = "Mark -"
        for i in range(1, created_versions+1):
            print(f"{mark} {i}")
        print("0 - for exit")
        
        try:
            version = int(input("\nVersion : "))
            if 0 == version:
                print("Thank you exiting program.")
                break
            if 1 <= version <= created_versions:
                callMark(version)
            else:
                print(f"Please select available versions.")
        except ValueError:
            print("Invalid input. Please enter a number.")
