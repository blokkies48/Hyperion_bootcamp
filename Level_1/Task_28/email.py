#An Email Simulation
class Email(): # Creating the Email class


    def __init__(self, from_address, email_content, to_address): # When creating the email object the sender's email and content should be passed. 
        # First to variables set to false
        self.has_been_read = False 
        self.is_spam = False
        self.from_address = from_address
        self.email_content = email_content
        self.to_address = to_address # Added another variable because emails have send and received addresses

    def mark_as_read(self): # Setting read variable as true
        self.has_been_read = True

    def mark_as_spam(self): # Setting spam as true
        self.is_spam = True
    

class Inbox(): # Creating another class for the inbox it just makes more sense to do this because email is already an object of its own and inbox is a object of emails
    
    def __init__(self):
        self.inbox = [] # Setting the list where the email objects will be saved in

    def add_email(self, email): # Simply appends new email object to the list
        return self.inbox.append(email)
    
    def get_count(self): # Returns the length of the list of objects
        return len(self.inbox)

    def get_email(self, index): # Gets the email at the position in the list
        return self.inbox[index - 1] # Index gotten by subtracting one form the position passed

    # Creates a list of the unread emails and returns said list
    def get_unread_email(self):
        unread_email = []
        for email in self.inbox:
            if email.has_been_read == False:
                unread_email.append(email)
        return unread_email

    # Creates a list of the spam emails and returns said list
    def get_spam_email(self):
        spam_email = []
        for email in self.inbox:
            if email.is_spam == True:
                spam_email.append(email)
        return spam_email
    
    # Pop used to remove email at position
    def delete(self, index):
        self.inbox.pop(index - 1)
        return self.inbox



def user_choice(inbox): # Needs a inbox object to work with
    
    while True:
        user_choice = input("What would you like to do - read/mark spam/send/delete/unread/quit?\n:").lower() # Make sure user input is all lower
        
        try: # Incase of index out of range 
            if user_choice == "read":
                print(f"You have {len(inbox.inbox)} emails.\nSelect one you would like to read?") # Printing the the amount of emails are available
                user_choice_e = int(input("Please select a email in the range: "))
                # Printing the info on separate lines
                print(f"From: {inbox.get_email(user_choice_e).from_address}")
                print(f"Content: {inbox.get_email(user_choice_e).email_content}")
                inbox.get_email(user_choice_e).mark_as_read() # Marking the chosen email as read
            
            elif user_choice == "mark spam":
                print(f"You have {len(inbox.inbox)} emails.")
                print(f"You have {len(inbox.get_spam_email())} spam emails.\nSelect one you would like to mark as spam?")
                
                while True:
                    user_choice_e = int(input("Please select an email in the range or -1 to cancel: "))
                    if user_choice_e == -1: # This has to be checked first so last item in the list isn't checked
                        break
                    elif inbox.inbox[user_choice_e] in inbox.get_spam_email(): # Checks if email is already marked as spam
                        print("This email is already marked as spam. Try another one")
                    else:
                        inbox.inbox[user_choice_e].mark_as_spam()
                        second_choice = input("Do you want to add another email as spam? (y/n): ")
                        if second_choice == "y":
                            pass # Goes back to the top
                        else:
                            break # Breaks out of loop
                print(f"You have {len(inbox.get_spam_email())} spam emails.") # Display changes to user after modification
            
            # If the user chooses send a new email will be created
            elif user_choice == "send":
                # The user is asked to enter the 3 required variables
                # Simple check done to see if it is an email entered. You can improve this by using regex and defining an expression to look for but I believe this is out of the scope of this task
                while True: 
                    from_email = input("Please enter your email: ")
                    to_email = input("Please enter the email you want to send to: ")
                    if "@" in from_email and "@" in to_email:
                        break
                    else:
                        print("Please enter a valid email")
                content = input("Please enter you message here.\n")
                new_send_email = Email(from_email,content,to_email) # A new instance of the email class is created and the user inputs are passed to the class
                inbox.add_email(new_send_email) # Adding the new email to the list of emails in inbox

            elif user_choice == "delete": # Not sure if I had to add these feature as well but the functions was created so might as well
                print(f"You have {len(inbox.inbox)} emails.\nSelect one you would like to delete?") # Printing the the amount of emails are available
                user_choice_e = int(input("Please select a email in the range: "))
                # Printing the info on separate lines
                inbox.delete(user_choice_e)
                print(f"You have {len(inbox.inbox)} emails.") # Show changes

            elif user_choice == "unread":
                if len(inbox.get_unread_email()) != 0: # Check if there are any unread emails
                    print(f"You have {len(inbox.get_unread_email())} unread emails.\nSelect one you would like to read?") # Printing the the amount of emails are available
                    user_choice_e = int(input("Please select a email in the range: ")) -1 # Subtracting 1 to get the correct index
                    # Printing the info on separate lines
                    print(f"From: {inbox.get_unread_email()[user_choice_e].from_address}")
                    print(f"Content: {inbox.get_unread_email()[user_choice_e].email_content}")
                    inbox.get_unread_email()[user_choice_e].mark_as_read() # Marking the chosen email as read
                else:
                    print("You have no unread emails")
            # Code that came with template
            elif user_choice == "quit":
                print("Goodbye")
                break
            
            else:
                print("Oops - incorrect input")

        # Catching the error
        except IndexError:
            print("Your choice was out of range select an option again")

# Defining main function only the code in the main method is ran
def main():
    # Creating a new instance of the Inbox class
    inbox = Inbox()
    
    # Creating a bunch of emails just for testing the and for the reviewer to play around with
    email1 = Email("test_email_1@abc.com", "Hope this email finds you well 1", "receiver_1@123.com")
    email2 = Email("test_email_2@abc.com", "Hope this email finds you well 2", "receiver_2@123.com")
    email3 = Email("test_email_3@abc.com", "Hope this email finds you well 3", "receiver_3@123.com")
    email4 = Email("test_email_4@abc.com", "Hope this email finds you well 4", "receiver_4@123.com")
    email5 = Email("test_email_5@abc.com", "Hope this email finds you well 5", "receiver_5@123.com")

    # Setting two emails to read and to spam for testing 
    email2.mark_as_read()
    email3.mark_as_spam()
    
    # Adding created emails to the email inbox instance
    inbox.add_email(email1)
    inbox.add_email(email2)
    inbox.add_email(email3)
    inbox.add_email(email4)
    inbox.add_email(email5)

    # Calling on the user_choice function and passing the inbox object to it
    user_choice(inbox)


# This shows this file is a script and it is only running the main method
if __name__ == '__main__':
    main()

