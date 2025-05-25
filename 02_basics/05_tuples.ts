// const user: (string | number)[] = [1, "hc"]
let user: [string, number, boolean];
user = ["foobar", 131, true];

let rgb: [number, number, number] = [255, 123, 112];

type User = [number, string]
const newUser: User = [112, "starfall@foo.com"]
// this can be done in touples but it should not happen
newUser[1] = "hc.com"
newUser.push("this can be pushed")
// this can be prevented by using
// readonly tuple
// ex type User = readonly [number, string]

export { };