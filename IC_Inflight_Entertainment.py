"""
You've built an inflight entertainment system with on-demand movie streaming.

Users on longer flights like to start a second movie right when their first one ends, but they complain that the plane
usually lands before they can see the ending. So you're building a feature for choosing two movies whose total run-times
will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and
returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:
* Assume your users will watch exactly two movies
* Don't make your users watch the same movie twice
* Optimize for runtime over memory
"""

def in_flight_movies(movies, flight_duration):

    # movies we've seen so far,
    movie_lengths = set()


    for first_movie in movies:
        second_movie = flight_duration - first_movie
        if second_movie in movies:
            print(f"length of first movie is: {first_movie}")
            print(f"length of second movie is: {second_movie}")
            return True


    # No movie found
    return False


current_movies = [70, 92, 78, 60, 180, 120]
current_flight_time = 180
ans =in_flight_movies(current_movies, current_flight_time)
print(ans)

"""
Bonus: 
1. What if we wanted something close to the flight length like 20 minutes?
2. What if we wanted to fill the flight lenth nicely as possible with an amount of movies
"""