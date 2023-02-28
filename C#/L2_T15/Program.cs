Console.Write("Введите день недели в виде числа: ");
int a = Convert.ToInt32(Console.ReadLine());
if (a >=1 && a <=5)
{
    Console.WriteLine($"{a} -> Нет");
}
else if (a >=6 && a<=7)
{
        Console.WriteLine($"{a} -> Да");
}
