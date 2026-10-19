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
        Console.Write("Введите возраст: ");
        int age = Convert.ToInt32(Console.ReadLine());

        if (age < 0)
        {
            Console.WriteLine("Ошибка: возраст не может быть отрицательным.");
        }
        else if (age <= 6)
        {
            Console.WriteLine("Возрастная категория: дошкольный");
        }
        else if (age <= 17)
        {
            Console.WriteLine("Возрастная категория: школьный");
        }
        else if (age <= 59)
        {
            Console.WriteLine("Возрастная категория: взрослый");
        }
        else
        {
            Console.WriteLine("Возрастная категория: старшая возрастная группа");
        }
    }
}
    

