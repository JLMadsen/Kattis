using System;
class Program
{
    static void Main(string[] args)
    {
        string input = Console.ReadLine();

        string[] tmp = input.Split(" ");

        int fizz = int.Parse(tmp[0]);
        int buzz = int.Parse(tmp[1]);
        int target = int.Parse(tmp[2]);

        for (int i = 1; i < target + 1; i++)
        {
            string result = "";

            if (i % fizz == 0)
                result += "fizz";

            if (i % buzz == 0)
                result += "buzz";

            if (i % fizz != 0 && i % buzz != 0)
                result = i.ToString();

            Console.WriteLine(result);
        }
    }
}