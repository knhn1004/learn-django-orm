from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q

# Part 2
#################################################################


#  def student_list(request):
#  posts = Student.objects.all()
#
#  print(posts)
#  print(posts.query)
#  print(connection.queries)
#
#  return render(request, 'output.html', {'posts': posts})

#  def student_list(request):
#  #  using Q objects
#  posts = Student.objects.filter(
#  Q(surname__startswith='austin') | ~Q(surname__startswith='baldwin') | Q(surname__startswith='avery-parker'))
#
#  print(posts)
#  print(posts.query)
#  print(connection.queries)
#
#  return render(request, 'output.html', {'posts': posts})

# Part 3
#################################################################

#  def student_list(request):
#  posts = Student.objects.filter(classroom=1) & Student.objects.filter(
#  age=20)
#
#  print(posts)
#  print(posts.query)
#
#  return render(request, 'output.html', {'posts': posts})

#  def student_list(request):
#  posts = Student.objects.filter(
#  Q(surname__startswith='baldwin') & Q(firstname__startswith='lakisha'))
#
#  print(posts)
#  print(posts.query)
#
#  return render(request, 'output.html', {'posts': posts})

# Perform an UNION query
#################################################################

#  def student_list(request):
#  # union removes any 'duplicated' rows
#  # union can only be used on the columns with same name
#  # in this case: 'firstname'
#  #  posts = Student.objects.all().values_list('firstname').union(
#  #  Teacher.objects.all().values_list('firstname'))
#
#  #  .values_list() returns a Queryset with an array of objects
#  #  .values() returns a Queryset with dictionary
#  posts = Student.objects.all().values('firstname').union(
#  Teacher.objects.all().values('firstname'))
#
#  print(posts)
#  print(posts.query)
#
#  return render(request, 'output.html', {'posts': posts})

# Perform a NOT query
#################################################################

#  def student_list(request):
#  #  posts = Student.objects.exclude(age=20) & Student.objects.exclude(
#  #  firstname__startswith='raquel')
#
#  posts = Student.objects.exclude(age__gt=20)
#
#  print(posts)
#  print(posts.query)
#  print(connection.queries)
#
#  return render(request, 'output.html', {'posts': posts})

def student_list(request):
    #  posts = Student.objects.exclude(age=20) & Student.objects.exclude(
    #  firstname__startswith='raquel')

    #  '~Q' means NOT
    posts = Student.objects.filter(
        ~Q(age__gt=20) & ~Q(surname__startswith='baldwin'))

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})
