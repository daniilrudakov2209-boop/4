namespace ConsoleApp;

internal class Program
{
    private static void Main(string[] args)
    {
        int start = 51;
        int end = -9;

        Console.WriteLine("1. Цикл for ");
        for (int i = start; i >= end; i--)
        {
            Console.Write($"{i} ");
        }
        Console.WriteLine();

        Console.WriteLine("2. Цикл while (шаг -2)");
        int current = start;
        while (current >= end)
        {
            Console.Write($"{current} ");
            current -= 2;
        }
        Console.WriteLine();

        Console.WriteLine(" 3. Цикл do while");
        current = start;
        int sumRange = 0;
        do
        {
            sumRange += current;
            current--;
        }
        while (current >= end);

        Console.WriteLine($"Сумма всех чисел от {start} до {end} включительно: {sumRange}");
    }
}
