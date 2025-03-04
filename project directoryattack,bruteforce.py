import itertools
import string

# Hardcoded password
CORRECT_PASSWORD = "Tiger"  # Change this as needed

# Function for Dictionary Attack
def dictionary_attack(dictionary_file):
    try:
        with open(dictionary_file, "r") as file:
            for word in file:
                word = word.strip()
                if word == CORRECT_PASSWORD:
                    return f"[SUCCESS] Dictionary Attack: Password found! -> {word}"
        return "[FAILED] Dictionary Attack: Password not found in dictionary."
    except FileNotFoundError:
        return "[ERROR] Dictionary file not found!"

# Function for Brute Force Attack
def brute_force_attack():
    chars = string.ascii_letters  # A-Z, a-z
    for combination in itertools.product(chars, repeat=5):
        guess = "".join(combination)
        if guess == CORRECT_PASSWORD:
            return f"[SUCCESS] Brute Force Attack: Password cracked! -> {guess}"
    return "[FAILED] Brute Force Attack: Exhausted all possibilities."

# Command-line execution
def main():
    dict_result = dictionary_attack("dictionary.txt")
    print(dict_result)

    # Always run brute force attack, regardless of dictionary attack result
    print("[INFO] Starting Brute Force Attack...")
    brute_result = brute_force_attack()
    print(brute_result)

if __name__ == "__main__":
    main()
