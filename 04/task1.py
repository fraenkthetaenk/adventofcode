
start = 193651
end = 649729
pwMeetingCriteria = 0
current = start

while current <= end:
    currentS = str(current)

    pos1 = int(currentS[0])
    pos2 = int(currentS[1])
    pos3 = int(currentS[2])
    pos4 = int(currentS[3])
    pos5 = int(currentS[4])
    pos6 = int(currentS[5])

    if (pos1<=pos2<=pos3<=pos4<=pos5<=pos6):
        if(pos1 == pos2 or pos2 == pos3 or pos3 == pos4 or pos4 == pos5 or pos5 == pos6):
            pwMeetingCriteria += 1

    current += 1

print(pwMeetingCriteria)

