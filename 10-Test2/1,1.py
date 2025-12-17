def f(player1, player2):
    sum1 = 0
    sum2 = 0
    for i in player1:
        if i in ('AKQJT'):
            sum1 += 10
        else:
            card_number = int(i)
            sum1 += card_number

    for i in player2:
        if i in ('AKQJT'):
            sum2 += 10
        else:
            card_number = int(i)
            sum2 += card_number
            
    if  sum1 >= sum2:
        return True
    else:
        return False
    

if __name__ == "__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))