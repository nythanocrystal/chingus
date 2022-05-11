#Welcome to life
import requests
request = requests.get('http://api.open-notify.org')
print(request.text)
print("Hello")
def bagels():
    bagel = input("Would you like bagels?").lower()
    if bagel == "yes":
        print("BAGELS!!!!")
    elif bagel == "no":
        print(":(")
    else:
        print("what?")

bagels()
yee = "Bingus"

for i in range(4):
    yee += "!"
    print(yee)