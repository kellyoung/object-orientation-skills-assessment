"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Abstraction: Abstraction is the idea that you can utilize certain methods and
   functions and expect the results you will get without actually knowing how the
   method or function is getting those results. An example of this would be the
   ".sort()" method on a list. You know you will get your list sorted either
   alphabetically or numerically but you don't necessarily know how the method is
   doing so.

   Encapsulation: Encapsulation is the concept of having your data close to the
   functionalities that work with the data. It is important because it keeps the
   data and functionalities safe from being misused or interfered with.
   Encapsulation makes code easier to read and work with.

   Polymorphism: Polymorphism is the flexibility of types without conditionals.
   It is the ability to redefine methods for derived classes without overriding
   methods or needing conditionals. For example, if you were to create a parent
   class of shape, the area method should be able to handle calculating the area
   of potential subclasses such as a triangle, circle, or rectangle.

2. What is a class?
   Class is a "type" of thing such as a String, File, or List. It allows you to
   store data in a structured way. It isn't as easy to modify as a dictionary,
   which allows it to keep its structure. It also has its own smarts meaning that
   it can own functions often referred to as methods. Classes allow you to not
   have to repeate code. For example, if you have a class called Animal you can
   instantiate different animals such as Ferret or Dog using the code that was
   already written in Animal.

3. What is an instance attribute?
   An instance attribute is an attribute associated with the individual occurence
   of a class. An example would be if you created an instance of pet such as
   fido = Pet() and you assigned fido.name = 'Fido'. The attribute 'name' is only
   associated with fido and not the entire class of Pet.

4. What is a method?
   A method is like a function defined on a class. It is different from a function
   because it can only be called in association to an object.

5. What is an instance in object orientation?
   An instance in object orientation is an individual occurence of a class.
   For example, if Pet is a class, and fido = Pet(), fido is an instance of
   the class Pet.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute as an attribute associated with the class and it will
   get passed down to every instance. An instance attribute is associated
   specifically with the instance the class is called on and will not affect
   the class it is from. An example of why you might use a class attribute
   is for example, if you had a class called Animal, you might have the attribute
   kingdom = 'Animalia'. Therefore, every instance or subclass would inherit
   the kingdom attribute. An instance attribute it is more useful to contain
   a state of an object/instance. For example, if you had a class called Cat and
   lives = 9. For a specific instance such as bob = Cat(), you might set
   bob.lives = 8 if he had lost a life. Therefore that is specific to bob
   and not all instances of Cat.


"""


# Parts 2 through 5:
# Create your classes and class methods

# Parts 2 and 3
class Student(object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        user_answer = raw_input(self.question + " > ")
        return user_answer == self.correct_answer


class Exam(object):
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        final_score = 0
        for question in self.questions:
            correct_answer = question.ask_and_evaluate()
            if correct_answer:
                final_score += 1

        return final_score

# Part 4
def take_test(exam, student):
    student_score = exam.administer()
    student.score = student_score


# was a little unclear of the directions for this question, but tried my best!
# my interpretation was to create a hard coded example of an exam
def example():
    example_exam = Exam("Example Exam")
    example_exam.add_question("How many states are in the U.S.A.?", "50")
    example_exam.add_question("Who was the first president?", "George Washington")
    example_exam.add_question("Who is our current president?", "Barack Obama")

    example_student = Student("Patty", "Cakes", "123 Gingerbread St.")

    take_test(example_exam, example_student)
    #to access the score from the test
    return example_student


# Part 5
class Quiz(Exam):
    def administer(self):
        final_score = super(Quiz, self).administer()
        return final_score > len(self.questions)/2
