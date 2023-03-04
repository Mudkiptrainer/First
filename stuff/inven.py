snacks = {'ChocoRamo': [2.00, 5], 'Hersheys': [1.50, 6], 'Snickers': [1.50, 2], 'Twix': [1.75, 4], 'Crunch': [2.20, 7], 'Jr,Double,Tripple Whopper':[6.50, 10], 'Choco Break':[1.6, 6], 'Chocolate milk':[3.20,4]}
money = float(input("morning homie, how much cash you got?"))
print(money)
for i in snacks:
    if money < snacks[i][0]:
        print("you dont have enough for", i)
    else:
        print("you can buy a", i)
