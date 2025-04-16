"use strict";
const score = [];
const names = [];
function identityOne(val) {
    return val;
}
function identityTwo(val) {
    return val;
}
function identityThree(val) {
    return val;
}
// identityThree(true)
function identityFour(val) {
    return val;
}
// identityFour<Bootle>({})
function getWithNormalFun(products) {
    // do some search database operations
    const myIndex = 3;
    return products[myIndex];
}
const getWithArrowFun = (products) => {
    //do some more database operations
    const myIndex = 3;
    return products[myIndex];
};
;
function someFunction(foo, bar) {
    return {
        foo, bar
    };
}
;
;
class Sellable {
    constructor() {
        this.cart = [];
    }
    addToCart(product) {
        this.cart.push(product);
    }
}
