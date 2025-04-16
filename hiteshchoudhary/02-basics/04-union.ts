let score: number | string = 10;
score = '10';

type User = {
    id: number;
    name: string;
}
type Admin = {
    id: number;
    username: string;
}
let foo: User | Admin = { id: 23, name: "foobar" }

function getDbId(id: number | string) {
    if (typeof id === "string") {
        id.toLowerCase();
    }
}
getDbId(1);

const data: (number | string | boolean)[] = [1, 2, "foo", true, false]

let seatType: "A" | "B" | "C";
seatType = "A";
// cant assign other values
// seatType = "Z";

export { };