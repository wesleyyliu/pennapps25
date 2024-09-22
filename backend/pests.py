from Pest import Pest
import json
# Initialize a map of bugs
def initializeBugs():
    ant = Pest("Ant", "", "spray vinegar on soil; mix borax, sugar, and water and place near plant;" + 
               "use diatomaceous earth (keep soil dry); pour boiling water")
    aphid = Pest("Aphid", "", "spray water, neem oil, or water-soap solution forcefully; use insecticide if severe")
    armyworm = Pest("Armyworm", "", "spray neem oil or insecticide with Bacillus thuringiensis")
    bee = Pest("Bee", "", "hire a beekeeper to relocate the bee nest; " + 
               "spray insecticide or soapy water at beehive during night from a safe distance. " + 
               "Note: bees are considered pests when they set up a nest near you or your plants")
    beetle = Pest("Beetle", "", "sprinkle Diatomaceous earth (keep soil dry); " + 
                  "spray or pour soapy water, vinegar water, or boiling water")
    bollworm = Pest("Bollworm", "", "use insecticide spray or spray substances containing Bacillus thuringiensis")
    caterpillar = Pest("Caterpillar", "", "remove caterpillars and eggs where discovered and put them in soapy water; " + 
                       "spray at them directly with soapy water, vinegar mixture, or insecticide")
    earthworm = Pest("Earthworm", "", "reduce the use of compost; introduce predatory species like birds; " +
                      "manually remove the worm")
    earwig = Pest("Earwig", "", "use fish or vegetable oil to attract earwigs into traps; " + 
                  "mix rubbing alcohol with water and spray")
    grasshopper = Pest("Grasshopper", "", "collaborate with others to control population when they’re small nymphs; " + 
                       "apply insecticide to green plants that they are attracted to")
    mite = Pest("Mite", "", "use insecticidal soap or oil to spray; use pesticides with horticultural oil to " + 
                "eliminate mites and their eggs")
    mosquito = Pest("Mosquito", "", "trim lawn and shrubs to reduce mosquito hiding and breeding spots;" + 
                    " bring mosquito-repelling plants like lavender")
    moth = Pest("Moth", "", "hand-pick them and throw them into soapy water; " + 
                "use row covers to prevent moths from reaching plants")
    sawfly = Pest("Sawfly", "", "spray with high pressure water to knock them off; " + 
                  "hand-pick them and throw into soapy water; use insecticidal soap and horticultural oil")
    slug = Pest("Slug", "", "use traps that contain bear or a water and yeast mixture that attract slugs and " + 
                 "cause them to fall; create drier conditions in garden")
    snail = Pest("Snail", "", "hand-pick snails and remove them; pour light amounts of salt on places where snails move")
    stern_borer = Pest("Stern borer", "", "remove infested/infected parts of crop as soon as possible; " + 
                       "spray pesticide as needed")
    wasp = Pest("Wasp", "", "spray at late evening or early morning with a mixture soap and water or just with pesticide")
    weevil = Pest("Weevil", "", "use Diatomaceous earth; incorporate plants they hate like lavender; "+ 
                  "spray insecticides on them ")
    bugMap = {"ants": ant, "aphids": aphid, "armyworm": armyworm, "bees": bee, "beetle": beetle, "bollworm": bollworm, 
              "caterpillar": caterpillar, "earthworms": earthworm, "earwig": earwig, "grasshopper": grasshopper, "mite": mite,
              "mosquito": mosquito, "moth": moth, "sawfly": sawfly, "slug": slug, "snail": snail, "stern_borer": 
              stern_borer, "wasp": wasp, "weevil": weevil}
    return bugMap

# Input: dictionary maps from bug to a list of tuples of times (they are in floats) and in seconds
# Output: List of bugs with recommendations
# So basically an array with a dictionary 
def compileBugs(bugDict: dict):
    # from collections import defaultdict
    # m = defaultdict(list)
    # m['bees'].append((1.0, 2.0))
    # bugDict = dict(m)

    bugMap = initializeBugs()
    bugList = []
    jsonList = []
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
            if startSecond < 10:
                time = str(startMinute) + ":0" + str(startSecond)
            elif startSecond >= 10:
                time = str(startMinute) + ":" + str(startSecond)
            if endSecond < 10:
                time += "-" + str(endMinute) + ":0" + str(endSecond)
            elif endSecond >= 10:
                time += "-" + str(endMinute) + ":" + str(endSecond)
            times.append(time)
        curBug.timeStamps = times
        bugList.append(curBug)
    for pest in bugList:
        jsonList.append({"bug":pest.name, "timestamp":pest.timeStamps, "description":pest.description})
    my_dict = {}
    my_dict["insects"] = jsonList
    return(my_dict)

# if __name__ == '__main__':
#     compileBugs({})