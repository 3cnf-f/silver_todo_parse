import todo_parser as tp
import sys
used_headers=[]
arg_thisfile=sys.argv[1]
arg_select_tag=sys.argv[2]
def taglist(select_tag,thisfile,outfile="poop.json"):
    results=tp.parse_todo(thisfile,outfile)
    output=[]
    output.append("# #"+select_tag.upper())
    for i,item in enumerate(results):
        if select_tag in item["tags"]:
            if item["my_header"] not in used_headers:
                used_headers.append(item["my_header"])
            output.append("* "+item["line_content"].replace("#"+select_tag,""))
    return output
taglistlist=arg_select_tag.split("+")
for thisarg in taglistlist:
    resultatata=taglist(thisarg,arg_thisfile)
    print("````")
    for r in resultatata:
        print(r)
    print("````")
    print("")
    print("")
