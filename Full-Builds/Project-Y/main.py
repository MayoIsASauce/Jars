# Storing and fetching student data from a database

# == IMPORT LIBRARIES == 
import libs.reader, libs.creator


# == PARSE THE STUDENTS DATA FROM DATABASE ==
students = libs.reader.parseStudents()


# == CREATE THE UI FOR SEARCHING DATA ==
libs.reader.UI.createInterface(students)



# Written 11/4/2020 by MayoIsASauce on github     ->    https://github.com/MayoIsASauce