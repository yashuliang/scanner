from textwrap import dedent
from github import Github
from datetime import datetime
from decouple import config

import os
import re


begin = datetime.now()

path ="C:\\Users\\Yashu\\repos\\treasury_tm5\\Backend\\BELLIN.TMS\\ForecastingContext"

with open('loggings.txt', 'w') as ft:
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".cs") and not "test" in file.lower():
                file_to_open = os.path.join(root,file)
                print("reading... " + file_to_open)

                f = open(file_to_open)
                lines = f.readlines()
                i=0
                while i < len(lines):
                    line = lines[i]
                    if "LogError" in str(line) or \
                        "LogDebug" in str(line) or \
                        "LogInformation" in str(line) or \
                        "LogWarning" in str(line) or \
                        "LogTrace" in str(line) or\
                        "LogCritical" in str(line):

                        three_lines_log = str(line) + str(lines[i+1]) + str(lines[i+2])
                        three_lines_log = three_lines_log.strip("\n\t")

                        three_lines_log = re.sub(r"[\n\t]*", "", three_lines_log)
                        print("*" + dedent(three_lines_log))

                        ft.write(file + "," + three_lines_log)
                        ft.write('\n')
                    i += 1
                f.close()
           





# while files:
#     file = files.pop(0)

#     if not "test" in file.name.lower() and not file.name.lower().endswith("dto.cs") and not file.name.lower().endswith("constants.cs"):
#         if file.type == "dir" and \
#             not file.name.endswith("Api") and \
#             not file.name.endswith("Commands") and \
#             not file.name.endswith("Events") and \
#             not file.name.endswith("Enums") and \
#             not file.name.endswith("Repositories") and \
#             not file.name.endswith("Models") and \
#             not file.name.endswith("Translations") and \
#             not file.name.endswith("Exceptions") and \
#             not file.name.endswith("Permissions") and \
#             not file.name.endswith("Actions") and \
#             not file.name.endswith("Aggregates") and \
#             not file.name.lower().endswith("dto") and \
#             not file.name.lower().endswith("dtos") :
#             files.extend(file)
#         else:
#             if file.name.endswith(".cs"):
#                 # parse the file
#                 print(file.path)

#                 lines = file.decoded_content.splitlines()

#                 i=0
#                 while i < len(lines):
#                     line = lines[i]
#                     if "LogError" in str(line) or \
#                         "LogDebug" in str(line) or \
#                         "LogInformation" in str(line) or \
#                         "LogWarning" in str(line) or \
#                         "LogTrace" in str(line) or\
#                         "LogCritical" in str(line):

#                         three_lines_log = str(line) + str(lines[i+1]) + str(lines[i+2])
#                         three_lines_log = three_lines_log.strip()
#                         print("*" + three_lines_log)
#                     i += 1

end = datetime.now()
print("total seconds:" + str((end-begin).total_seconds()))
