def number_guesser():
    print("Welcome to the number guesser! Pick a number in your mind between 1 and 100, and I'll try to guess it!\n")
    
    ready = input("Are you ready (yes or no): ").strip().lower()
    if ready != 'yes':
        print("Okay, come back when you're ready!")
        return
    
    low, high = 1, 100
    while low <= high:
        guess = (low + high) // 2
        answer = input(f"\nIs it {guess} (yes or no): ").strip().lower()
        
        if answer == 'yes':
            print("\nI got it! Awesome! Thanks for playing!")
            break
        else:
            too_high_low = input("Was that too high or too low (too high or too low): ").strip().lower()
            if too_high_low == 'too high':
                high = guess - 1
            elif too_high_low == 'too low':
                low = guess + 1

number_guesser()
