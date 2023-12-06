/*
  Implement a class `Calculator` having below methods
    - initialise a result variable in the constructor and keep updating it after every arithmetic operation
    - add: takes a number and adds it to the result
    - subtract: takes a number and subtracts it from the result
    - multiply: takes a number and multiply it to the result
    - divide: takes a number and divide it to the result
    - clear: makes the `result` variable to 0
    - getResult: returns the value of `result` variable
    - calculate: takes a string expression which can take multi-arithmetic operations and give its result
      example input: `10 +   2 *    (   6 - (4 + 1) / 2) + 7`
      Points to Note: 
        1. the input can have multiple continuous spaces, you're supposed to avoid them and parse the expression correctly
        2. the input can have invalid non-numerical characters like `5 + abc`, you're supposed to throw error for such inputs

  Once you've implemented the logic, test your code by running
*/


// Class Definition: class Calculator {}. This is where the Calculator class is defined. 
//Think of a class as a template for creating objects. In this case, the template is for a calculator.

class Calculator {

// Constructor: constructor() { this.result = 0; }. The constructor is a special function that gets called when 
// you create a new calculator using this class. It sets up the initial state of the calculator, 
//which in this case is setting the result to 0.

  constructor() {
      this.result = 0;
  }

  add(number) {
      this.result += number;
  }

  subtract(number) {
      this.result -= number;
  }

  multiply(number) {
      this.result *= number;
  }

  divide(number) {
      if (number === 0) {
          throw new Error("Cannot divide by zero");
      }
      this.result /= number;
  }

  clear() {
      this.result = 0;
  }

  getResult() {
      return this.result;
  }

  calculate(expression) {
      // Check for invalid characters
      if (expression.match(/[^0-9+\-*/().\s]/)) {
          throw new Error("Invalid characters in expression");
      }

      // Remove extra spaces
      expression = expression.replace(/\s+/g, '');

      try {
          // Temporarily update result to check for division by zero
          const tempResult = eval(expression);
          if (!isFinite(tempResult)) {
              throw new Error("Invalid operation (e.g., division by zero)");
          }
          this.result = tempResult;
      } catch (error) {
          throw new Error("Invalid expression");
      }

      return this.result;
  }
}

module.exports = Calculator;