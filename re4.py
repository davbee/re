import re

regex = r"^.+?(?=physician)"

test_str = "John Rolph (1793–1870) was a physician, lawyer, and political figure. He immigrated to Upper Canada in 1813 and practised law and medicine concurrently. In 1824, Rolph was elected to the Parliament of Upper Canada. He was elected as an alderman to Toronto's first city council but resigned after his council colleagues did not select him as the city's mayor."

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

    print(
        "Match {matchNum} was found at {start}-{end}: {match}".format(
            matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()
        )
    )

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print(
            "Group {groupNum} found at {start}-{end}: {group}".format(
                groupNum=groupNum,
                start=match.start(groupNum),
                end=match.end(groupNum),
                group=match.group(groupNum),
            )
        )

