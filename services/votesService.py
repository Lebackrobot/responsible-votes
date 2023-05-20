from abc import abstractmethod
import csv


class votesService():

    @abstractmethod
    def get():
        votes = {}

        with open('./db.csv', 'r') as db:
            reader = csv.reader(db, delimiter=',')

            for row in reader:
                candidate = row[1]
                votes[candidate] = row[2]

        return votes

    @abstractmethod
    def updateVote(name):
        with open('./db.csv', 'r') as db:
            reader = csv.reader(db, delimiter=',')

            rows = []
            for row in reader:
                if row[1] == name:
                    vote = int(row[2]) + 1
                    rows.append([row[0], row[1], vote])
                else:
                    rows.append(row)

        with open('./db.csv', 'w', newline='') as db:
            writer = csv.writer(db)
            writer.writerows(rows)

        return True
