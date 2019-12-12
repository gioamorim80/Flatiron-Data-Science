import copy

class School:
    def __init__(self, name=None, roster={}):
        self.name = name
        self.roster = roster

    def add_student(self, name, grade):
        if grade in self.roster:
            self.roster[grade].append(name)
        else:
            self.roster[grade] = [name]
        return self.roster
    
    def grade(self, grade):
        return self.roster[grade]
    
    #def sort_roster(self):
     
    #    for k in self.roster:
    #        sorted(self.roster.values())
    #    return self.roster

    def sort_roster(self):
        new_dict = copy.deepcopy(self.roster)
        for key in new_dict:
            new_dict[key].sort()
        return new_dict



    