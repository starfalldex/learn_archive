class User {

    protected _courseCount = 1
    readonly _city: string = ""
    constructor(
        public email: string,
        public name: string,
        // private userid: string
    ) { }

    private deleteToken(){
        console.log("Token deleted");
        
    }

    get getAppleEmail(): string{
        return `apple${this.email}`
    }

    get courseCount(): number {
        return this._courseCount
    }

    set courseCount(courseNum) {
        if (courseNum <= 1) {
            throw new Error("Course count should be more than 1")
        }
        this._courseCount = courseNum
    }
}

class SubUser extends User {
    isFamily: boolean = true
    changeCourseCount(){
        this._courseCount = 4
    }
}

const foo = new User("foo@email.com", "bar")
// foo.city = "bar"

export {}