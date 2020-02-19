# Passing Scoring
s_passingYds = .04
s_passingTd = 4
s_passingTwoPointConversion = 2
s_completion = .1
s_longCompletion = 2
s_interception = -2

# RushingScoring
s_rushingYds = .1
s_rushingTd = 6
s_rushingTwoPointConversion = 2
s_rushAtt = .1
s_longRush = 2

# ReceivingScoring
s_receivingYds = .1
s_receivingTd = 6
s_receivingTwoPointConversion = 2
s_reception = .5
s_longReception = 2

# KickingScoring
s_fg19 = 3
s_fg29 = 3
s_fg39 = 3
s_fg49 = 4
s_fg99 = 5
s_pat = 1
s_fgMiss = -1
s_patMiss = -1

def calculatePassingScore(passingYds, passingTDs, twoPointConversions, completions, longCompletions, interceptions):
    return passingYds*s_passingYds + passingTDs*s_passingTd + twoPointConversions*s_passingTwoPointConversion + completions*s_completion + longCompletions*s_longCompletion + interceptions*s_interception

def calculateRushingScore(rushingYds, rushingTDs, twoPointConversions, rushAtt, longRushes):
    return rushingYds*s_rushingYds + rushingTDs*s_rushingTd + twoPointConversions*s_rushingTwoPointConversion + rushAtt*s_rushAtt + longRushes*s_longRush

def calculateReceivingScore(receivingYds, receivingTDs, twoPointConversions, receptions, longReceptions):
    return receivingYds*receivingYds + receivingTDs*receivingTDs + twoPointConversions*s_receivingTwoPointConversion + receptions*s_reception + longReceptions*s_longReception

def calculateRushingReceivingScore(rushingYds, rushingTDs, twoPointConversionsRushing, rushAtt, longRushes, receivingYds, receivingTDs, twoPointConversionsReceiving, receptions, longReceptions):
    return rushingYds*s_rushingYds + rushingTDs*s_rushingTd + twoPointConversionsRushing*s_rushingTwoPointConversion + rushAtt*s_rushAtt + longRushes*s_longRush + receivingYds*receivingYds + receivingTDs*receivingTDs + twoPointConversionsReceiving*s_receivingTwoPointConversion + receptions*s_reception + longReceptions*s_longReception

def calculateSimpleScore(rushingYds, rushingTDs, rushAtt, receivingYds, receivingTDs, receptions):
    return rushingYds*s_rushingYds + rushingTDs*s_rushingTd + rushAtt*s_rushAtt + receivingYds*receivingYds + receivingTDs*receivingTDs + receptions*s_reception

def calculateKickingScore(fg19, fg29, fg39, fg49, fg99, pat, fgMiss, patMiss):
    return fg19*s_fg19 + fg29*s_fg29 + fg39*s_fg39 + fg49*s_fg49 + fg99*s_fg99 + pat*s_pat + fgMiss*s_fgMiss + patMiss*s_patMiss