const customers = Array.from({ length: 5 }, () => ({}));

// 두번이상 구매한사람인지?
function isTwicePurchaseCumtomer(customer) {
    return customer.purchases.length >= 2;
}

function isOverOneHunredDollorPurchase(customer) {
    return customer.purchases.total > 100
}

function bigSpenders(customers) {
    filter(customers, function(customer) {
        return isOverOneHunredDollorPurchase(customer) && isTwicePurchaseCumtomer(customer)
    })
}