car = {'make': 'Hyundai', 'model': 'grandi10', 'year': 2015}

try:
    result = car['color']
except:
    print("Error Occurred.")
else:
    print(result)
finally:
    print("All done.")

