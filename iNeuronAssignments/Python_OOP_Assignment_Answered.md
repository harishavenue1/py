## Python OOP Assignment

Q1. What is the purpose of Python's OOP?

    To implement basis building blocks of programming with objects such as Encapsulation, Polymorphism,
    inheritance and abstraction.

Q2. Where does an inheritance search look for an attribute?

    First check starts at the object created, then at class from which the object got created and finally at parent
    class.

Q3. How do you distinguish between a class object and an instance object?

    Class variables are declared inside a class but outside any function. Instance variables are declared inside the
    constructor which is the __init__ method.

Q4. What makes the first argument in a class’s method function special?

    First argument is nothing but the class object itself, it's only a convention.

Q5. What is the purpose of the init method?

    The init method helps the class initialize the object's attributes and serves no other purpose.

Q6. What is the process for creating a class instance?

    To create instance of a class, call the class using class name and pass in arguments its __init__ method accepts.
    Ex: classObj = ClassName(arg1, arg2)

Q7. What is the process for creating a class?

    To create a class, you call the class keyword and followed by a name.
    Ex: class ClassName(object):

Q8. How would you define the superclasses of a class?

    The class from which a class inherits is called the parent or superclass.
    
    # Parent Class
    
    class Person(object):
    
        def __init__(self, name):
            self.name = name
    
        def getName(self):
            return self.name
          
        def isEmployee(self):
            return False
    
    # Inherited or Subclass (Note Person in bracket)
    
    class Employee(Person):
    
        def __init__(self, name, eid):
            super().__init__(name)
            self.empID = eid

Q9. What is the relationship between classes and modules?

    Modules are functions which perform specific task and classes allows access to these functions.

Q10. How do you make instances and classes?

    Classes using as, class ClassName(object) & Instances of the Classes as, classObj = ClassName(arg1, arg2)

Q11. Where and how should be class attributes created?

    Class attributes are created outside the init method.

Q12. Where and how are instance attributes created?

    Instance attributes are created inside the init method.

Q13. What does the term "self" in a Python class mean?

    "self" keyword is nothing but the object itself.

Q14. How does a Python class handle operator overloading?

    Performed by respective classes as implemented within each classes, ex: int (+) for adding, str (+) for
    concatenating.

Q15. When do you consider allowing operator overloading of your classes?

    Based on the input, the classes implementation check for overloading, ex: int (+) for adding, str (+) for
    concatenating.

Q16. What is the most popular form of operator overloading?

    Addition operator, int (+) for adding, str (+) for concatenating.

Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?

    Inheritance and polymorphism are fundamental concepts of OOP. These concepts help us to create code that can be
    extended and easily maintainable.

Q18. Describe three applications for exception processing.

    a) While working with Files, incase file is not available to access, FileNotFound exception is triggered
    b) While performing numeric operations, in case of divide by 0, ZeroDivisionError exception is triggered
    c) While accessing list elements, in case of incorrect access to unavailable index, arrayIndexOutOfBound exception is
    triggered

Q19. What happens if you don't do something extra to treat an exception?

    Program will be terminated with exception details.

Q20. What are your options for recovering from an exception in your script?

    Adding logic inside Except block to continue execution.

Q21. Describe two methods for triggering exceptions in your script.

    Raise and Except

Q22. Identify two methods for specifying actions to be executed at termination time, regardless of whether an exception
exists.

    Finally is a block which executes whether an exception occurred.

Q23. What is the purpose of the try statement?

    The try block lets you test a block of code for errors. The except block lets you handle the error. The else block
    lets you execute code when there is no error.

Q24. What are the two most popular try statement variations?

    try,except,else & try,except,finally

Q25. What is the purpose of the raise statement?

    To stop the execution with a reason based on certain logical event.

Q26. What does the assert statement do, and what other statement is it like?

    The assert keyword is used when debugging code. The assert keyword lets you test if a condition in your code returns
    True, if not, the program will raise an AssertionError.
    Ex:
    x = "hello"
    
        #if condition returns False, AssertionError is raised:
        assert x == "goodbye", "x should be 'hello'"
    
    Output: AssertionError: x should be 'hello'

Q27. What is the purpose of the with/as argument, and what other statement is it like?

    The with statement is a replacement for commonly used try/finally error-handling statements. A common example of
    using the with statement is opening a file. To open and write to a file in Python, you can use the with statement as
    follows:
    
        with open("example.txt", "w") as file:
        file.write("Hello World!")

Q28. What are *args, **kwargs?

    *args are Non-Key Valued arguments, ex below

    def example_nonkeyed_args(*argv):
        for param in argv:
            print(param)

    example_nonkeyed_args('Hello', 'Welcome', 'To', 'iNeuron')

    **kwargs are Key Value type of arguments in Python

    def example_of_kwargs(**kwargs):
        print("Value of host : ", kwargs['host'])
        print("Value of port : ", kwargs['port'])
        print("Value of password : ", kwargs['pswd'])

    for k, v in kwargs.items():
        print("Key is ", k, ' and Value is ', v)

    example_of_kwargs(host='170.80.80.80', port=9021, pswd='XXFGH')
    example_of_kwargs(port=9021, pswd='XXFGH', host='170.80.80.80')

Q29. How can I pass optional or keyword parameters from one function to another?

    def func(string1, string2="World!"):
    print(string1 + string2)
    
    func(string2='World!', string1="Hello") # output -> Hello World!
    func(string1='Hello') # output -> Hello World!, as World! is already provided as parameter to function.

Q30. What are Lambda Functions?

    A lambda function is an anonymous function, which is defined without a name, it can take any number of arguments
    but, unlike normal functions, evaluates and returns only one expression.

Q31. Explain Inheritance in Python with an example?

    In below example, Person is parent class and Employee is child class extends Parent using (Person).
    Parent class has only name argument, whereas the child class Employee has employeeId (eid).
    So to instantiate this, super() method is called, to initialize the name from parent class or super class and eid from
    child class. Parent class Person provides getName and isEmployee methods to child class.

    # Parent Class

    class Person(object):

        def __init__(self, name):
            self.name = name
    
        def getName(self):
            return self.name
          
        def isEmployee(self):
            return False

    # Inherited or Subclass (Note Person in bracket)

    class Employee(Person):

        def __init__(self, name, eid):
            super().__init__(name)
            self.empID = eid

Q32. Suppose class C inherits from classes A and B as class C(A, B).Classes A and B both have their own versions of
method func(). If we call func() from an object of class C, which version gets invoked?

    Invocation is from ClassA, as class-A is the first argument in class-C.

Q33. Which methods/functions do we use to determine the type of instance and inheritance?

    Using isinstance() function, we can test whether an object is an instance of specific type or class. In the case of
    inheritance, we can check if the specified class is the parent class of an object.

Q34. Explain the use of the 'nonlocal' keyword in Python.

    The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to
    the inner function. Use the keyword nonlocal to declare that the variable is not local.

Q35. What is the global keyword?

    The global keyword allows us to modify the variable outside the current scope. It is used to create a global
    variable and make changes to the variable in a local context.