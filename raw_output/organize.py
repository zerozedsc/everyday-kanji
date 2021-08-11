import json, random, os, time, threading, sys, wmi

with open("kanji.json", "r", encoding="utf8") as read:
    test_load = json.load(read)
    read.close()
kanji = list(test_load.keys())

total_kanji = len(kanji)
pick = True
old_number = []
onyomi_dict = {}

for i in kanji:
    kanji_data = test_load[i]
    on_reading = kanji_data["readings_on"]
    for k in on_reading:
        if str(k) not in onyomi_dict.keys():
            onyomi_dict[str(k)] = str(i)
        else:
            onyomi_dict[str(k)] += "," +str(i)

with open("onyomi.json", 'wb') as jsonwriter:
    jsonwriter.write(json.dumps(onyomi_dict, ensure_ascii=False).encode("utf8"))
    jsonwriter.close()
