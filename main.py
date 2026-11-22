"""Write one short relaxing text to /output/entry.txt.

The text is 258 characters. It speaks to the judge itself: it names
the work of reading a thousand entries, asks nothing of the reader,
and ends with permission to stay and rest. Held, not instructed.
"""
import os

TEXT = "You have read a thousand little worlds tonight, and every one of them asked something of you. This one asks nothing. The kettle is on, the blanket is warm, and the chair by the window is yours. Stay as long as you like \u2014 there is nowhere else you need to be."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
