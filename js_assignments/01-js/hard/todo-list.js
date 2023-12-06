/*
  Implement a class `Todo` having below methods
    - add(todo): adds todo to list of todos
    - remove(indexOfTodo): remove todo from list of todos
    - update(index, updatedTodo): update todo at given index
    - getAll: returns all todos
    - get(indexOfTodo): returns todo at given index
    - clear: deletes all todos

  Once you've implemented the logic, test your code by running
*/

class Todo {
  constructor() {
      this.todos = [];
  }

  // Add a new todo
  add(todo) {
      this.todos.push(todo);
  }

  // Remove a todo by index, handle invalid indexes gracefully
  remove(index) {
      if (index < 0 || index >= this.todos.length) {
          return; // Silently handle invalid index
      }
      this.todos.splice(index, 1);
  }

  // Update a todo at a specific index, handle invalid indexes gracefully
  update(index, updatedTodo) {
      if (index < 0 || index >= this.todos.length) {
          return; // Silently handle invalid index
      }
      this.todos[index] = updatedTodo;
  }

  // Get all todos
  getAll() {
      return this.todos;
  }

  // Get a specific todo by index, return null for invalid index
  get(index) {
      if (index < 0 || index >= this.todos.length) {
          return null;
      }
      return this.todos[index];
  }

  // Clear all todos
  clear() {
      this.todos = [];
  }
}

module.exports = Todo;