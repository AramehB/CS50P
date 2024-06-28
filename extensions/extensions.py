file = input("File name: ").strip().lower()

if "." in file:
    _, extension = file.rsplit(".", maxsplit = 1)

    match extension:
        case "gif" | "png":
            print("image/" + extension)
        case  "jpg" | "jpeg":
            print("image/jpeg")
        case "pdf" | "zip":
            print("application/" + extension)
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")

else:
    print("application/octet-stream")
