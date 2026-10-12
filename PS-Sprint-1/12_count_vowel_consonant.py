def count_v_c(string):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0

    for char in string:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return  v_count, c_count

try:
    string = input("Enter a string : ")
    vowel, consonant = count_v_c(string)
    print(f"Numbers of vowel : {vowel}")
    print(f"Numbers of consonant : {consonant}")
except Exception as e:
    print(f"An error occurred. {e}")