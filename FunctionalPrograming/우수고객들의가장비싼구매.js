const customers = Array.from({ length: 5 }, () => ({}));

// 우수 고객은 3개 이상 구매한 사람이다.
const BestCustomer = filter(customers, function (customer) {
    return customer.purchases.length >= 3;
})

// 우수고객중에 가장 비싼 물품을 알려줘
map(BestCustomer, function (customer) {
       return reduce(customer.purchases, 0, function(cur, purchase) {
            if (purchase.total > cur.total) {
                return purchase
            }
            else {
                return cur
            }
       })
})

function maxKey(array, init, f) {
    return reduce(array, init, function(cur, element) {
        if (f(cur) > f(element)) {
            return cur
        } else {
            return element
        }
    })
}

map(BestCustomer, function (customer) {
    return maxKey(customer.purchases, {total : 0}, function (purchase) {
        return purchase.total
    })
})