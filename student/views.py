from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q

# Part 2
#################################################################


#  def student_list(request):
#  students = Student.objects.all()
#
#  print(students)
#  print(students.query)
#  print(connection.queries)
#
#  return render(request, 'output.html', {'students': students})

#  def student_list(request):
#  #  using Q objects
#  students = Student.objects.filter(
#  Q(surname__startswith='austin') | ~Q(surname__startswith='baldwin') | Q(surname__startswith='avery-parker'))
#
#  print(students)
#  print(students.query)
#  print(connection.queries)
#
#  return render(request, 'output.html', {'students': students})

# Part 3
#################################################################

#  def student_list(request):
#  students = Student.objects.filter(classroom=1) & Student.objects.filter(
#  age=20)
#
#  print(students)
#  print(students.query)
#
#  return render(request, 'output.html', {'students': students})

#  def student_list(request):
#  students = Student.objects.filter(
#  Q(surname__startswith='baldwin') & Q(firstname__startswith='lakisha'))
#
#  print(students)
#  print(students.query)
#
#  return render(request, 'output.html', {'students': students})

# Perform an UNION query
#################################################################

#  def student_list(request):
#  # union removes any 'duplicated' rows
#  # union can only be used on the columns with same name
#  # in this case: 'firstname'
#  #  students = Student.objects.all().values_list('firstname').union(
#  #  Teacher.objects.all().values_list('firstname'))
#
#  #  .values_list() returns a Queryset with an array of objects
#  #  .values() returns a Queryset with dictionary
#  students = Student.objects.all().values('firstname').union(
#  Teacher.objects.all().values('firstname'))
#
#  print(students)
#  print(students.query)
#
#  return render(request, 'output.html', {'students': students})

# Perform a NOT query
#################################################################

#  def student_list(request):
#  #  students = Student.objects.exclude(age=20) & Student.objects.exclude(
#  #  firstname__startswith='raquel')
#
#  students = Student.objects.exclude(age__gt=20)
#
#  print(students)
#  print(students.query)
#  print(connection.queries)
#
#  return render(request, 'output.html', {'students': students})

#  def student_list(request):
#  #  students = Student.objects.exclude(age=20) & Student.objects.exclude(
#  #  firstname__startswith='raquel')
#
#  #  '~Q' means NOT
#  students = Student.objects.filter(
#  ~Q(age__gt=20) & ~Q(surname__startswith='baldwin'))
#
#  print(students)
#  print(students.query)
#  print(connection.queries)
#
#  return render(request, 'output.html', {'students': students})

#######################
# SELECT and OUTPUT individual fields
# only()
#######################
#  def student_list(request):
#  students = Student.objects.filter(classroom=1).only('firstname', 'age')
#
#  print(students)
#  print(students.query)
#  print(connection.queries)
#
#  return render(request, 'output.html', {'students': students})

#######################
# using raw queries
# raw()
#######################
def student_list(request):
    #  students = Student.objects.all()
    # using raw queries
    #  query = 'SELECT * FROM student_student WHERE age=20'
    query = 'SELECT * FROM student_student'
    # limiting to 2 items
    students = Student.objects.raw(query)[:2]

    #  print(students)
    for s in students:
        print(s)
    print(students.query)
    #  print(connection.queries)

    return render(request, 'output.html', {'students': students})
