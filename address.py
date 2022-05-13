#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 12th, 2022.
# This program asks the user several questions regarding their address. It then
# formats it and displays it to the user.


def format_address(full_name, question, street_num, name_street, city,
                   province, postal_code, apt_num=None):

    # formats strings & converts from lowercase to capital
    capital_adress = full_name.upper() + "\n" + street_num + " " \
                     + name_street.upper() + "\n" + city.upper() \
                     + " " + province.upper() + " " + postal_code.upper()

    # handles the case if user lives in an apartment
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

    user_city = input("Enter your city: ")
    user_province = input("Enter your province (as an abbreviation,"
                          " i.e ON, AB, etc): ")
    user_postal = input("Enter your postal code (A1B 2C3): ")

    # assigns a variable to function call,
    # giving it a returned value.
    if apt_num_user is not None:
        address = format_address(user_name, question_apt, user_num_street,
                                 user_street_name, user_city,
                                 user_province, user_postal, apt_num_user)

    else:
        address = format_address(user_name, question_apt, user_num_street,
                                 user_street_name, user_city,
                                 user_province, user_postal)
    print("")
    print("Your Canadian mailing address is: \n")
    print(address)


if __name__ == "__main__":
    main()
