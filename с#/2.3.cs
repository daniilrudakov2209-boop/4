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
       Console.Write("Введите целое число n: ");
        int n = Convert.ToInt32(Console.ReadLine());

        string result = (n >= 10 && n <= 99) 
            ? "является двузначным положительным числом от 10 до 99" 
            : "не является двузначным положительным числом от 10 до 99";

        Console.WriteLine($"Число {n} {result}.");
    }
}
    

