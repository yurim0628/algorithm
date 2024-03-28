def solution(enrollments, referrals, sellers, amounts):
    earnings = {}
    total_earnings = {}
    for enrollment, referral in zip(enrollments, referrals):
        earnings[enrollment] = referral
        total_earnings[enrollment] = 0
    
    for seller, amount in zip(sellers, amounts):
        amount *= 100
        while True:
            if seller == '-':
                break
            
            if amount >= 10:
                share = amount // 10
                total_earnings[seller] += amount - share
            else:
                total_earnings[seller] += amount
                break
            
            amount = share
            seller = earnings[seller]
            
    return list(total_earnings.values())
