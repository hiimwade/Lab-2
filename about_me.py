"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        'name': 'Wade Manley',
        'student id': 65160657,
        'pizza toppings': [
            'SAUSAGE',
            'PEPPERONI',
            'BACON'
       
        ],
       
       
        # TODO: Put full name into data structure
        # TODO: Put student ID into data structure
        # TODO: Put list of 3 pizza toppings into data structure
        'movies': [
            # TODO: Change this to a movie you like
            {
                'title': 'law abiding citizen',
                'genre': 'drama'
            },

            {
                'title': 'underworld',
                'genre': 'action'
            },
            # TODO: Add one more movie
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)
    print(f"My name is {about_me['name']}, but you can call me Sir {about_me['name'].split()[0]}")
    print (f"My student ID is {about_me['student id']}")

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)
    for pizza_toppings in about_me['pizza toppings']:
        print(f"My favourite pizza toppings are:*{pizza_toppings}")

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['peppers', 'onions'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'saw', 'horror')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)
    print(about_me['genre'], end=', ')

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])
    print(about_me['title'], end=', ')

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    # Print sentence containing name
    # Print sentence containing student ID
    print(f"My name is {my_info['name']}, but you can call me Sir {my_info['name'].split()[0]}")
    print (f"My student ID is {my_info['student id']}")


def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    for pizza_toppings in my_info['pizza toppings']:
        print(f"My favourite pizza toppings are:*{pizza_toppings}")
    # Print header "My favourite pizza toppings are:"
    # Print bullet list of favourite pizza toppings
    print()

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5
    # Append new pizza toppings to end of list 
    my_info['pizza toppings'].extend(['peppers','onions'])
    # Convert all pizza toppings to lowercase
    for i, toppings in enumerate(my_info['pizza toppings']):
        my_info['pizza toppings'][i] = toppings.lower()

    # Sort toppings list alphabetically
    my_info['pizza toppings'].sort()
    return

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    my_info['movies'].append({title, genre})
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    return

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """

    # TODO: Complete function body per Step 7
    print(f"I like to watch {my_info['genre']}, {my_info['genre']},{my_info['genre']} movies ")


def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    print(f"I like to watch {movie_list['title']}, {movie_list['title']},{movie_list['title']} movies ")

if __name__ == '__main__':
    main()