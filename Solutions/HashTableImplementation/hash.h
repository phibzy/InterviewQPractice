#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

typedef struct _hash * Hash;

// Returns value of key
// Returns -1 if not in hash table
int get(char* key, Hash h);

// Returns 0 if all is well
// Returns -1 if hash table is full
int put(char * key, int value, Hash h);

// Create the hash
Hash initialiseHash(void);
