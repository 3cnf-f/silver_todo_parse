import todo_parser as tp
import sys
used_headers=[]
arg_thisfile=sys.argv[1]
arg_header=sys.argv[2]
def taglist(select_header,thisfile,outfile="poop.json"):
    results=tp.parse_todo(thisfile,outfile)
    output=[]
    output.append("# #"+select_header.upper())
    for i,item in enumerate(results):
        if select_header.lower().strip() == item["my_header"].lower().strip():
            content=item["line_content"].strip()
            if content!="":
               output.append("* "+item["line_content"])
    return output
taglistlist=arg_header.split("+")
for thisarg in taglistlist:
    resultatata=taglist(thisarg,arg_thisfile)
    print("````")
    for r in resultatata:
        print(r)
    print("````")
    print("")
    print("")
