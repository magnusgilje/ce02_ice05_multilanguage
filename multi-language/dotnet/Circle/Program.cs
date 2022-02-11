using System;

namespace Circle
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                float radius = float.Parse(args[0]);

                Circle circle = new Circle(radius);
                Console.WriteLine(circle.Summary());                 
            }
            catch (IndexOutOfRangeException e)
            {
                Console.WriteLine("Invalid or non radius entered: {0}", e); 
            }
        }
    }
}
