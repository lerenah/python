def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    lengths = set()
    for current_length in movie_lengths:
        second_movie_length = flight_length - current_length
        if second_movie_length in lengths:
            return True
        else:
            lengths.add(current_length)

    return False
