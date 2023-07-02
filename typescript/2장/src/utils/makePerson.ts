const MAX_AGE = 100

export function makePerson(name:string, age:number) {
    return {name:name, age:age}
}
export function testMakePerson() {
    console.log(
        makePerson('Jane', 22),
        makePerson('Jack', 33)
    )
}

export function makeRandomNumber(max : number = MAX_AGE): number {
    return Math.ceil((Math.random() * max))
}