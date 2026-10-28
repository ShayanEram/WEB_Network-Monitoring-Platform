#include "packet_sniffer.h"
#include <stdio.h>

// Functions----------------------------------------------
void start_capture(void) {
    /* Capture packets */
}

void process_packet(void) {
    /* Extract data */
}

// Main----------------------------------------------------
int main(void) {
    printf("{");
    printf("\"packets\":12845,");
    printf("\"devices\":3,");
    printf("\"tcp\":72,");
    printf("\"udp\":22,");
    printf("\"icmp\":6");
    printf("}");

    start_capture();
    return 0;
}
