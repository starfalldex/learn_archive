interface User {
    readonly dbId: number
    email: string,
    userId: number,
    googleId?: string
    // startTrail: () => string
    startTrail(): string
    getCoupon(couponname: string, value: number): number
}

interface User {
    githubToken: string
}

interface Admin extends User {
    role: "admin" | "ta" | "learner"
}

const foo: Admin = {
    dbId: 2,
    email: "starfall@foo.com",
    userId: 222,
    role: "admin",
    githubToken: "gitgitgit",
    startTrail: () => {
        return "trail started"
    },
    getCoupon: (name: "foo100", off: 100) => {
        return 100
    }
}
foo.email = "foo@email.bar"

export { }