using System;   // instead of calling `System` everytime before `Console.WriteLine()`
// the first line of code using System; tells the C# compiler to look in the base class library if it can't find 
// the method definition in your code.

namespace World
{
    public class Hello
    {
        // The code `public static void Main()` and its set of curly braces define a type of code block called a method. 
        // A method contains a grouping of code that works toward a single purpose or responsibility in your software system.
        // Methods are organized inside other code blocks called classes. 
        // A class can contain one or more methods. Ideally, all of the methods in a class have a related purpose in the system. 
        // The class in the preceding code is named Program.
        public static void Main(string[] args)
        {

            // Console.WriteLine("Hello World!");

            // This will print Congratulations! You wrote your first lines of code!
            Console.Write("Congratulations!"); // System is a base class library - Console is a class -  Write is a class method.
            Console.Write(" ");
            Console.Write("You wrote your first lines of code!");






        }

        private static void Unit4()
        {
            // 1. A command to compile your new code invokes the C# compiler.

            // 2. The C# compiler ensures your code can be compiled and is free from syntax errors. If it can't compile your code, 
            // the compiler stops and sends an error message back to the Output pane.

            // 3. If the C# compiler succeeds, the .NET runtime opens the newly compiled .NET assembly. 
            // By default, it looks in a class named Program to find a method named Main() to begin running the instructions.

            // 4. Instruction by instruction, the .NET runtime evaluates each line of code. It runs the instruction and moves to the next line of code.

            // 5. In this case, when the instruction to print the words "Hello world!" finishes, 
            // the running path continues to the next line but finds nothing. The path ends, and the 
            // .NET runtime removes the program from its memory. Meanwhile, the output from the WriteLine() 
            // instruction is delivered back to your web browser.
        }
    }
}


