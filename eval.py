import pytest as pt
import os
import pygit2 as git
#Grading structure based on https://github.com/The-College-of-the-Ozarks/2021DATASTRUCTURES/blob/main/README.md


def cloneBuilder(rootRepo):
    fNames = []
    sfh = "https://github.com/"
    igns = open('usernames.txt', 'r')
    people = []
    for name in igns:
        fNames.append(sfh + name + '/' + rootRepo + '.git')
        people.append(name)
    igns.close()
    return [fNames, people]




def main():
    #Clone repos to a temp folder
    repoName = input('Please enter the name of the repository that will be cloned from the students (case sensitive)')
    studentRepoList = cloneBuilder(repoName)
    print(studentRepoList[1])
    #Make the root dirs to clone into
    for student in zip(studentRepoList[1], studentRepoList[0]):
        if '#' not in student[0]:
            if not os.path.exists(os.getcwd() + '/' + str(student[0])):
                os.mkdir(os.getcwd() + '/' + str(student[0]))
            print('Made a folder for ' + student[0])
            os.chdir(os.path.join(os.getcwd() + '/' + str(student[0])))
            #Clone each student's repo
            print('Cloning ' + repoName + ' for ' + student[0])
            git.clone_repository(repos, '/' + str(student[1]))
        
    #Copy student folders into an appdata folder
            
    #TODO
    #For each student's assignment files, run pytest and grade?
    #TODO
    #Post-grading cleanup, delete what we dont need
    #TODO
                             











if __name__=='__main__':
    main()
