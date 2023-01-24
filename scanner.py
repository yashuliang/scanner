from github import Github
from datetime import datetime
from decouple import config


begin = datetime.now()

GITHUB_PERSONAL_KEY = config('GITHUB_PERSONAL_KEY')

# using an access token
g = Github(GITHUB_PERSONAL_KEY)


repo = g.get_repo("coupa/treasury_tm5")
files = repo.get_contents("/Backend/BELLIN.TMS/ForecastingContext")

while files:
    file = files.pop(0)

    if not "test" in file.name.lower() and not file.name.lower().endswith("dto.cs") and not file.name.lower().endswith("constants.cs"):
        if file.type == "dir" and \
            not file.name.endswith("Api") and \
            not file.name.endswith("Commands") and \
            not file.name.endswith("Events") and \
            not file.name.endswith("Enums") and \
            not file.name.endswith("Repositories") and \
            not file.name.endswith("Models") and \
            not file.name.endswith("Translations") and \
            not file.name.endswith("Exceptions") and \
            not file.name.endswith("Permissions") and \
            not file.name.endswith("Actions") and \
            not file.name.endswith("Aggregates") and \
            not file.name.lower().endswith("dto") and \
            not file.name.lower().endswith("dtos") :
            files.extend(repo.get_contents(file.path))
        else:
            if file.name.endswith(".cs"):
                # parse the file
                print(file.path)

                lines = file.decoded_content.splitlines()

                i=0
                while i < len(lines):
                    line = lines[i]
                    if "LogError" in str(line) or \
                        "LogDebug" in str(line) or \
                        "LogInformation" in str(line) or \
                        "LogWarning" in str(line) or \
                        "LogTrace" in str(line) or\
                        "LogCritical" in str(line):
                        print("*" + str(line))
                        print("*" + str(lines[i+1]))
                        print("*" + str(lines[i+2]))
                    i += 1

end = datetime.now()
print("total seconds:" + str((end-begin).total_seconds()))
