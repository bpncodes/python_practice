from sys import argv
#for encoding a string
str='नेपाली'
raw=str.encode()
string=raw.decode()
print(raw)
print("\n",string)

script,files=argv

def read_line(file):
    line=file.readline()
    if line:
        print(line.encode(encoding="utf-8",errors="strict"))
        read_line(file)

new_file=open(files)
read_line(new_file)


