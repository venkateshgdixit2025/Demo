using System;

namespace MyApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            // Rule Violation: Hardcoded credentials
            string password = "SuperSecret123";

            // Rule Violation: Inefficient string concatenation in a loop
            string result = "";
            for (int i = 0; i < 20; i++)
            {
                result += i.ToString();  // This should use StringBuilder instead
            }

            Console.WriteLine("Processing complete.");
        }
    }
}
