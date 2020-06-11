#include "hash.h"
#include <string.h>


// Will implement with chaining

typedef struct _node * Node;
static int hashFunc(char * key);
static void printHash(Hash h);

struct _node {
   char * key;
   int value;
   Node next;
};

struct _hash {
   Node table[20];
   int length;
};

int get(char*key, Hash h) {
   int index = hashFunc(key) % 20;

   Node curr = h->table[index];
   
   while (curr != NULL) {
      if (strcmp(curr->key, key) == 0) {
         return curr->value;
      }
      curr = curr->next;
   }

   printHash(h);
   return -1;
}

int put(char* key, int value, Hash h) {
   int index = hashFunc(key) % 20;

   Node n = malloc(sizeof(struct _node));
   n->key = key;
   n->value = value;
   
   if (h->table[index] == NULL) {
      h->table[index] = n;
   } else {
      Node curr = h->table[index];

      while (curr->next != NULL) {
         curr = curr->next;
      }
      curr->next = n;
   }

   printHash(h);
   return 0;
}

static int hashFunc(char*key) {
   assert(strcmp(key, ""));

   // Return ascii value of first char in string
   return (int) key[0];
}

static void printHash(Hash h) {
   Node curr;

   for (int i = 0; i < 20; i++) {
      printf("Index %d: ", i);
      curr = h->table[i];

      while (curr != NULL) {
         printf("--> Key %s, Value %d ", curr->key, curr->value);
         curr = curr->next;
      }

      printf("-->\n");
   }
   printf("\n");
}

Hash initialiseHash(void) {
   Hash h = malloc(sizeof(struct _hash));
   struct _hash n = {.table = {NULL}, .length = 0}; 
   *h = n;

   return h;

}

