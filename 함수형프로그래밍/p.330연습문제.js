cusomters = []

function average(numbers) {
    return reduce(numbers, 0, plus) / numbers.length 
}

function plus(a ,b) {
    return a+b
}

function averagePurchaseTotals(cusomters) {
    const purchases = map(cusomters, cusomterTotalPrice)
    return average(purchases)
}

function cusomterTotalPrice(customer) {
    return customer.purchase.total;
}