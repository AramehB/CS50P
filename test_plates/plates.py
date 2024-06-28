def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            z = s.lstrip('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            if s.rstrip('0123456789').isalpha() and (not z or z[0] != '0'):
                if s.isalnum() or s.isalpha():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False




if __name__ == "__main__":
    main()
