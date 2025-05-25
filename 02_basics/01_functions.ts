function addTwo(num: number): number {
    return num + 2;
    // return "foo";
}

function getUpper(val: string) {
    return val.toUpperCase();
}

function signUpUser(name: string, email: string, isPaid: boolean) { }
let loginUser = (name: string, email: string, isPaid: boolean = false) => { }

addTwo(5);
getUpper("starfall");
signUpUser("starfall", "starfall@foo.bar", false);
loginUser("starfall", "starfall@foo.bar");

const greetUser = (s: string): string => { return "hello" };

const colours = ["yellow", "lightblue", "red"];
colours.map((c): string => { return `color is ${c}` });

function logError(errmsg: string): void {
    console.log(errmsg)
}
function handleError(errmsg: string): never {
    throw new Error (errmsg);
}


export { }