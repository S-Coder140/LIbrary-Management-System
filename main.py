
# *************************************Library Management System***************************************

# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book
# users for their input
''' This system can also be made by pointing on OOP as object and classes.
However this program has not used any if-main method and can be run by impporting 
the system to any other programs '''
# *************************************************
# ----------------Sayam Maity----------------------
# *************************************************

import pyttsx3 # pip install pyttsx3
# pyttsx3 is a text-to-speech conversion library in Python.
import datetime
# Third-party library with expanded time zone and
#  parsing support.# Third-party library with expanded time zone and parsing support.
import time 
# time module is a built in Module
# time module is being used for counting time 
import random
# random module is a built in module 
# random module is used to generate the 4 digit libraryID 
from plyer import notification
# download plyer module using 'pip install plyer'
# Plyer is used to send the noficiation to the user 

# defining the engine 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(text): # function to speak a given string 
    """ Speak function will pronounce the string which is passed to it."""
    engine.say(text)
    engine.runAndWait()


user_points = 0
# this LMS has a daily gradng system for the user 
# printing statements ..... 
print ()
print ("**************************************")
print ("    Welcome to World_Sayam Library    ")
speak("    Welcome to WorldSayam Library    ")
print ("       Online Library System          ")
print ("**************************************")
print ()
print ('''Choose one of the following numbers to
see their corresponding items :''')
print ("1. See all the lists of the books")
speak("1. See all the lists of the books")
print ("2. Lend the book from the library")
speak ("2. Lend the book from the library")
print ("3. Add a book to the library")
speak ("3. Add a book to the library")
print ("4. Return a book to the library")
speak ("4. Return a book to the library")
print ("5. See terms of this library")
speak ("5. See terms of this library")
print ()
print ()
print ("But first you need to give your libraryID or make a new libraryID")
print ("press 1 to give your existing libraryID")
speak ("press 1 to give your existing libraryID")
print ("press 2 to make a new libraryID")
speak ("press 2 to make a new libraryID")
print ()
# used Exception handling to make the LMS user-friendly and not breaking the program 
# using try.....
try: 
    c = open('libraryID.txt')
    # opening the text file to store the libraryIDs

    choice_successful = False 
    # choice_successful is a variable to break the loop when the user makes or enter a libraryID successfully 
    libraryID = ["1234","7091","8918"]
    # a list to store the libraryID temporarily
    # running a while loop 
    while choice_successful == False :
        speak("Enter your choice")
        choice_libraryID = int(input("Enter your choice (1 or 2) : "))
        # taking a choice as the user input to enter a previously made ID or making a new ID
        if choice_libraryID == 1:
            # if the user chose to enter a previously made libraryID  (a trial version)
            # printing statements
            print ("For free visit to the library you can enter the 1234 as your libraryID.")
            speak ("For free visit to the library you can enter the 1234 as your libraryID.")
            speak("Enter your ID ")
            ID = int(input("Enter your ID : "))
            if ID in libraryID and ID == 1234:
                # if the user entered the trial version of the app
                # printing statements
                print ("You are using a trial version of the library")
                speak ("You are using a trial version of the library")
                print ("Thank you.....")
                speak ("Thank you.....")
                print ()
                print ("Please take our subscription to take the full access to the library")
                print ('Please press YeS in bold letters to take the premium content .')
                speak("Enter your choice")
                user_premium = str(input("Enter your choice : "))
                # a variable to enter the user choice to buy the premium 
                if user_premium == 'YES':
                    # if the user opted for buying the premium version ....
                    # printing about how and why to take the premium .......
                    print ("Our premium content has all our options of the library including adding a new book if the book is good.")
                    print ("Our monthly plan needs a payment of Rs. 100 per month and the annual plan incudes Rs. 80 per month ")
                    print ("Please send a mail on sayamcoding4321@gmail.com to get the bank account on which the payment shold be done . ")

                choice_successful = True
                # to break the loop 
            elif ID in libraryID:
                # if the user chose to enter a previously made libraryID
                print ("Your library ID is correct .")
                speak("Your libraryID is correct . Thank you")
                print ("Thank you ........")
                choice_successful = True
                # to break the loop
            else :
                # if the ID is incorrect 
                print ("Your ID is incorrect")
                speak ("Your ID is incorrect")
                print ("Either make a new libraryID or regive the libraryID")
                speak ("Either make a new libraryID or regive the libraryID")
        elif choice_libraryID == 2:
                # if the user chose to make a new libraryID
                # b = open('libraryID.txt,'a')
                # to open the library ID and add the new ID 
                print ("Making a libraryID...")
                speak ("Making a libraryID...")
                # using the random module.....
                new_libraryID = random.randint(1000,5000)
                # new_libraryID is the 4-digit new libraryID for the user 
                new_libraryID= str(new_libraryID)
                # making the new_libraryID a str to append the new_libraryID in the libraryID.txt 
                # contents = c.write(new_libraryID)
                
                # printing statements
                print ("New libraryID made .....")
                # printing as a f string.......
                # Note : f-string is a new structure added to the python library . Very old python versions cannot access it
                print (f"Your new libraryID is {new_libraryID}")
                print ()
                print ("Just remember this ID ")
                speak("Just remember the written ID ")
                print ()
                choice_successful = True
                # to break the loop 
        else : 
            # if the user has given any other choice except 1 and 2
                print ("wrong input.. please try again")
                speak ("wrong input.. please try again")
                print ()
    # finially asking the user to give the libraryID if it is new and also if it is old
    speak("Now finally give the ID : (You cannot enter if the ID is wrong) : ")
    user_ID = int(input("Now finally give the ID : (You cannot enter if the ID is wrong) : "))
    user_ID = str(user_ID)
    # typecasting the user_ID into a string to write the ID in a file in future 
    if user_ID in libraryID:
        # if the ID is getting matched
        correct_ID = user_ID
        # printing statements
        print ("Your library ID has been verfied . Thank you ")
        speak ("Your library ID has been verfied . Thank you ")
        print ("You will be redirected to the library")
        speak ("You will be redirected to the library")
        print ()
        print ()
        print ("****************** Main Library ******************")
        speak("welcome to the main library")
        print ()
        print ()
        print ('''Choose one of the following numbers to see their corresponding items :''')
        print ("1. See all the lists of the books")
        print ("2. Lend the book from the library")
        print ("3. Add a book to the library")
        print ("4. Return a book to the library")
        print ("5. See terms of this library")
        print ("6. Exit from the library")
        speak ("1. See all the lists of the books")
        speak ("2. Lend the book from the library")
        speak ("3. Add a book to the library")
        speak ("4. Return a book to the library")
        speak ("5. See terms of this library")
        speak ("6. Exit from the library")
        speak ()
        speak ()
        # printing the grarded system of the library for the user 
        print ("There are a bag of points for you . Let me tell you in detail about this ")
        print ("Every lenting a book and retuning a book even reading the list of the books increases your points")
        print ("What is the benifit of the points ?? There will be a high score ! If you crack a certain level of points .You can get the premium content free")
        print ("For reading this , I give you 5 pointa !!! Yay !!!")
        speak ("There are a bag of points for you . Let me tell you in detail about this ")
        speak ("Every lenting a book and retuning a book even reading the list of the books increases your points")
        speak ("What is the benifit of the points ?? There will be a high score ! If you crack a certain level of points .You can get the premium content free")
        speak ("For reading this , I give you 5 pointa !!! Yay !!!")
        user_points = user_points+5
        # increasing 5 points 
        print ("You have now",user_points,"points")
        # showing the total points till then
        user_exit = False 
        # a variable to run the loop and exit the loop when needed
        no_of_books = 5
        # no_of_books = total number of books in the library
        books = []
        # books keeping as a empty list to store the content of the book as the file name 
        list_of_books = [ "Harry Potter","Amazing Science","History of Medival India","Programming with Python","C++ fun"]
        # list for the name of the books
        book_file_name = ['book.txt','book.txt','book.txt','book.txt','book.txt']
        # books keeping as a empty list to store the content of the book as the file name
        # running a while loop 
        while user_exit == False:
            speak("Enter your choice now : ")
            user_choice = int(input("Enter your choice now : "))
            # taking the user input to take the choice what he/she will do to the library 
            if user_choice == 1:
                # if the user chose 1 as their choice
                # 1. See all the lists of the books
                # printing statements
                print ('showing all the lists of the books ')
                speak ('showing all the lists of the books ')
                print ()
                # running a for loop to print all the books according their index with a new line formation
                # i is the index of the for loop
                # no_of_books is the total number of books present in the library
                for i in range (1,no_of_books):
                    print( list_of_books[i])
                    # printing the list of the books according to the index of i 
                print ()
                user_points = user_points+5
                # increasing 5 points 
                # printing the total user points 
                print ("You have now",user_points,"points")
            elif user_choice == 6:
                # 6. Exit from the library
                print ("Exiting from the library")
                speak ("Exiting from the library")
                # open and read the highscore.txt 
                d = open('highscore.txt','rw')
                file_content = d.read()
                file_content = int(file_content)
                # if the user points of the day is bigger than the previous high score , then the new 
                # highscore will be set as the user_points
                if user_points > file_content:
                    contents = c.write(user_points)

                # user_points = user_points+5
                print ("You have now",user_points,"points")
                user_exit = True
                # breaking the while loop
                # user_points = user_points+5
                print ("You have now",user_points,"points")
                # printing total number of points 
            elif user_choice == 2 :
                # 2. Lend the book from the library

                speak('Enter the name of the book you want to lend : ')
                book_name = str(input('Enter the name of the book you want to lend : '))
                # asking the book name from the user 
                # printing statements
                print ()
                print ("Trying to lend the book.....")
                speak ("Trying to lend the book.....")

                '''if the book is already in the library then the user can lend the book otherwise
                the management system will not allow for lending and say which user with the libraryID has taken
                the book and also will get notified whether any book has been returned to the library or not ...'''
                if book_name in list_of_books:
                    print ("ok! Your book has been lent .....")
                    speak ("ok! Your book has been lent .....")
                    no_of_books = no_of_books-1
                    # making the no_of_books decreased by 1 otherwise if the for loop showing the list of the books will give an index error 
                    list_of_books.remove(book_name)
                    # removing the item from the main Library list 
                    # notifying the system of the user that a book has been lent from the library....
                    notification.notify(title = "Book Lent",message ="A book has been lent by the user from the library",timeout= 12)
                    print ("Remember to return the book after 2 hours .....")
                    speak("A book has been lent by the user from the library")
                    speak("Return the book in 2 hours")
                    # setting and getting the time of the system in which the user is using the library 
                    user_time = int(datetime.datetime.now().hour)
                    # setting the time when the user have to submit the lent book
                    returning_time = user_time + 2
                    while True :
                        # the time of returning the book 
                        if returning_time == user_time:
                            notification.notify(title = "Return the book",message ="Please return the book which you have just taken",timeout= 12)
                            print ("Please return the book")
                        
                            speak ("Please return the book")
                            user_answer = ''
                            while user_answer == "YES"  :
                                user_answer = str("Write Yes in bold letters")
                            print ("Thank you for returning the book...")
                            speak ("Thank you for returning the book...")
                            break 
                    user_points = user_points+5
                    # increasing the points of the user 
                    print ("You have now",user_points,"points")

                    # printing statements
                    print ()
                    print ("Do you want to read the book now?")
                    print ("Press 1 to read the book now and 2 to read the book later")
                    speak ("Do you want to read the book now?")
                    speak ("Press 1 to read the book now and 2 to read the book later")
                    speak("Enter your choice")

                    read_book = int(input("Enter your choice : "))
                    # taking the user input to see if the user asked for opening and reading the book instantly
                    if read_book == 1:
                        # printing statements
                        print ("Ok opening the book......")
                        speak ("Ok opening the book......")
                        print()
                        print ()
                        print ("*******************************************************")
                        
                        print ("opening the book....")
                        speak ("opening the book....")
                        if book_name == "Amazing Science" :
                            # opening the text file and reading the content 
                            t = open('book.txt')
                            content = t.read()
                            print (content)
                            t.close()

                        '''
                        This system should be improved .IF the user returns a book he will give the content of the book
                        and the file with the content will get saved in a .txt file named by the name of the book.
                        and it will get appended in the list book_file_name ....
                        When a user will lent the book, the book should get a loop where the index of the book in the book_name list
                        will be taken and the file name will be taken from the same index of the book in the book_file_name list

                        '''
                        
                        print ("*******************************************************")
                    elif read_book == 2 :
                        # if the user chose for reading later 
                        print ("Why hurry! when you can read it later ..Book saved successfully")
                        speak ("Why hurry! when you can read it later ..Book saved successfully")
                        '''
                        This system shoul be improved .
                        Whenever a user selects for reading the book later , 
                        the book will be downloaded in file explorer of the user as a .txt file
                        '''
                    else :
                        # if the user give wrong choices 
                        print ("Wrong input .....Try again")
                        speak ("Wrong input .....Try again")

                else :
                    # if the book is not present and is taken by someone else 
                    # printing statements
                    print ("Book not present in Library")
                    speak ("Book not present in Library")
                    print(f"{book_name} is taken by the user with the libraryID {correct_ID}")
                    print ()
                    print ("We will notify you when the book is returned by the user")
                    speak ("We will notify you when the book is returned by the user")


            elif user_choice == 3 :
                # 3.Adding a book to the library
                print ("Adding a book to the library")
                print ("Please make sure that the book name and the content is correct")
                speak ("Adding a book to the library")
                speak ("Please make sure that the book name and the content is correct")
                print ()
                speak("Enter the name and contents of the book : ")
                add_book_name = str(input("Enter the name of the book : "))
                # asking the user for entering book name to the library 
                add_book_content = str(input("Enter the content of the book : "))
                # asking the user for adding the conent of the book in the library 
                ''' 
                This system should be improved.
                If the user enters only a word or a text less than 150 words or just enters a space,
                the content will not get saved as a book. It should be either taken the user input again 
                for the content (can be done by loops) or get ignored....

                '''
                # adding the content of the book in a file
                list_of_books.append(add_book_name)
                book_txt_file = add_book_name+".txt"
                book_file_name.append(book_txt_file)
                no_of_books = no_of_books+1
                # increasing the total number of books
                book_content = add_book_content
                f = open(add_book_name,'w')
                f.write(book_content)
                f.close
                print ("Book successfully added.....")
                speak("Book successfully added.....")
                # sending a notification to the user
                notification.notify(title = "Book Returned",message ="A book has been returned by the user to the library..Chek out now...",timeout= 12)
                # print ("Remember to return the book after 5 days .....")
                print ("You can check your own book.....How fun is that!")
                print ("****************************************************")
                speak ("A book has been returned by the user to the library")
                user_points = user_points+5
                # increasing 5 points 
                print ("You have now",user_points,"points")
                # showing total points 

            elif user_choice == 5:
                # See terms of this library
                print ("*******************************************************")
                print ("             TERMS OF THIS LIBRARY                     ")
                print ("*******************************************************")
                print ("This library has meant for no abuse like adding bad books or the books which have no or wrong information about the topic of the book..")
                print ("We are not responsible if there is any abuse from the user's side . ")
                print ("We will keep us and you responsible and aware ")
                print ("Thank you for having a look on our terms ")
                speak ("This library has meant for no abuse like adding bad books or the books which have no or wrong information about the topic of the book..")
                speak ("We are not responsible if there is any abuse from the user's side . ")
                speak ("We will keep us and you responsible and aware ")
                speak ("Thank you for having a look on our terms ")
                print ("********************************************************")
                user_points = user_points+5
                # increasing 5 points
                print ("You have now",user_points,"points")
                # printing the total points of the user 

    else :
        # if the user entered wrong choice other than 1 to 6 
        # printing statements
        print ("wrong library ID . Try again with making a new library ID ")
        speak ("wrong library ID . Try again with making a new library ID ")
        user_points = user_points+5
        # increasing 5 points
        print ("You have now",user_points,"points")
        # printing the total points of the user
except Exception as e:
    # Exception Handling 
    user_points = user_points+5
    # printing the total points of the user
    print ("You have now",user_points,"points")
    print (e)
    print()
    # printing statements
    print ('Some error has occured')
    speak ('Some error has occured')
    print ("Please try again")
    speak ("Please try again")
    
'''                   End of the program                              '''
'''                  Thank you for visiting the program               '''
# program created by Sayam Maity 
# Dated 7/4/2021




