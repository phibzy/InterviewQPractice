#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int myAtoi(char * s);
int numSum(char * s, int count);


int main(int argc, char*argv[]) {
  
   int thing = myAtoi("-91283472332");
   printf("%d", thing);

   return EXIT_SUCCESS;
}

int myAtoi(char * s) {
   unsigned int total = 0;
   int negSign = 1;
   int count = 0;

   //printf("I am the function\n");

   char nextChar = s[count];

   while (nextChar != '\0') {
      if (nextChar != ' ') { 
         if (nextChar == '+' || nextChar == '-') {
            if (nextChar == '-') { negSign = -1; }
            count++;
            total = numSum(s, count);
            break;
         } else if ('0' <= nextChar && nextChar <= '9') {
            total = numSum(s, count);
            break;
         } else {
            break;
         }
      } 

      count++;
      nextChar = s[count];
   }   

   total = total * negSign;

   if (total < pow(-2,31)) {

      total = pow(2, 31); 

   } else if (total > pow(2, 31) - 1) {
  
      total = pow(2, 31) - 1;

   }

   int rTotal = 0;

   rTotal = total * negSign;

   return rTotal;
}


int numSum(char * s, int count) {
      unsigned int sum = 0;
      char nextChar = s[count];
      int val = 0;

      while ('0' <= nextChar && nextChar <= '9') {
         printf("nextChar is %c\n", nextChar);
         val = nextChar - '0';
         sum = 10*sum + val;
         printf("sum is %d\n", sum);

         count++;
         nextChar = s[count];
      }
      return sum;
}


