using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace ConsoleApp;

internal class Program
{
    private static void Main(string[] args)
    {
       Console.Write("Введите число x: ");
        double x = Convert.ToDouble(Console.ReadLine());
        if (x >= 0)
        {
            double result = Math.Sqrt(x);
            Console.WriteLine("Число неотрицательное, извлечение корня успешно.");
            Console.WriteLine($"Квадратный корень из {x} равен: {result}");
        }
    }
}
    

