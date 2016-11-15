class Person:
    def __init__(self,initialAge):
        
        self.initialAge = initialAge
        self.age = age

        # Add some more code to run some checks on initialAge
        if age < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.initialAge = self.age
            
        # Do some computations in here and print out the correct statement to the console
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
            
        # Increment the age of the person in here  
    def yearPasses(self):
        self.age += 1
        
        
       
            
            
     
