import json

def main():
    with open("./entities.json", "r") as file:
        datas = json.load(file)
    
        for data in datas:
            code = f"`{data}`"
            datas[data]["code"] = code
    print(datas)
    
    
    with open("./test.txt", "w", encoding="utf-8") as file:
        for i in datas:
            file.write(f"{i}: {datas[i]}\n\n")


if __name__ == "__main__":
    main()