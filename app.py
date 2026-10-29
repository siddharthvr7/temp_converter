def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("=== Temperature Converter (Version 1.0) ===")
    print("1. Convert Celsius to Fahrenheit")
    choice = input("Enter choice (1): ")
    
    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C is equal to {celsius_to_fahrenheit(c)}°F")
    else:
        print("Invalid Choice.")

if __name__ == "__main__":
    main()
