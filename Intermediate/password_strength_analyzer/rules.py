import helper as hel
def rules():
    print(f"\n{"-"*32} Rules {"-"*32}")
    print("1. Length: ")
    print(f"   {"If length has less then 8 characters":<60} :score 0")
    print(f"   {"If length has 8 or more characters  but less then 12":<60} :score 1")
    print(f"   {"If length has more then 8 characters":<60} :score 2")

    print("\n2. Uppercase Character: ")
    print(f"   {"No uppercase characters in the password":<60} :score 0")
    print(f"   {"Atleast 1 uppercase character in the password":<60} :score 2")

    print("\n3. Lowercase Character: ")
    print(f"   {"No lowercase characters in the password":<60} :score 0")
    print(f"   {"Atleast 1 lowercase character in the password":<60} :score 1")

    print("\n4. Digits: ")
    print(f"   {"No digit in the password":<60} :score 0")
    print(f"   {"Atleast 1 digit in the password":<60} :score 1")

    print("\n5. Special Character: ")
    print(f"   {"No special characters in the password":<60} :score 0")
    print(f"   {"Atleast 1 special character in the password":<60} :score 2")

    print("\n6. Common Passwords: ")
    x = ", ".join(hel.common_pass_examples)
    print(f"   List of common passwords: {x}")
    # for p in hel.common_pass_examples:
    #     print("   "+p)
    print(f"   {"If password appears in given list":<60} :score 0")
    print(f"   {"If password dont appear in the list":<60} :score 1")



if __name__ == "__main__":
    rules()
