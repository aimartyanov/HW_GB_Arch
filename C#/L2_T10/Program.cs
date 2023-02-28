Console.Write("Введите трехзначное число: ");
int a = Convert.ToInt32(Console.ReadLine());
int b = a%100/10;
Console.WriteLine($"{a} -> {b}");