"""
Splits entered strings into groups based on even or odd position in word
Determines intended number of words based on first input
Prints each entered word seperated with a space on each line, one line per word
"""
def even_odd_string():

    #inputs number of desired test cases
    test_case = int(input())

    #creates empty list for string entries
    word_list = []

    #funtion to appent input words into word_list
    def input_words():
        count = test_case
            
        while count > 0:
            word_list.append(input())
            count -= 1
            
    #seperates words by letter position into even and odd
    def sort_word():
       
        for x in word_list:

            word = x
            
            odd_letters = ""
            even_letters = ""
            
            position = 0
            
            for i in word:
                
                if position % 2 == 0:
                    even_letters += i
                    
                else:
                    odd_letters += i

                position += 1

            print(even_letters + " " + odd_letters)
                
    input_words()
    sort_word()

even_odd_string()

       
    



    
    

