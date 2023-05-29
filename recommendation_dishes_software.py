class Menu_Tool:

    def __init__(self, dishes_info):
        self.dishes_info = dishes_info
        #self.shoppingList = {}
        #self.weeklyMenu = {"Monday":[{"Lunch": " "}, {"Dinner": " "}], "Tuesday":[{"Lunch": " "}, {"Dinner": " "}], "Wednesday":[{"Lunch": " "}, {"Dinner": " "}], "Thursday":[{"Lunch": " "}, {"Dinner": " "}], "Friday":[{"Lunch": " "}, {"Dinner": " "}], "Saturday":[{"Lunch": " "}, {"Dinner": " "}], "Sunday":[{"Lunch": " "}, {"Dinner": " "}]}

    def add_newdish(self, country, dish):
        if country not in self.dishes_info:
            self.dishes_info[country] = {}
        self.dishes_info[country].append(dish)

    def removing_dish(self, country, dish):
        for i in range(len(self.dishes_info[country])):
            if dish.lower() == self.dishes_info[country][i]["NAME"].lower():
                self.dishes_info[country].pop(i)
                return
            print("Sorry there no receipe with this name!")

    def welcome(self):

        print("""
        --------------------------------------------------------------------------------
        Welcome to our program for recommending traditional dishes based on countries!
        --------------------------------------------------------------------------------
        """)

        print("""
        Discover traditional dishes from around the world with our program. You can search
        for a country by typing the first letter of its name, and the program will display 
        all available options starting with that letter. Once you select a country by typing
        its corresponding number, the program will show you a list of traditional dishes 
        from that location. For each dish, you can view information such as the ingredients,
        average preparation time, and common allergens.
        """)


        print("""
        --------------- 
        So let's start!
        ---------------
        """)
   
    def letter_user_choice(self):
        return input(str("\n* To view traditional dishes from a specific country, please enter the first letter of its name:")) 

    def countries_available(self):
        choice = self.letter_user_choice()
        countries = []
        count = 1

        for key in self.dishes_info.keys():
            
            if key.startswith(choice.upper()):
                countries.append(str(count) + "- " + key)
                count += 1 
                                
        if len(countries) == 0:
            one_more_time = self.one_more_time_f()
            if not one_more_time:
                print("Thank you for using our program, and we hope to see you again soon!")
                exit()
            else:
                return self.dishes_available_by_country()
            
               


        else:
            print(f"\n* We have the following countries available starting with the letter '{choice}': \n")
            for i in countries:
                print(i)

            return countries
    
    def dishes_available_by_country(self):
        self.welcome()
        countries = self.countries_available()
        country_choosed = (input("\n* Please choose a number corresponding to the country of your choice to view its traditional dishes: "))
        found_country = False

        for countrie in countries:
            if countrie[0] == str(country_choosed):
                found_country = True
                print(f"\n* You chose {countrie[3:]}, right? Here are the available options:\n")
                for dish in range(len(self.dishes_info[countrie[3:]])):
                    print(self.dishes_info[countrie[3:]][dish]["NAME"])
                    print("\nIngredients: " + str(self.dishes_info[countrie[3:]][dish]["Ingredients"]))
                    print("Time to prepare(min): " + str(self.dishes_info[countrie[3:]][dish]["Prep_time(min)"]))
                    print("Allergens: " + str(self.dishes_info[countrie[3:]][dish]["Allergens"]) + "\n\n")

                see_more = input(str("\nWould you like to see more dishes (y or n)?"))
                if see_more.lower() == "y":
                    return self.dishes_available_by_country() 
                elif see_more.lower() == "n":
                    print("\nBye bye! Hope to see you again soon!\n")
                    exit()
            

        if not found_country:
            while True:
                y_or_n = input("Sorry, we don't this option available. Would you like to try again? (Type 'y' for yes, 'n' for no): ")
                if y_or_n.lower() == "n":
                    print("Thank you for using our program, and we hope to see you again soon!")
                    break
                
                elif y_or_n.lower() == "y":
                    return self.dishes_available_by_country()
        
    def print_all_dishes(self):
        print("\nHere are all the available options in our system: ")
        for country in self.dishes_info:
            print("\n")
            print("------------------------------------------------------------------------")
            print(country)
            print("------------------------------------------------------------------------")
            
            for item in range(len(self.dishes_info[country])):
                print(self.dishes_info[country][item]["NAME"])
                print("\n")
                print("Ingredients: ", self.dishes_info[country][item]["Ingredients"])
                print("Prep_time(min): ", self.dishes_info[country][item]["Prep_time(min)"])
                print("Allergens: ", self.dishes_info[country][item]["Allergens"])
                print("\n")

    def weekly_menu(self):
        user_input_menu = input("\nWould you like to create a Menu with some of this dish? (y or n)\n")
        if user_input_menu == "n":
            print("See you next time!")
        elif user_input_menu == "y":
            for day in self.weeklyMenu:
                user_input_lunch = input(f"Type the number dish's correspondent number that you would like to add on the {day} in the lunch time: \n")
            for country in self.dishes:
                print("\n")
                print("------------------------------------------------------------------------")
                print(country)
                print("------------------------------------------------------------------------")
                print("\n")
                for item in range(len(self.dishes[country])):
                    print("Name: ", self.dishes[country][item]["NAME"])
                    print("\n")
                    print("Ingredients: ", self.dishes[country][item]["Ingredients"])
                    print("Prep_time(min): ", self.dishes[country][item]["Prep_time(min)"])
                    print("Allergens: ", self.dishes[country][item]["Allergens"])
                    print("\n")
      
    def shopping_list(self):
        user_input_shop = input("\nWould you like to generate a shopping list based on your weekly menu? (Type 'y' for yes, 'n' for no): \n")
        if user_input_shop == "y":
            pass

    def sorry_ending(self):
        print("\nSorry we don't have the option you're looking for. Thank you for using our program, and we hope to see you again soon!")

    def one_more_time_f(self):
        one_more_time = input("\nSorry, we don't have any countries available that start with that letter at the moment. Would you like to try again? (Type 'y' for yes, 'n' for no): ")
        return one_more_time.lower() == "y"

