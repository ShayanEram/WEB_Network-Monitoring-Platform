#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// XOR key for encryption/decryption
#define KEY 0x5A  // Arbitrary byte value

// Encrypts a string using XOR cipher
char* encrypt(char* input) {
    size_t len = strlen(input);
    char* output = (char*)malloc(len + 1);
    if (!output) return NULL;

    for (size_t i = 0; i < len; i++) {
        output[i] = input[i] ^ KEY;
    }
    output[len] = '\0';
    return output;
}

// Decrypts a string using XOR cipher (same as encryption)
char* decrypt(char* input) {
    return encrypt(input);  // XOR is symmetric
}