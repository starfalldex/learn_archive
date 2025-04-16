const foo = {
    name: "dex",
    email: "dex@foo.bar",
    isActive: true,
}

function createUser1({ name: string, isPaid: boolean }) { }
createUser1({ name: "dex", isPaid: false });

function createCourse(): { name: string, price: number } {
    return { name: "foobar", price: 999 }
}

type User1 = {
    name: string;
    email: string;
    isActive: boolean;
}
function createUser2(user: User1): User1 {
    return { name: "foo", email: "bar", isActive: true }
}
createUser2({ name: "foo", email: "bar", isActive: true })

type User2 = {
    readonly _id: string;
    name: string;
    email: string;
    isActive: boolean;
    paymentDetails?: number;
}
let fooUser: User2 = {
    _id: "123",
    name: "dex",
    email: "dex@foo@bar",
    isActive: true
}
fooUser.email = "dex2"
// cant change _id because it is readonly
// myUser._id = "1234"

type cardNumber = {
    cardnumber: string;
}
type cardDate = {
    carddate: string;
}
type cardDetails = cardNumber & cardDate & {
    cvv: number;
}

export { };