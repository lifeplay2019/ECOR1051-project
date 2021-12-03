def blackjack( a: int , b:int ) -> int:
if a > 21 and b > 21:
        return 0
elif a <= 21 and b <= 21:
        if a - b > 0:
            return a
        else:
            return b
elif a > 21:
        return b
else:
        return a