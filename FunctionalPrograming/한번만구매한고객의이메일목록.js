const customers = Array.from({ length: 5 }, () => ({}));

function isOnePurchaseCumstomer(customer) {
    return customer.purchases.length === 1
}
function getCustomerEmail(customer) {
    return customer.email;
}

const onePurchaseCustomers = filter(customers, isOnePurchaseCumstomer)
const emails = map(onePurchaseCustomers, getCustomerEmail)