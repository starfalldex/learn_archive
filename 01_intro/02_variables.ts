//string
let greet: string = "Starfall";
greet.toLowerCase();
console.log("Hello, World!", greet);

// numbers
let userId: number = 345345;
console.log(userId);

// boolean
let isLoggedIn: boolean = false;
console.log(isLoggedIn)

// dont - let hero;
let hero: string;
function getHero() {
    return "ironman"
}
hero = getHero();

// good practice
// not use 'type' everywhere if assigning value directly
// don't - let foo: type = bar; 
// do js -let foo = bar; 
// always avoid this - any


export { }