import pytest as pt
import os
import git
#Grading structure based on https://github.com/The-College-of-the-Ozarks/2021DATASTRUCTURES/blob/main/README.md


def cloneBuilder(rootRepo):
    fNames = []
    sfh = "https://github.com/"
    igns = open('usernames.txt', 'r')
    for name in igns.readAllLines():
        fName.append(name)
    return fNames




def main():
    #Clone repos to a temp folder
    repoName = input('Please enter the name of the repository that will be cloned from the students (case sensitive)')
    studentReopList = cloneBuilder(repoName)
    for student in studentRepoList:
        os.mkdir(os.getcwd() + student)
        
    #Copy student folders into an appdata folder
    #TODO
    #For each student's assignment files, run pytest and grade?
    #TODO













if __name__=='__main__':
    main()
