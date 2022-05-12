#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 11th, 2022.
# This program asks the user to enter a two numbers and the operation they'd
# like to perform. After asking, it completes the calculation if the responses
# are valid & displays it to the user.


def format_address(full_name, question, street_num, name_street, city,
                  province, postal_code, apt_num = None):
    # formats strings
    capital_adress = full_name.upper() + "\n" + street_num + " " \
                     + name_street.upper() + "\n" + city.upper() \
                     + " " + province.upper() + " " + postal_code.upper()
    
    # hanldes the case if user lives in an apartment
    if question == "y":
        Capital_adress = full_name.upper() + "\n" + apt_num \
        + "-" + street_num + " " + name_street.upper() \
        + "\n" + city.upper() + " " + province.upper() \
        + " " + postal_code.upper()
        return Capital_adress
    # copies to main function
    return capital_adress



def main():
    apt_num_user = None
    
    # opening message
    print("This program formats an address to a Canadian mailing address.")
    print("")
    
    # get user input
    user_name = input("Enter your full name: ")
    question_apt = input("Do you live in an apartment (y/n): ")
    
    # checks if user lives in an apartment
    if question_apt == "y":
        apt_num_user = input("Enter your apartment number: ")
        
        # get more user input
        user_num_street = input("Enter your street number: ")
        user_street_name = input("Enter you street name AND "
                            "type (Main St., Flower Cres., etc): ")
       
        user_city= input("Enter your city: ")
        user_province = input("Enter your province (as an abbreviation,"
                            " i.e ON, AB, etc): ")
        user_postal = input("Enter your postal code (A1B 2C3): ")
        
        # assigns variable to funcition calll
        if apt_num_user !=None:
            address = format_address(user_name, question_apt, user_num_street, 
                                    user_street_name, user_city, user_province,
                                    user_postal, apt_num_user)
        else:
            address = format_address(user_name, question_apt, user_num_street, 
                                     user_street_name, user_city, 
                                     user_province, 
                                     user_postal)
        print("")
        print("Your Canadian mailing address is: \n")
        print(address)


if __name__ == "__main__":
    main()