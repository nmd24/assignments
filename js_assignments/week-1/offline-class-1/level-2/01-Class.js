class Animal {
  constructor(name, legCount) {
    this.name = name;
    this.legCount = legCount;
  }
  describe() {
    return `${this.name} has ${this.legCount} legs`;
  }
}

// Create an instance of the Animal class
let myAnimal = new Animal("animal", 10);

// Call the describe method on the instance
console.log(myAnimal.describe());