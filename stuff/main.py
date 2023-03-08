import inven

def select_item():
    
    encoreunefois = 'yes'
    while encoreunefois != 'no':
        item = input('What item do you want?')
        price = inven.snacks[item][0]
        quantity = inven.snacks[item][1]
        print('there are', quantity, item, 'left. You will pay', price, 'for one', item, ', do you want to proceed?')
        seleccion = input('(yes/no)')
        if seleccion == 'no':
            print('ok')
            break
            
        else:
            print('enjoy your', item, '!')
            inven.snacks[item][1] -= 1
            encoreunefois = input('do you want to keep buying? (yes/no)')
            if encoreunefois == 'no':
                break
            else:
                encoreunefois = 'yes'
select_item()