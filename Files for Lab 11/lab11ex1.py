def bank_statement(transactions):
    """Returns a new list of three numbers: the first will be the sum of the
    deposits, the second (a negative number) will be the sum of the withdrawals,
    and the third will be the current account balance.
    
    
    >>>bank_statement([67.23,-43.32,133.875,-60.64])
    [201.11, -103.96, 97.14]
    
    """
    deposits=0
    withdrawals=0
    balance=0
    for i in transactions:
        if i < 0:
            withdrawals+=i
        if i > 0:
            deposits+=i
        balance+=i
    return [round(deposits,2),round(withdrawals,2),round(balance,2)]