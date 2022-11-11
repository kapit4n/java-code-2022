import os 
import pathlib

fReadme = open("./Readme.md", "w")

## Linear count
def countLines(path):
    count = 0
    for f in os.listdir(path):
        fPath = path + "/" + f
        file_ext = pathlib.Path(fPath).suffix
        if (os.path.isfile(fPath) and file_ext in ['.java']):
            fCount = len(open(fPath).readlines())
            fReadme.write(str(f) + "(" + str(fCount) + "), ")
            count = count + fCount
    fReadme.write("S(" + str(count) + ")\n")
    return count

next_goal = 100

total = 0
fReadme.write("## Categories")
for f in os.listdir('./src-ig'):
    pathFull = "./src-ig/" + f
    fReadme.write("\n## " + str(f).upper() + "\n")
    if (os.path.isdir(pathFull)):
        total = total + countLines(pathFull)

for f in os.listdir('./src'):
    pathFull = "./src/" + f
    fReadme.write("\n## " + str(f).upper() + "\n")
    if (os.path.isdir(pathFull)):
        total = total + countLines(pathFull)

if (total >= next_goal):
    print(total, "GOAL REACHED")
else:
    print("Total: ", total, " and ", (next_goal - total), "FOR THE GOAL")




fReadme.write("\n# Total \n" + str(total))