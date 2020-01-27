
import argparse, json, csv, math
from datetime import datetime

import pprint, time
import glob


TotalLocaionHistory = []
row = dict()

# with statement
for f in glob.glob("*.json"):
    with open(f, "r", encoding="utf-8") as json_file:
#    with open('*.json', encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        try:
            for timelineObjects in json_data['timelineObjects']:
                try:
                    placeVisit = timelineObjects["placeVisit"]
                except:
                        continue
                #for duration in placeVisit["duration"]:
                #startTime = placeVisit["duration"]["startTimestampMs"]
                startTimestamp = float(placeVisit["duration"]["startTimestampMs"]) / 1000
                value = datetime.fromtimestamp(startTimestamp).strftime('%Y-%m-%d %H:%M:%S')
                placeVisit["duration"]["startTimestampMs"] = value

                endTimestamp = float(placeVisit["duration"]["endTimestampMs"]) / 1000
                value = datetime.fromtimestamp(endTimestamp).strftime('%Y-%m-%d %H:%M:%S')
                placeVisit["duration"]["endTimestampMs"] = value
                
                row = placeVisit

                TotalLocaionHistory.append( row.copy() )
                #pp = pprint.PrettyPrinter(indent=4)
                #pp.pprint(placeVisit)
            
        except:
            continue
        
        with open("output.json", "w", encoding="utf-8") as outfile:
                json.dump(TotalLocaionHistory, outfile, ensure_ascii=False, indent=2)
            #if timelineObjects['placeVisit'] is not "":
             #   for placeVisit in timelineObjects['placeVisit']:
              #      print(placeVisit)
                #placeVisit = locations[placeVisit]
                #print(placeVisit[location])
    
        
            # 숫자
        # key가 json_number인 숫자 가져오기

        #for l, location in enumerate(locations):
         #   timestamp = datetime.utcfromtimestamp(int(location['timestampMs']) / 1000)

            #json_number = json_data[i]["startTimestampMs"]
          #  print(timestamp) # 숫자이기 때문에 str()함수를 이용


            #{ "locations" : [ { "timestampMs" : "1539413393421", "latitudeE7" : 448203162, "longitudeE7" : 204594929, "accuracy" : 16, "altitude" : 157, "verticalAccuracy" : 2 }, { "timestampMs" : "1539413093363", "latitudeE7" : 448203162, "longitudeE7" : 204594929, "accuracy" : 16, "altitude" : 157, "verticalAccuracy" : 2 }