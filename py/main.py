def listTopFive(ls):
    scores = []
    for d in ls:
        score = (int(d["math"]) + int(d["physics"]) + int(d["chemistry"]) + int(d["english"]))
        scores.append({'name' : d['name'], 'score' : score})
    scores.sort(key=lambda item: item["score"], reverse=True)
    for i in range(5):
        print(f"{scores[i]['name']} : {scores[i]['score']}")

def averageScoreOfAll(ls):
    for d in ls:
        average = (int(d["math"]) + int(d["physics"]) + int(d["chemistry"]) + int(d["english"])) / 4
        print(f"{d['name']} : {average}")

def findStudent(ls):
    sName = input("Enter the name of the student: ")
    for d in ls:
        if (d["name"].lower() == sName.lower()):
           print(f"\nName: {d['name']}")
           print(f"Math: {d['math']}")
           print(f"Physics: {d['physics']}")
           print(f"Chemistry: {d['chemistry']}")
           print(f"English: {d['english']}")
           return
    print("\nThe entered student is not in the list.")

def listAllNames(ls):
    for d in ls:
        print(d['name'])

def listAllDetails(ls):
    for d in ls:
       for key in d:
           print(f"{key} : {d[key]}")
       print()

def maxScore(ls):
   maxScore = -1
   mexScoreDet = None
   for d in ls:
      currentScore = 0
      currentScore += int(d["math"])
      currentScore += int(d["physics"])
      currentScore += int(d["english"])
      currentScore += int(d["chemistry"])
      if (currentScore > maxScore):
          maxScore = currentScore
          maxScoreDet = d
   print(f"\nThe student with the maximum score of {maxScore} is {maxScoreDet['name']}.\n")

def main():
    ls = []
    with open("students.csv", "r") as f:
        for line in f:
            d = {}
            arr = line.strip().split(",")
            d["name"] = arr[0]
            d["math"] = arr[1]
            d["english"] = arr[2]
            d["physics"] = arr[3]
            d["chemistry"] = arr[4]
            ls.append(d)
    while (1):
        print("\n1. List all the student names.")
        print("2. List the details of all the students.")
        print("3. List the detail of student with the highest score.")
        print("4. Search for a student.")
        print("5. Average score of all students.")
        print("6. List top 5 students.")
        print("7. Exit.")
        ch = int(input("\nEnter your choice: "))
        match ch:
            case 1:
                print()
                listAllNames(ls)
            case 2:
                print()
                listAllDetails(ls)
            case 3:
                print()
                maxScore(ls)
            case 4:
                print()
                findStudent(ls)
            case 5:
                print()
                averageScoreOfAll(ls)
            case 6:
                print()
                listTopFive(ls)
            case 7:
                print()
                break;
            case _:
                print()
                print("Enter a valid choice.")

if __name__ ==  "__main__":
    main()
