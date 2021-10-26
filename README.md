# 2021DATASTRUCTURES
Reources for the FA 2021 CSC Data Structures Class


Structure for homework submissions is as follows:

Ex: /studantName/

          Problem1/
          
                    assignment1/
                    
                    assignment2/
          ProblemN/          
                    assignmentN/


In order to run the testing program AT ALL, two naming conventions need to be followed:

The student's file  name needs  to be prefixed with 'test_'

The main method in the student's file needs to be prefixed with 'test_' 

(The main method does not need any explicit calls, this program uses pytest which automatically will run the test method)




How this works:

The main file runs, using pytest in order to grade the student files 

testCaseGenerator.py is run, this module will use randomly generated inputs to try and match outputs (still being designed)
