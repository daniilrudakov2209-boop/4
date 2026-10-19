namespace ConsoleApp;

internal class Program
{
    static void Main()
    {
        Console.Write("Введите число N: ");
        int n = Convert.ToInt32(Console.ReadLine());

        double sum = 0;

        for (int i = 1; i <= n; i++)
        {
            sum += 1.0 / (i + 4);
        }

        Console.WriteLine($"Сумма S = {sum:F1}");
    }
}