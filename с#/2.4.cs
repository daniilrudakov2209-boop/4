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
        Console.WriteLine("Выберите код преобразования:");
        Console.WriteLine("1 — сантиметры в метры");
        Console.WriteLine("2 — метры в сантиметры");
        Console.WriteLine("3 — килограммы в граммы");
        Console.WriteLine("4 — граммы в килограммы");
        Console.Write("Ваш выбор: ");
        int code = Convert.ToInt32(Console.ReadLine());
        
        Console.Write("Введите значение величины: ");
        double x = Convert.ToDouble(Console.ReadLine());

      
        switch (code)
        {
            case 1:
                double meters = x / 100;
                Console.WriteLine($"{x} см = {meters} м");
                break;

            case 2:
                double centimeters = x * 100;
                Console.WriteLine($"{x} м = {centimeters} см");
                break;

            case 3:
                double grams = x * 1000;
                Console.WriteLine($"{x} кг = {grams} г");
                break;

            case 4:
                double kilograms = x / 1000;
                Console.WriteLine($"{x} г = {kilograms} кг");
                break;

            default:
                Console.WriteLine("Ошибка: указан неверный код преобразования (допустимы значенияот 1 до 4).");
                break;
                
        }
    }
}
    

