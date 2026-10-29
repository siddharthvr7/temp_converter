def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("=== Temperature Converter (Version 2.0) ===")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C is equal to {celsius_to_fahrenheit(c)}°F")
    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F is equal to {fahrenheit_to_celsius(f)}°C")
    else:
        print("Invalid Choice.")

if __name__ == "__main__":
    main()
