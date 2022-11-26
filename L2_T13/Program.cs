Console.Write("Введите число: ");
int a = Convert.ToInt32(Console.ReadLine());
if (a < 100)
{
    Console.WriteLine($"{a} - Нет третьего числа");
}
else 
{
Console.Write($"{a} -> ");
while (a>1000)
{
    a /=10;
}
Console.WriteLine($"{a%10}");
}


