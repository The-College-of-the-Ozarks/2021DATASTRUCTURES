import os
import pygit2 as git
import shutil as shell
#import unittest as ut
import pytest as ut

'''
Reads input from the usernames.txt file to determine who to clone repositories from.
Repository MUST be public and follow conventions from:
https://github.com/The-College-of-the-Ozarks/2021DATASTRUCTURES/blob/main/README.md
'''
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

'''
Moving all student folders into a custom location for ease of grading later
All files are copied, and the copies will be removed after usage
This is run after repositories are cloned
'''
def setupRepo(count, students, rootDir):
    #Make new folder to store student files
    root = os.path.join(os.path.expandvars('%appdata%'),'homework')
    if os.path.exists(root):
        os.rmdir(root)
    os.mkdir(root)
    for student in range(0,count):
        if not os.path.exists(os.path.join(root + '/' + students[student][0])):
            os.mkdir(os.path.join(root + '/' + students[student][0]))
        shell.copytree(os.path.join(rootDir + '/' + students[student][0]), os.path.join(root + '/' + students[student][0]))
    #Each student now has their own folder with their python files
    return os.path.join(os.path.expandvars('%appdata%'),'homework')

'''
This is where the actual unit tests are run
the files ran against are temporarily stored in ...AppData/Roaming/homework
and listed by username
'''
def evaluate(rwd, count):
    studentFolders = os.listdir(rwd)
    testInput = open(os.path.join(os.getcwd(), "unitTestInput.txt"), 'r')
    #
    for i in range(0, count):
        pass
            
    return


def main():
    #Clone repos to a temp folder
    '''repoName = input('Please enter the name of the repository that will be cloned from the students (case sensitive)')
    studentRepoList = cloneBuilder(repoName)
    print(studentRepoList[1])
    studentcount = 0
    rootDir = os.getcwd()
    #Make the root dirs to clone into
    for student in zip(studentRepoList[1], studentRepoList[0]):
        if '#' not in student[0]:
            if not os.path.exists(os.getcwd() + '/' + str(student[0])):
                os.mkdir(os.getcwd() + '/' + str(student[0]))
            print('Made a folder for ' + student[0])
            os.chdir(os.path.join(os.getcwd() + '/' + str(student[0])))
            #Clone each student's repo
            print('Cloning ' + repoName + ' for ' + student[0])
            git.clone_repository(studentRepoList[0], '/' + str(student[1]))
        studentcount = studentcount + 1
    #Setup the files in these repos to grade
    evaluate(setupRepo(studentcount, studentRepoList, rootDir), studentcount)
    '''
    #The key to the solution lies here
    #For each student folder, run this pytest. use time to find out how long execution took.
    os.chdir('')
    os.system('python -m pytest'  + '>> out.txt')
    
    
if __name__=='__main__':
    main()
