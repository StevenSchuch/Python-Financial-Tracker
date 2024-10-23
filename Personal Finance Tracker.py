"""
Programmer: Steven Schuch
Purpose: Create a user interactive program that calculates personal finance.
Date: 10/16/2024
Version: 1.0
"""

def housing_expenses():
    housing_data = {"Rent": float(input("Enter monthly rent: ")),
                    "Mortgage": float(input("Enter monthly mortgage: ")),
                    "Property Tax": float(input("Enter property tax: ")),
                    "Property Insurance": float(input("Enter property insurance: "))}

    return housing_data
def housing_calculations(housing_data):
    total_housing = 0
    total_housing += housing_data["Rent"]
    total_housing += housing_data["Mortgage"]
    total_housing += housing_data["Property Tax"]
    total_housing += housing_data["Property Insurance"]
    return total_housing

def utility_expenses():
    utility_data = {"Electricity": float(input("Enter electricity utility: ")),
                    "Gas": float(input("Enter gas utility: ")),
                    "Water": float(input("Enter water utility: ")),
                    "Internet/Cable": float(input("Enter internet utility: ")),
                    "General Waste": float(input("Enter general waste utility: ")),
                    "Other": float(input("Enter other utility: "))}
    return utility_data

def utility_calculations(utility_data):
    total_utility = 0
    total_utility += utility_data["Electricity"]
    total_utility += utility_data["Gas"]
    total_utility += utility_data["Water"]
    total_utility += utility_data["Internet/Cable"]
    total_utility += utility_data["General Waste"]
    total_utility += utility_data["other"]
    return total_utility

def transportation_expenses():
    transportation_data = {"Car Payment": float(input("Enter Car Payment: ")),
                           "Fuel": float(input("Enter fuel utility: ")),
                           "Car insurance": float(input("Enter car insurance: ")),
                           "Public Transportation": float(input("Enter public transport utility: ")),
                           "Parking Fees": float(input("Enter parking fees: ")),
                           "Vehicle Maintenance": float(input("Enter vehicle maintenance: "))}

def transportation_calculations(transportation_data):
    total_transportation = 0
    total_transportation += transportation_data["Car Payment"]
    total_transportation += transportation_data["Fuel"]
    total_transportation += transportation_data["Car insurance"]
    total_transportation += transportation_data["Public Transportation"]
    total_transportation += transportation_data["Parking Fees"]
    total_transportation += transportation_data["Vehicle Maintenance"]
    return total_transportation

def food_expenses():
    food_data = {"Groceries": float(input("Enter groceries: ")),
                 "Dinning out": float(input("Enter dinning out: ")),
                 "Coffee/Snack": float(input("Enter coffee and snack: ")),
                 "Meal Delivery": float(input("Enter meal delivery: ")),}

def food_calculations(food_data):
    total_food = 0
    total_food += food_data["Groceries"]
    total_food += food_data["Dinning out"]
    total_food += food_data["Coffee/Snack"]
    total_food += food_data["Meal Delivery"]
    return total_food

def medical_expenses():
    medical_data = {"Health Insurance": float(input("Enter health insurance: ")),
                    "Medications": float(input("Enter medications: ")),
                    "Doctor Visits": float(input("Enter doctor visits: ")),
                    "Vision Care": float(input("Enter vision care: ")),
                    "Other": float(input("Enter other: "))}
    return medical_data

def medical_calculations(medical_data):
    total_medical = 0
    total_medical += medical_data["Health Insurance"]
    total_medical += medical_data["Medications"]
    total_medical += medical_data["Doctor Visits"]
    total_medical += medical_data["Vision Care"]
    total_medical += medical_data["Other"]
    return total_medical

def debt_expenses():
    debt_data = {"Student loans": float(input("Enter student loans: ")),
                 "Credit cards": float(input("Enter credit cards: ")),
                 "Personal Loans": float(input("Enter personal loans: ")),
                 "Device Debt": float(input("Enter device debt: ")),
                 "other": float(input("Enter other: "))}
    return debt_data

def debt_calculations(debt_data):
    total_debt = 0
    total_debt += debt_data["Student loans"]
    total_debt += debt_data["Credit cards"]
    total_debt += debt_data["Personal Loans"]
    total_debt += debt_data["Device Debt"]
    total_debt += debt_data["other"]
    return total_debt

def personal_expenses():
    personal_data = {"Clothing": float(input("Enter clothing: ")),
                     "Haircut": float(input("Enter haircut: ")),
                     "Self Care": float(input("Enter self care: ")),
                     "Gym": float(input("Enter gym: ")),
                     "Subscriptions": float(input("Enter subscriptions: "))}
    return personal_data
def personal_calculations(personal_data):
    total_personal = 0
    total_personal += personal_data["Clothing"]
    total_personal += personal_data["Haircut"]
    total_personal += personal_data["Self Care"]
    total_personal += personal_data["Gym"]
    total_personal += personal_data["Subscriptions"]
    return total_personal

def family_expenses():
    family_data = {"Childcare": float(input("Enter child care: ")),
                   "School Supplies": float(input("Enter school supplies: ")),
                   "Extracurricular Activities": float(input("Enter extracurricular activities: ")),
                   "Allowance": float(input("Enter allowance: ")),
                   "Child Support": float(input("Enter child support: "))}
    return family_data

def family_calculations(family_data):
    total_family = 0
    total_family += family_data["Childcare"]
    total_family += family_data["School Supplies"]
    total_family += family_data["Extracurricular Activities"]
    total_family += family_data["Allowance"]
    total_family += family_data["Child Support"]
    return total_family

def animals_expenses():
    animals_data = {"Pet food": float(input("Enter pet food: ")),
                    "Vet Bills": float(input("Enter vet bills: ")),
                    "Grooming": float(input("Enter grooming: ")),
                    "Toys": float(input("Enter toys: ")),}
    return animals_data

def animals_calculations(animals_data):
    total_animals = 0
    total_animals += animals_data["Pet food"]
    total_animals += animals_data["Vet Bills"]
    total_animals += animals_data["Grooming"]
    total_animals += animals_data["Toys"]
    return total_animals

def entertainment_expenses():
    entertain_data = {"Streaming services": float(input("Enter streaming services: ")),
                      "Hobbies": float(input("Enter hobbies: ")),
                      "Travel Savings": float(input("Enter travel savings: ")),
                      "Movies/Concerts": float(input("Enter movies/concerts: ")),}
    return entertain_data

def entertainment_calculations(entertain_data):
    total_entertain = 0
    total_entertain += entertain_data["Streaming services"]
    total_entertain += entertain_data["Hobbies"]
    total_entertain += entertain_data["Travel Savings"]
    total_entertain += entertain_data["Movies/Concerts"]
    return total_entertain

def savings_expenses():
    savings_data = {"Emergency Funds": float(input("Enter emergency funds: ")),
                    "Retirement Contribution": float(input("Enter retirement contribution: ")),
                    "Stock Investments": float(input("Enter stock investments: ")),
                    "Major Purchase Savings": float(input("Enter major purchase savings: ")),
                    "College Savings": float(input("Enter college savings: ")),}
    return savings_data

def savings_calculations(savings_data):
    total_savings = 0
    total_savings += savings_data["Emergency Funds"]
    total_savings += savings_data["Retirement Contribution"]
    total_savings += savings_data["Stock Investments"]
    total_savings += savings_data["Major Purchase Savings"]
    total_savings += savings_data["College Savings"]
    return total_savings

def personal_finance():
    print("Welcome to the personal finance tracker!")
    print("Please answer the following questions:")




