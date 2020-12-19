using System;
using System.Net;
using System.Net.Sockets;
using System.IO;
using System.Linq;
using System.Collections.Generic;

namespace CSharp_Shell
{

    public static class Program 
    {
        public static void Main(){
            Console.WriteLine("Input Card Number:");
            int card = Convert.ToInt32(Console.ReadLine());
            if (card == 4445){
                Console.WriteLine("Please Enter PassWord(Card List-Number:{0}.):",card);
                string passwd = Console.ReadLine();
                if (passwd == "3k8z"){
                    Console.WriteLine("Success! Thanks For You Using Our Product.");
                }else{
                    Console.WriteLine("The PassWord:{0} Can't Against To Card List-number{1}",card,passwd);
                }
                    
            }
            else{
                Console.WriteLine("Bad Card Number:{0}.",card);
                
            }
        }
    }
}
