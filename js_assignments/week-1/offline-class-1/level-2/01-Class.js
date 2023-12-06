class Animal {
  constructor(name, legCount, age) {
    this.name = name;
    this.legCount = legCount;
    this.age = age;
  }
  describe() {
    return `${this.name} has ${this.legCount} legs and is ${this.age} years old`;
  }
}

// Create an instance of the Animal class
let myAnimal = new Animal("My Dog", 4, 12);

// Call the describe method on the instance
console.log(myAnimal.describe());