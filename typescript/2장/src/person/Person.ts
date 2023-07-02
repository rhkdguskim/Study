import * as U from "../utils/makePerson"
import IPerson from "./IPerson"

export default class Person implements IPerson {
    constructor(public name: string, public age: number = U.makeRandomNumber()) {}
}

export const makePerson2 = (name:string, age:number = U.makeRandomNumber()) => ({name,age})