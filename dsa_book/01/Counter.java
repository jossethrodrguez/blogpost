public class Counter {
    public static void main(String[] args) {
        /* We create a object called Counter that increase a reset the count value */
        Counter c = new Counter(); // Counter Object reference it to c variable
        c.increment(); // increase its value by one
        c.increment(3); // increase its value by three
        int temp = c.getCount(); // its value is 4
        c.reset(); // value becomes 0
        Counter d = new Counter(5); // declares and construct a counter having 5
        System.out.println(temp + " " + d);

    }

    // Instance Variables
    int count = 0; // This store our count
    
    // creating Objects
    public Counter() { } // This created the object, is a construtor method, the default vaule is null
    public Counter(int initial) { count = initial; } // alternate constuctor, we can specify the count value

    // Methods
    public int getCount() { return count; } // An accessor method
    public void increment() { count++; } // An update method
    public void increment(int delta) { count += delta; } // An update method
    public void reset() { count = 0; } // An update method 

}