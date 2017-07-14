mainList = []

num_users = int(raw_input("how many pie party goers? "))
num_pies = int(raw_input("how many pies were made? "))

for user in range(0, num_users):

    is_string = False
    user_name = ""
    while not is_string:
        user_name = raw_input("enter name for user " + str(user) + ": ")
        if not isinstance(user_name, str):
            print "Let's try that again..."
        else:
            is_string = True

    mainList.append([user_name])


for user in mainList:
    print user[0] + "'s turn"

    for pie in range(1, num_pies + 1):

        is_int = False
        score = 0
        while not is_int:

            try:
                is_int = True
                score = int(raw_input("(0 - 10) enter your integer score for pie #" + str(pie) + ": "))
                if score < 0 or score > 10:
                    raise ValueError
            except ValueError:
                print "try that again champ..."
                is_int = False

        mainList[mainList.index(user)].append(score)

totalsList = []

for x in range(0, num_pies):
    totalsList.append(0)

for list in mainList:
    x = 1
    print list[0] + "'s scores: "
    while x < len(list):

        totalsList[x - 1] += list[x]

        print "#" + str(x) + " score is " + str(list[x])
        x += 1

x = 0
while x < len(totalsList):
    print "pie #" + str(x + 1) + "'s score is: " + str(totalsList[x])
    x = x + 1