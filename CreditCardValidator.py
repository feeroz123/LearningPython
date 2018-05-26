# Validate if the entered Credit Card number is valid based on Luhn's Algorithm.

#Say we have 38520000023237 and we want to check if it could be a real credit card number

#Take the last digit 7. This is our check digit
#Take the rest of the sequence 3852000002323
#Double every other digit starting from the right 6,8,10,2,0,0,0,0,0,2,6,2,6
#Sum the digits of the products 10 = 1 + 0 = 1
#Add all the digits together 6+8+1+2+0+0+0+0+0+2+6+2+6 = 33
#Multiply the result by 9 33 * 9 = 297
#Take the last digit of the result 7. If this matches the check digit we have a valid sequence
#Since our check digit 7 matches our result 7, we conclude that this sequence would be a valid credit card number!


# Issuer Identification Number (IIN)
##American Express: 34, 37
##Discover Card: 6011, 64, 65
##Mastercard: 2221 to 2720, 51 to 55
##Visa: 4
### Read more: Issuer Identification Number (IIN) https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp#ixzz5GcsKYZmL


# Some examples of VALID card numbers
##  Visa
### 4916525244697752
### 4532857518460433
### 4556567022681488
### 4716925167591283
### 4539149620158748

##  Mastercard
### 5210862957022039
### 5148518132778468
### 5109362255758222
### 5135724920606599
### 5490343858073992


def get_card_number():
    while True:
        crd_number = input("\n Enter the 16 digit Credit Card Number: ")

        try:
            if type(int(crd_number)) != int:
                print(" Invalid Input. Enter Only card number")
                continue
            else:
                return crd_number
                break
        except ValueError:
            print(" Invalid Input. Enter Only card number")
            continue


def get_card_issuer(card_number):
    ae = ['34', '37']        # American Express
    dc = ['6011', '64', '65']  # Discovery Card
    v = '4'               # Visa
    mc = [[2221, 2720], [51, 55]]  # Mastercard => Range 2221 to 2720, Range 51 to 55

    # Take out first 2 and first 4 digits of the card
    first_two = card_number[0:2]
    ''.join(first_two)
    first_four = card_number[0:4]
    ''.join(first_four)

    if card_number[0] == v:
        return "Visa"
    elif first_two in ae:
        return "American Express"
    elif first_two in dc or first_four in dc:
        return "Discovery Card"
    elif int(first_two) in range(mc[1][0], mc[1][1]+1) or int(first_four) in range(mc[0][0], mc[0][1]+1):
        return "Mastercard"
    else:
        return "Unknown"

def validate_card(card_number):
    # Check if card number is less than 16 digits
    while len(card_number) != 16:
        print("Invalid Card Number. Try again.")
        card_number = get_card_number()
    else:
        # Create list of digits in card number
        card_digits = []
        for digit in card_number:
            card_digits.append(digit)
            card_digits = [int(i) for i in card_digits]

        # 16th digit of the card is taken out as the Check Digit
        check_digit = card_digits.pop()

        # Starting with the first digit, multiply every second digit by 2
        for i in range(0, len(card_digits), 2):
            card_digits[i] = card_digits[i]*2

            # Every time you have a two-digit number, just add those digits together for a one-digit result
            if 10 - card_digits[i] <= 0:
                sum_digits = 0
                for digit in str(card_digits[i]):
                    sum_digits += int(digit)
                card_digits[i] = sum_digits

        # Sum of all digits
        sum_card_digits = sum(card_digits)

        # Final Check => If (Sum of all digits * 9)%10 = Check Digit, it is a VALID CARD. Else INVALID CARD
        if (sum_card_digits*9) % 10 == check_digit:
            print(" *** VALID CARD ***")
        else:
            print(" *** INVALID CARD ***")


print("\nCREDIT CARD NUMBER VALIDATOR")
card_number = get_card_number()
print(" Issuer = ", get_card_issuer(card_number))
validate_card(card_number)
print("\nCard Validation completed.")


# Some examples of VALID card numbers
##  Visa
### 4916525244697752
### 4532857518460433
### 4556567022681488
### 4716925167591283
### 4539149620158748
##  Mastercard
### 5210862957022039
### 5148518132778468
### 5109362255758222
### 5135724920606599
### 5490343858073992