// const enum SeatChoice {
enum SeatChoice {
    AISLE,
    MIDDLE,
    WINDOW,
    A = 10,
    B,
    C = "not_number",
    D = 20,
    E
}

const fooSeat = SeatChoice.AISLE;

export {};