import sys
import os


def main():

    FOLDER = "test"

    filepath = sys.argv[1]
    relfilepath = filepath[len(f"D:/Files/Writing/{FOLDER}/"):-3]
    names = relfilepath.split("\\")

    out = "[[void/index|~]] / "

    if names[-1] == names[-2]:
        names.pop(-1)

    for index, name in enumerate(names[:-1]):
        out += f"[[{'/'.join(names[:index+1])}/{name}|{name}]] / "

    out += f"{names[-1]}"

    header_exists = False
    with open(filepath, "r") as doc:
        lines = doc.readlines()
        try:
            body_index = lines.index("---\n")
            body = lines[body_index+1:]
            header_exists = True

        except:
            body = lines[1:]

    with open(filepath, "w") as doc:
        doc.writelines(f"{out}\n\n---\n")
        doc.writelines(body)


if __name__ == "__main__":
    main()
