# Data Generator
### Created by Matt August

I created this generator a while ago to test my skills in building and storing data in python. I recently repurposed it to generated student data for sql databases. The reason only 3,996 students can be generated is because of how the student ids work. There are four years of school and only 000-999 numbers 999*4 = 3,996.

## Features

- **generate \<int>** up to 3,996 students at once to Students.csv.
- **list** all students inside the Students.csv.
- **make** a specific student to specifications.
- Precise data retrieval.
- Entirely open-sourced.

### Commands can be issued such as
```python
sophmore year -> retrieve the graduating year of sophmores.
freshman first -> retrieve the first names of all freshman
generate 1000 -> generates 1000 students to Students.csv up to a maximum of 3,996 students
```
and many more similar commands.

  
### Errors:
number out of range, the number of students in Students.csv + the amount you are generating exceeds 3,996
