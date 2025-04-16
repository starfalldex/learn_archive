const score: Array<number> = [];
const names: Array<string> = [];

function identityOne(val: boolean | number): boolean | number {
    return val;
}

function identityTwo(val: any): any {
    return val;
}

function identityThree<Type>(val: Type): Type {
    return val;
}
// identityThree(true)

function identityFour<T>(val: T): T {
    return val;
}

interface Bootle {
    brand: string,
    type: number
}
// identityFour<Bootle>({})

function getWithNormalFun<T>(products: T[]): T {
    // do some search database operations
    const myIndex = 3;
    return products[myIndex];
}

const getWithArrowFun = <T,>(products: T[]): T => {
    //do some more database operations
    const myIndex = 3;
    return products[myIndex];
}

interface Database {
    connection: string,
    username: string,
    password: string
};
function someFunction<T, U extends Database>(foo: T, bar: U): Object {
    return {
        foo, bar
    }
}
// someFunction(3, { connection: "", username: "", password: "" })

interface Quiz {
    name: string,
    type: string
};

interface Course {
    name: string,
    author: string,
    subject: string
};

class Sellable<T> {
    public cart: T[] = [];

    addToCart(product: T) {
        this.cart.push(product);
    }
}

