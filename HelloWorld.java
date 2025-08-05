public class HelloWorld {
    // Instance variables
    private String name;
    private int age;
    
    // Constructor
    public HelloWorld(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    // Default constructor
    public HelloWorld() {
        this.name = "World";
        this.age = 0;
    }
    
    // Method to display greeting
    public void greet() {
        System.out.println("Hello, " + name + "!");
        if (age > 0) {
            System.out.println("You are " + age + " years old.");
        }
    }
    
    // Method to demonstrate loops
    public void countToTen() {
        System.out.println("\nCounting from 1 to 10:");
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + " ");
        }
        System.out.println(); // New line
    }
    
    // Method to calculate factorial
    public long factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
    
    // Static method to demonstrate arrays
    public static void demonstrateArrays() {
        System.out.println("\nArray demonstration:");
        int[] numbers = {5, 10, 15, 20, 25};
        
        System.out.print("Array elements: ");
        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
        
        // Calculate sum
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        System.out.println("Sum of array elements: " + sum);
    }
    
    // Main method - entry point of the program
    public static void main(String[] args) {
        System.out.println("=== Simple Java Program Demo ===");
        
        // Create objects
        HelloWorld defaultGreeting = new HelloWorld();
        HelloWorld personalGreeting = new HelloWorld("Alice", 25);
        
        // Call methods
        defaultGreeting.greet();
        personalGreeting.greet();
        
        // Demonstrate loops
        defaultGreeting.countToTen();
        
        // Demonstrate recursion
        int number = 5;
        long result = personalGreeting.factorial(number);
        System.out.println("\nFactorial of " + number + " is: " + result);
        
        // Demonstrate static method and arrays
        demonstrateArrays();
        
        // Demonstrate conditional statements
        System.out.println("\nConditional demonstration:");
        int score = 85;
        if (score >= 90) {
            System.out.println("Grade: A");
        } else if (score >= 80) {
            System.out.println("Grade: B");
        } else if (score >= 70) {
            System.out.println("Grade: C");
        } else {
            System.out.println("Grade: F");
        }
        
        System.out.println("\n=== Program completed successfully! ===");
    }
}