def calculation_pi(number) :
    numerator = 4.0
    denominator = 1.0
    operation = 1.0
    pi = 0.0
    for _ in range(number):
        pi += operation *(numerator/denominator)
        denominator +=2
        operation *= -1
    
    return pi

if __name__ == "__main__":
  print(calculation_pi(1000000))