dict_dishes = {
    "Afghanistan": [
    {"NAME": "Sabzi Chalaw",
     "Ingredients": [["spinach", 200, "g"], ["rice", 200, "g"], ["onions", 100, "g"], ["garlic", 10, "g"], ["spices", "to taste"]],
     "Prep_time(min)": 45,
     "Allergens": []
    },
    {
    "NAME": "Qorma Lawand",
    "Ingredients": [["potatoes", 200, "g"], ["chickpeas", 200, "g"], ["tomatoes", 100, "g"], ["onions", 100, "g"], ["garlic", 10, "g"], ["spices", "to taste"]],
    "Prep_time(min)": 60,
    "Allergens": []
    },
    {
    "NAME": "Borani Banjan",
    "Ingredients": [["eggplant", 200, "g"], ["tomatoes", 100, "g"], ["onions", 100, "g"], ["garlic", 10, "g"], ["spices", "to taste"], ["vegan yogurt", 50, "g"]],
    "Prep_time(min)": 60,
    "Allergens": ["Dairy (if not using vegan yogurt)"]
    }
    ],


    "Argentina": [      
    {
    "NAME": "Empanadas",
    "Ingredients": [["pastry", 200, "g"], ["onions", 50, "g"], ["bell pepper", 50, "g"], ["tomatoes", 50, "g"], ["spinach", 50, "g"], ["spices", "to taste"]],
    "Prep_time(min)": 60,
    "Allergens": ["Gluten"]
    },
    {
    "NAME": "Locro",
    "Ingredients": [["pumpkin", 200, "g"], ["beans", 100, "g"], ["corn", 100, "g"], ["potatoes", 100, "g"], ["spices", "to taste"]],
    "Prep_time(min)": 90,
    "Allergens": []
    },
    {
    "NAME": "Humita",
    "Ingredients": [["corn", 200, "g"], ["onions", 50, "g"], ["spices", "to taste"]],
    "Prep_time(min)": 60,
    "Allergens": []
    }
    ],


    "Australia": [
    {
    "NAME": "Lentil Shepherd's Pie",            
    "Ingredients": [["lentils", 200, "g"], ["vegetables", 200, "g"], ["potatoes", 200, "g"], ["spices", "to taste"]],
    "Prep_time(min)": 90,
    "Allergens": []
    },
    {
    "NAME": "Damper",
    "Ingredients": [["flour", 200, "g"], ["water", 100, "ml"], ["yeast or baking powder (optional)", "to taste"]],
    "Prep_time(min)": 45,
    "Allergens": ["Gluten"]
    },
    {
    "NAME": "Vegemite and Avocado Sandwich",        
    "Ingredients": [["bread", 2, "slices"], ["Vegemite spread", 1, "tsp"], ["avocado", 1/4, "medium"], ["tomato", 2, "slices"], ["lettuce", 1, "leaf"], ["salt", 1/8, "tsp"], ["pepper", 1/8, "tsp"]],
    "Prep_time(min)": 5,
    "Allergens": ["Gluten"]
    }
    ],


    "Brazil": [
    {
    "NAME": "Vegan Feijoada", 
    "Ingredients": [["black beans", 200, "g"], ["onions", 200, "g"], ["garlic", 9, "g"], ["smooked paprika", 20, "g"], ["coriander", 50, "g"]], 
    "Prep_time(min)": 120, 
    "Allergens":[]
    },
    {
    "NAME": "Vegan Brigadeiro", 
    "Ingredients": [["cashew nuts", 200, "g"], ["cocoa Powder", 150, "g"], ["dark Brown Sugar", 100, "g"], ["water", 250, "ml"]], 
    "Prep_time(min)": 60, 
    "Allergens":["Cashew nuts"]
    },
    {
    "NAME": "Moqueca de Palmito",        
    "Ingredients": [["heart of palm", 400, "g"], ["onion", 1, "un"], ["bell pepper", 1, "un"], ["tomato", 2, "un"], ["garlic", 3, "un"], ["coconut milk", 200, "ml"], ["lime juice", 2, "tbsp"], ["olive oil", 2, "tbsp"], ["coriander", 1/4, "cup"], ["paprika", 1/2, "tsp"], ["cumin", 1/2, "tsp"], ["salt", 1/2, "tsp"], ["black pepper", 1/4, "tsp"]],
    "Prep_time(min)": 40,
    "Allergens": []
    },
    ],


    "Canada": [
    {
    "NAME": "Poutine",
    "Ingredients": [["french fries", 500, "g"], ["vegan cheese curds", 200, "g"], ["gravy", 200, "ml"]],
    "Prep_time(min)": 30,
    "Allergens": []
    },
    {
    "NAME": "Nanaimo Bars",
    "Ingredients": [["coconut", 100, "g"], ["vegan butter", 100, "g"], ["cocoa powder", 50, "g"], ["vegan graham cracker crumbs", 200, "g"], ["powdered sugar", 200, "g"]],
    "Prep_time(min)": 60,
    "Allergens": []
    },
    {
    "NAME": "Butter Tarts",
    "Ingredients": [["vegan butter", 150, "g"], ["brown sugar", 150, "g"], ["maple syrup", 100, "ml"], ["vanilla extract", 5, "ml"], ["pastry shells", 9]],
    "Prep_time(min)": 45,
    "Allergens": []
    }
    ],


    "China": [
    {
    "NAME": "Mapo Tofu",
    "Ingredients": [["tofu", 300, "g"], ["chili bean paste", 30, "g"], ["Sichuan peppercorns", 5, "g"], ["garlic", 3, "cloves"]],
    "Prep_time(min)": 40,
    "Allergens": []
    },
    {
    "NAME": "Buddhist Delight",
    "Ingredients": [["assorted vegetables", 500, "g"], ["tofu", 200, "g"], ["mushrooms", 100, "g"], ["soy sauce", 30, "ml"], ["sesame oil", 15, "ml"]],
    "Prep_time(min)": 25,
    "Allergens": []
    },
    {
    "NAME": "Hot and Sour Soup",
    "Ingredients": [["tofu", 150, "g"], ["mushrooms", 100, "g"], ["bamboo shoots", 100, "g"], ["black vinegar", 30, "ml"], ["white pepper powder", 5, "g"]],
    "Prep_time(min)": 30,
    "Allergens": []
    }
    ],


    "Colombia": [
    {
    "NAME": "Ajiaco",
    "Ingredients": [["potatoes", 500, "g"], ["corn", 200, "g"], ["avocado", 1], ["capers", 10, "g"], ["vegetable broth", 500, "ml"]],
    "Prep_time(min)": 60,
    "Allergens": []
    },
    {
    "NAME": "Empanadas de Pipián",
    "Ingredients": [["pumpkin seeds", 100, "g"], ["peanuts", 100, "g"], ["flour", 300, "g"], ["vegan butter", 100, "g"], ["water", 150, "ml"]],
    "Prep_time(min)": 50,
    "Allergens": []
    },
    {
    "NAME": "Arroz Atollado",
    "Ingredients": [["rice", 300, "g"], ["plantains", 200, "g"], ["soy protein", 150, "g"], ["vegetables", "assorted"], ["vegetable oil", 30, "ml"]],
    "Prep_time(min)": 45,
    "Allergens": []
    }
    ],


    "Italy": [
    {
    "NAME": "Pasta with Cashew Cream and Pesto", 
    "Ingredients": [["pasta(spaguetti)", 500, "g"], ["cashew nuts", 200, "g"], ["parsley", 100, "g"], ["oliva Oil", 20, "g"], ["cherry tomato", 100, "g"]], 
    "Prep_time(min)": 60, 
    "Allergens":["Cashew nuts", "Gluten"]
    },
    ],


    "India": [
    {
    "NAME": "Cabbage Muthya", 
    "Ingredients": [["cabbage", 500, "g"], ["chick pea flour", 250, "g"], ["corn semolina", 250, "g"], ["moustard seeds", 20, "g"], ["onions", 200, "g"], ["ginger", 40, "g"], ["coriander", 100, "g"], ["salt", 10, "g"], ["cider vinagre", 20, "ml"], ["sesame seed", 20, "g"]], 
    "Prep_time(min)": 120, 
    "Allergens":[]
    },
    {
    "NAME": "Chana Masala",
    "Ingredients": [["chickpeas", 2, "cups"], ["onions", 1, "large"], ["tomatoes", 2, "medium"], ["garlic", 4, "cloves"], ["spices", "to taste"]],
    "Prep_time(min)": 40,
    "Allergens": []
    },
    {
    "NAME": "Aloo Gobi",
    "Ingredients": [["potatoes", 2, "medium"], ["cauliflower", 1/2, "small"], ["onions", 1, "medium"], ["tomatoes", 2, "medium"], ["spices", "to taste"]],
    "Prep_time(min)": 30,
    "Allergens": []
    },
    ],
    
}                
    
new_dish =  {
    "NAME": "Nhocci", 
    "Ingredients": ["Pasta(spaguetti)", "Cashew Cream", "Parsley", "Oliva Oil", "Cherry Tomato"], 
    "Prep_time(min)": 60, 
    "Allergens":["Cashew nuts", "Gluten"]
    }

option_1 = Menu_Tool(dict_dishes)

#option_1.add_newdish("Italy", new_dish)

#option_1.removing_dish("India", "Chana Masala")

option_1.dishes_available_by_country()

#option_1.print_all_dishes()













