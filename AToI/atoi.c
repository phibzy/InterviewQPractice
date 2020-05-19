#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <limits.h>

int myAtoi(char * s);
int numSum(char * s, int count, int negSign);


int main(int argc, char*argv[]) {
  
   int thing = myAtoi("-91283472332");
   /*int thing = myAtoi("-912");*/
   printf("%d", thing);

   return EXIT_SUCCESS;
}

int myAtoi(char * s) {
   long total = 0;
   int negSign = 1;
   int count = 0;

   //printf("I am the function\n");

   char nextChar = s[count];

   while (nextChar != '\0') {
      if (nextChar != ' ') { 
         if (nextChar == '+' || nextChar == '-') {
            if (nextChar == '-') { negSign = -1; }
            count++;
            total = numSum(s, count, negSign);
            break;
         } else if ('0' <= nextChar && nextChar <= '9') {
            total = numSum(s, count, negSign);
            break;
         } else {
            break;
         }
      } 

      count++;
      nextChar = s[count];
   }   

   return total;
}


int numSum(char * s, int count, int negSign) {
      long sum = 0;
      char nextChar = s[count];
      int val = 0;

      while ('0' <= nextChar && nextChar <= '9') {
         val = nextChar - '0';

         sum = 10*sum + val*negSign;
         
         if (sum <= INT_MIN) {
            sum = INT_MIN;
            break;
         }

         if (sum >= INT_MAX) {
            sum = INT_MAX;
            break;
         }

         count++;
         nextChar = s[count];
      }
      return sum;
}


