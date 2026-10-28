#include "packet_sniffer.h"
#include <stdio.h>

// Functions----------------------------------------------
void start_capture(void) {
    /* Capture packets */
}

void process_packet(void) {
    /* Extract data */
}

void simulate_packet_capture() {
    // Hardcoded packet data for now (later, this will be libpcap loop)
    const char* source_ip = "192.168.1.50";
    const char* destination_ip = "142.250.190.46";
    int packet_size = 512;
    const char* protocol = "TCP";

    // Print CSV format: source,dest,size,protocol
    printf("%s,%s,%d,%s\n", source_ip, destination_ip, packet_size, protocol);
    fflush(stdout);  // Ensure it outputs immediately
}

// Main----------------------------------------------------
int main(void) {
    simulate_packet_capture();
    start_capture();
    return 0;
}
