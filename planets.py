def weight_on_planets():
    #I used a basic input function and then converted into a float on the same line to be concise.
    weight = float(input("What do you weigh on earth? "))
    #These are the formulas to calculate the weight on other planets
    mars = weight*0.38
    jupiter = weight*2.34

    #Prints out results
    print("\nOn Mars you would weigh", mars, "pounds.\nOn Jupiter you would weigh", jupiter, "pounds.")

    if __name__ == '__main__':
        weight_on_planets()