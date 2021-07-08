def main():
    # Ask for the user's weight in pounds.
    weight = int(input('Please enter your weight in pounds: '))

    # Ask for the user's height in inches.
    height = int(input('Please enter your height in inches: '))

    # Calculate the BMI (BMI = weight*703/height^2)
    BMI = weight * 703.0 / height**2
    print ('Your BMI is %.1f'%BMI)

    # Determine whether the user is underweight, overweight, or optimal
    if BMI < 18.5:
        print('You are underweight.')
    elif BMI > 25:
        print('It would appear that you are overweight.')
    else:
        print('You are at an optimal weight.')

# Call the main function.
main()
