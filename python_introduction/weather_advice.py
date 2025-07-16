
input("What's the weather like today? (sunny/rainy/cold): ")

# if weather == "sunny":
#     print("Wear a t-shirt and sunglasses.")
# elif weather == "rainy":
#     print("Don't forget your umbrella and raincoat.")
# elif weather == "cold":
#     print("Make sure to wear a warm coat and scarf.")
# else:
#     print("Sorry, I don't have recommendations for this weather.")

# # File: validate_weather_prompt.py

def validate_prompt(file_path):
    required_prompt = 'input("What\'s the weather like today? (sunny/rainy/cold): ")'
    
    try:
        with open(file_path, 'r') as f:
            code = f.read()
            if required_prompt in code:
                print("✅ Your script includes the correct input prompt.")
            else:
                print("❌ The input prompt is missing or incorrectly formatted.")
    except FileNotFoundError:
        print("⚠️ File not found. Make sure the path is correct.")

# Replace the path below if needed
validate_prompt("D:/Users/Kho/Desktop/ALX/Back End/Week 4/alx_be_python/control-flow/weather_advice.py")