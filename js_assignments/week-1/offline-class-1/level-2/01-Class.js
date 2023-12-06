class Animal {
  constructor(name, legCount, age) {
    this.name = name;
    this.legCount = legCount;
    this.age = age;
  }
  describe() {
    return `${this.name} has ${this.legCount} legs and is ${this.age} years old`;
  }
  describe2() {
    return `This ${this.name} has ${this.legCount} legs and is ${this.age} years old`;
  }
}

// Create an instance of the Animal class
let myAnimal = new Animal("Dog", 4, 12);

// Call the describe method on the instance
console.log(myAnimal.describe());

// Call the describe method on the instance
console.log(myAnimal.describe2());