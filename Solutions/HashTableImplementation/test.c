#include "hash.h"

int main(void) {

   Hash h = initialiseHash();

   put("chris", 42, h);
   assert(get("chris", h) == 42);
   put("charlie", 93, h);
   assert(get("charlie", h) == 93);
   put("$BillYall", 69, h);
   assert(get("$BillYall", h) == 69);
   put("<xXxDefil3rxXx>", 420, h);
   assert(get("<xXxDefil3rxXx>", h) == 420);

   //printf("h length is %p", h);

   return EXIT_SUCCESS;
}
