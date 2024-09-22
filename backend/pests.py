import data.Pest as Pest

# Initialize a map of bugs
def initializeBugs():
    ant = Pest("Ant", "", "")
    aphid = Pest("Aphid", "", "")
    armyworm = Pest("Armyworm", "", "")
    bee = Pest("Bee", "", "")
    bollworm = Pest("Bollworm", "", "")
    caterpillar = Pest("Caterpillar", "", "")
    earthworm = Pest("Earthworm", "", "")
    earwig = Pest("Earwig", "", "")
    grasshopper = Pest("Grasshopper", "", "")
    mite = Pest("Mite", "", "")
    mosquito = Pest("Mosquito", "", "")
    moth = Pest("Moth", "", "")
    sawfly = Pest("Sawfly", "", "")
    slug = Pest("Slug", "", "")
    snail = Pest("Snail", "", "")
    stern_borer = Pest("Stern borer", "", "")
    wasp = Pest("Wasp", "", "")
    weevil = Pest("Weevil", "", "")
    bugMap = {"ant": ant, "aphid": aphid, "armyworm": armyworm, "bee": bee, "bollworm": bollworm, "caterpillar": caterpillar,
              "earthworm": earthworm, "earwig": earwig, "grasshopper": grasshopper, "mite": mite, "mosquito": mosquito, "moth":
              moth, "sawfly": sawfly, "slug": slug, "snail": snail, "stern_borer": stern_borer, "wasp": wasp, "weevil": weevil}
    return bugMap

# Input: dictionary maps from bug to a list of tuples of times (they are in floats) and in seconds
# Output: List of bugs with recommendations
def compileBugs(bugDict: dict):
    bugMap = initializeBugs()
    bugList = []
    for bugName, timeStamps in bugDict.items():
        curBug = bugMap[bugName]
        times = []
        for timeStamp in timeStamps:
            startTime = int(timeStamp[0])
            endTime = int(timeStamp[1])
            startMinute = startTime // 60 
            startSecond = startTime % 60
            endMinute = endTime // 60
            endSecond = endTime % 60
            time = str(startMinute) + ":" + str(startSecond) + "-" + str(endMinute) + ":" + str(endSecond)
            times.append(time)
        curBug.timeStamps = timeStamps
        bugList.append(curBug)
    return bugList