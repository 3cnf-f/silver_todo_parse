from ics import Calendar
import requests
from zoneinfo import ZoneInfo
def to_sthlm(dt):
    dt_utc = dt.astimezone(ZoneInfo("UTC"))
    return dt_utc.astimezone(ZoneInfo("Europe/Stockholm"))

datedic = {}   
with open("tessa.ics", "r") as f:
    c = Calendar(f.read())
for this_event in c.events:
    if str(to_sthlm(this_event.begin))[:10] not in datedic:
       datedic[str(to_sthlm(this_event.begin))[:10]]=[(this_event)]
    else:
       datedic[str(to_sthlm(this_event.begin))[:10]].append(this_event)

newdate_dic=dict(sorted(datedic.items()))
for k,v in newdate_dic.items():
    print(k)
    for this_event in v:
        print(this_event.location[:14])
# for this_event in c.events:
#     print(to_sthlm(this_event.begin), to_sthlm(this_event.end), this_event.location[:14])

