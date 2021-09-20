import pytest as pt
import os
import git
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
    for student in studentRepoList[1]:
        if '#' not in student:
            os.mkdir(os.getcwd() + '/' + str(student))
            print('Made a folder for ' + student)
            #Clone each student's repo
            print('Cloning ' + repoName + ' for ' + student)
            cloned_repo = repo.clone(os.path.join(rw_dir, '')

    studentReopList = cloneBuilder(repoName)
    for student in studentRepoList:
        os.mkdir(os.getcwd() + student)
        os.chdir(os.getcwd() + student)
        
    #Copy student folders into an appdata folder
            
    #TODO
    #For each student's assignment files, run pytest and grade?
    #TODO












if __name__=='__main__':
    main()
