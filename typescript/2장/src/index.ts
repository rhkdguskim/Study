import { testMakePerson } from "./utils/makePerson"
import Person, { makePerson2 } from "./person/Person"
import IPerson from "./person/IPerson"
import Chance  from "chance"
import * as R from "ramda"
testMakePerson()

const testMakePerson2 = ():void => {
    let jane: IPerson = makePerson2('Jane')
    let jack: IPerson = new Person("Jack")
    console.log(jane, jack)
}

testMakePerson2()

const chance = new Chance()
let persons : IPerson[] = R.range(0,2).map((n:number) => new Person(chance.name(), chance.age()))
console.log(persons)