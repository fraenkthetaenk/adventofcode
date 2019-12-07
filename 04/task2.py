
start = 193651
end = 649729
pwMeetingCriteria = 0
current = start-1

while current <= end:
    currentS = str(current)
    current += 1
    pos1 = int(currentS[0])
    pos2 = int(currentS[1])
    pos3 = int(currentS[2])
    pos4 = int(currentS[3])
    pos5 = int(currentS[4])
    pos6 = int(currentS[5])

    if (pos1<=pos2<=pos3<=pos4<=pos5<=pos6):
        if(pos1 == pos2):
            if(pos2 != pos3):
                pwMeetingCriteria += 1
                continue
        if(pos2 == pos3):
            if(pos1 != pos2 and pos3 != pos4):
                pwMeetingCriteria += 1
                continue
        if(pos3 == pos4):
            if(pos2 != pos3 and pos4 != pos5):
                pwMeetingCriteria += 1
                continue
        if(pos4 == pos5):
            if(pos3 != pos4 and pos5 != pos6):
                pwMeetingCriteria += 1
                continue
        if(pos5 == pos6):
            if(pos4 != pos5):
                pwMeetingCriteria += 1
                continue
                

print(pwMeetingCriteria)
