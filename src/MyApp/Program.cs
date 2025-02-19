using System;

namespace MyApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            int x = 10; // Example of a meaningful variable name
            int y = 30;

            int result = Add(x, y);
            Console.WriteLine($"The result is: {result}");
        }

        static int Add(int a, int b)
        {
            return a + b;
        }
    }
}
