CURRENT_YEAR = 2026
MINIMUM_AGE = 18

def voters_details():
    voter = {}
    voter["name"]=input("Enter Voter's Full Name: ")
    voter["age"]=int(input("Enter Voter's Age: "))
    voter["birth_year"]=int(input("Enter Voter's Year Of Birth: "))
    voter["id_number"]=input("Enter Voter's National Id Number: ")
    return voter
def voter_validtion(voter):
    if not voter["name"]:
        return False, "Namer Cannot Be Empty! "
    if not voter["id_number"]:
        return False, "ID Number Cannot Be Empty! "
    if voter["age"]<=0 or voter ["age"]>125:
        return False, "Enter a Valid Age! "
    if voter["birth_year"]<=0 or voter["birth_year"]>CURRENT_YEAR:
        return False, "Invalid Year Of Birth! "
    calc_age=CURRENT_YEAR-voter["birth_year"]
    if voter["age"] not in (calc_age, calc_age-1):
        return False, "Age and Year Of Birth Do Not Match! "
    if voter["age"]<MINIMUM_AGE:
        return False, "Voter Must Be 18 Years Or Older!"
    return True, "Voter Registration Success!!"
def voter_display(voter):
    print("__---VOTER DETAILS---__")
    print(f"Full Name: {voter['name']}")
    print(f"Age: {voter['age']}")
    print(f"Year Of Birth: {voter['birth_year']}")
    print(f"ID Number: {voter['id_number']}")
def main():
    print("WELCOME TO VOTER REGISTRATION SYSTEM ")
    try:
        voter = voters_details()
        eligible, message = voter_validtion(voter)
        print(f"\n{message}")
        if eligible:
            voter_display(voter)
    except ValueError:
        print("Invalid input. Enter numbers for age and year of birth.  ")
main()