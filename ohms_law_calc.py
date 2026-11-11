def calc():
    while True:
        print("=========================================")
        print("⚡ OHM'S LAW & CIRCUIT SOLVER ⚡")
        print("=========================================")
        print("Choose the variable you want to find:")
        print("V = Voltage (Volts)")
        print("I = Current (Amps)")
        print("R = Resistance (Ohms)")
        print("=========================================")

        choice = input("").upper()
        if choice=="V":
            while True:
                try:
                    current=float(input("Enter current in Amps(precision of 0.00): "))
                    resistance=float(input("Enter resistance in Ohms(precision of 0.00): "))
                    print(f"Calculated Voltage: {(current*resistance):.2f}")
                    break
                except ValueError:
                    print("Please type a number.")
        elif choice=="I":
            while True:
                try:
                    voltage=float(input("Enter voltage in Volts(precision of 0.00): "))
                    resistance=float(input("Enter resistance in Ohms(precision of 0.00): "))
                    print(f"Calculated Current: {(voltage/resistance):.2f}")
                    break
                except ValueError:
                    print("Please type a number.")
        elif choice=="R":
            while True:
                try:
                    voltage=float(input("Enter voltage in Volts(precision of 0.00): "))
                    current=float(input("Enter current in Amps(precision of 0.00): "))
                    print(f"Calculated Resistance: {(voltage/current):.2f}")
                    break
                except ValueError:
                    print("Please type a number.")
        else:
            print("Invalid choice. Please select V, I, or R.")
if __name__ == "__main__":
    calc()
