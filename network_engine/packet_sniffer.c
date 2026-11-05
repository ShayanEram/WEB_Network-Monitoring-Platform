#include "packet_sniffer.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#ifdef _WIN32
#include <windows.h>
#define sleep_ms(ms) Sleep(ms)
#else
#include <unistd.h>
#define sleep_ms(ms) usleep((ms) * 1000)
#endif

// Functions----------------------------------------------
void start_capture(void) {
    /* Future Npcap loop placeholder */
}

void simulate_packet_capture() {
    // Arrays of mock data to create realistic variety
    const char* src_ips[] = {"192.168.1.50", "192.168.1.101", "192.168.1.15",
                             "192.168.1.10", "192.168.1.75",  "192.168.1.88"};

    const char* dest_ips[] = {"142.250.190.46", "8.8.8.8",     "151.101.193.140",
                              "13.107.42.14",   "192.168.1.1", "172.217.14.206"};

    const char* protocols[] = {"TCP", "UDP", "ICMP", "DNS", "TCP", "TCP"};

    int num_src = sizeof(src_ips) / sizeof(src_ips[0]);
    int num_dest = sizeof(dest_ips) / sizeof(dest_ips[0]);
    int num_protos = sizeof(protocols) / sizeof(protocols[0]);

    srand((unsigned int)time(NULL));

    // Stream continuous packets simulating live network traffic
    while (1) {
        const char* source_ip = src_ips[rand() % num_src];
        const char* destination_ip = dest_ips[rand() % num_dest];
        const char* protocol = protocols[rand() % num_protos];
        int packet_size = 64 + (rand() % 1400);  // Random size between 64 and 1464 bytes

        // Print CSV format: source,dest,size,protocol
        printf("%s,%s,%d,%s\n", source_ip, destination_ip, packet_size, protocol);
        fflush(stdout);  // Ensure it outputs immediately to Python subprocess

        sleep_ms(1500);  // Wait 1.5 seconds between packets
    }
}

// Main----------------------------------------------------
int main(void) {
    simulate_packet_capture();
    start_capture();
    return 0;
}