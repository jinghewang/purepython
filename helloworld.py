__author__ = 'robin'

if __name__ == "__main__":
    print "Hello";

#define a function
def welcome():
    print("Welcome to my python class")
# define a function by arg
def welcome_bylevel( name, level ):
  print ( 'Welcome ' + name + ' to the program =)' )
  print ( 'We will try some things out.' )
  if level == 'pro': print ( 'Be patient, I am beginner.' )
  print ('')


welcome()
welcome_bylevel( 'Alex', 'beginner' )
welcome_bylevel( 'Viki', 'pro' )




