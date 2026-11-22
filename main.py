import os

TEXT = "The cups are already on the table, steam thinning in the evening air. A chair has been pulled out for you. Outside, the street is quiet enough to hear a bicycle pass, and then nothing at all."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
