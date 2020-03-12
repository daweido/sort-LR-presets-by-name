import glob
import sys
import os


new_group_name = ""

if len(sys.argv) > 1:
    new_group_name = sys.argv[1]
elif (new_group_name == ""):
    new_group_name = os.path.basename(os.getcwd())
    
group_name_opening = "<rdf:li xml:lang=\"x-default\">"
group_name_closing = "</rdf:li>"

for filename in glob.glob('*.xmp'):
    f = open(filename)
    lines = f.readlines()
    for index,line in enumerate(lines):
        line = line.rstrip().strip()
        if "<crs:Group>" == line:
            group_name_line = lines[index+2]
            name_starting_index = group_name_line.find(group_name_opening)+len(group_name_opening)
            name_finishing_index = group_name_line.find(group_name_closing)
            old_name = group_name_line[name_starting_index:name_finishing_index]
            lines[index+2] = group_name_line.replace(old_name,new_group_name)
    f.close()

    f = open(filename,'w')
    f.writelines(lines)
    f.close()