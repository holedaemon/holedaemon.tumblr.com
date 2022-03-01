#!/usr/bin/env python3


def main():
    print("writing output")

    REPLACE_STRING = "<!-- CSS -->"

    output_data = ""

    with (
        open("theme.html", "r") as theme,
        open("theme.css", "r", encoding="utf-8-sig") as css,
    ):
        for line in theme:
            # line = line.strip()
            if REPLACE_STRING in line:
                line = "<style>\n\t"+css.read()+"\t\n</style>\n"
            
            output_data += line
        
    with open("output.html", "w") as output:
        output.write(output_data)
       
if __name__ == "__main__":
    main()