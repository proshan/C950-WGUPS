import HashTable

if __name__ == '__main__':
    bestMovies = [
        [1, "CITIZEN KANE - 1941"],
        [2, "CASABLANCA - 1942"],
        [3, "THE GODFATHER - 1972"],
        [4, "GONE WITH THE WIND - 1939"],
        [5, "LAWRENCE OF ARABIA - 1962"],
        [6, "THE WIZARD OF OZ - 1939"],
        [7, "THE GRADUATE - 1967"],
        [8, "ON THE WATERFRONT- 1954"],
        [9, "SCHINDLER'S LIST -1993"],
        [10, "SINGIN' IN THE RAIN - 1952"],
        [11, "STAR WARS - 1977"]
    ]

    myHash = HashTable.Hash()

    print("\nInsert:")
    myHash.insert_hash(bestMovies[0][0], bestMovies[0][1])  # 2nd bucket; Key=1, item="CITIZEN KANE - 1941"
    print(myHash.main_table)

