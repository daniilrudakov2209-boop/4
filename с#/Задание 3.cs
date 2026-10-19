namespace ConsoleApp;
internal class Program
{
    private static void Main(string[] args)
    {
        
        Console.Write("Введите строку: ");
        string? text = Console.ReadLine();

        Console.Write("Введите  символ: ");
        char target = Convert.ToChar(Console.ReadLine());

        int count = 0;

        Console.WriteLine("\nСимволы строки:");
        if (text != null)
        {
            foreach (char symbol in text)
            {
                Console.WriteLine(symbol);
                if (symbol == target)
                {
                    count++;
                }
            }
        }

        Console.WriteLine($" Символ '{target}' встречается в строке: {count} раз(а)");
    }
}
