import re
import json

thistask=re.compile(r'(\s*\*\s\[ \])(.*)(?:[ ]|$)')
thisheader=re.compile(r'^#\s(.*)$')

thistag=re.compile(r'#([\w]+)(?:[ :]|$)')
line_list=[]
line_item={"ln":0,"original_line":"","line_content":"","tags":[],"my_header":""}
header_list=[]
header_item={"ln":0,"line_content":""}
header_range_list=[]
header_range_item={"line_content":"","start":0,"end":0}

def parse_todo(filename_in, filename_out=""):
            with open (filename_in, 'r') as f:
                ln=0
                for line in f.readlines():
                    ln=ln+1
                    line_item["ln"]=ln
                    line_item["original_line"]=line
                    line_item["line_content"]=""
                    line_item["tags"]=[]

                    # print(ln,line)
                    if thistask.match(line):
                        # print("  task:"+thistask.match(line).group(2))
                        line_item["line_content"]=thistask.match(line).group(2)
                        line_item["tags"].append("task")
                        if thistag.search(thistask.match(line).group(2)):
                            taglist=thistag.findall(thistask.match(line).group(2))
                            # print("       tag:"+str(taglist))
                            line_item["tags"].extend(taglist)
                    if thisheader.match(line):
                        # print("header:"+thisheader.match(line).group(1))
                        line_item["tags"].append("header")
                        line_item["line_content"]=thisheader.match(line).group(1)
                    line_list.append(line_item.copy())

# print((line_list))

            for i,item in enumerate(line_list):
                if "header" in item["tags"]:
                    # print("header line: "+str(item["ln"])+" "+item["line_content"])
                    header_item["ln"]=item["ln"]
                    header_item["line_content"]=item["line_content"]
                    header_list.append(header_item.copy())

            for i,item in enumerate(header_list):
                header_range_item["line_content"] = item["line_content"]
                header_range_item["start"] = item["ln"]+1
                if i==len(header_list)-1:
                    header_range_item["end"] = len(line_list)+1
                else:
                    header_range_item["end"] = header_list[i+1]["ln"]-1
                header_range_list.append(header_range_item.copy())
                
            for i,item in enumerate(line_list):
                for x,xitem in enumerate(header_range_list):
                    if item["ln"] >= xitem["start"] and item["ln"] <= xitem["end"]:
                        line_list[i]["my_header"] = xitem["line_content"]
                                          
            if filename_out != "":                                                                     
                with open (filename_out, 'w') as f:
                    json.dump(line_list, f, ensure_ascii=False, indent=2)
            return line_list
# with open ('Todo_test.json', 'a') as f:
#     json.dump(header_list, f, ensure_ascii=False, indent=2)
# with open ('Todo_test.json', 'a') as f:
#     json.dump(header_range_list, f, ensure_ascii=False, indent=2)
