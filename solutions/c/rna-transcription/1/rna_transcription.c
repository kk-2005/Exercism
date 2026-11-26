#include "rna_transcription.h"
char *to_rna(const char *dna) {
    size_t n;
    size_t i;
    char *rna;

    if (dna == NULL) {
        return NULL;
    }

    n = strlen(dna);
    rna = (char *)malloc(n + 1);
    if (rna == NULL) {
        return NULL;
    }

    for (i = 0; i < n; i++) {
        switch (dna[i]) {
            case 'G': rna[i] = 'C'; break;
            case 'C': rna[i] = 'G'; break;
            case 'T': rna[i] = 'A'; break;
            case 'A': rna[i] = 'U'; break;
            default:
                free(rna);
                return NULL;
        }
    }

    rna[n] = '\0';
    return rna;
}
