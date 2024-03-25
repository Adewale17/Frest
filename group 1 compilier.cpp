#include <iostream>
#include <vector>

// Function to assign loads to servers
void assignLoad(std::vector<int>& servers, int load) {
    int minLoadServer = 0;  // Index of the server with minimum load
    int minLoad = servers[0];  // Minimum load initialized to the first server's load

    // Find server with minimum load
    for (int i = 1; i < servers.size(); ++i) {
        if (servers[i] < minLoad) {
            minLoad = servers[i];  // Update minimum load
            minLoadServer = i;  // Update index of server with minimum load
        }
    }

    // Assign load to the server with minimum load
    servers[minLoadServer] += load;

    // Calculate processing time for the load
    double processingTime = load / 	9.5; // Assuming a constant processing rate of 1.5 units per minute

    // Display load and processing time for the assigned server
    std::cout << "Server " << minLoadServer + 1 << " is handling load : " << servers[minLoadServer] 
              << "   Processing Time = " << processingTime << " Seconds" << std::endl;
}

int main() {
    int numServers = 5; // Number of servers
    std::vector<int> serverLoad(numServers, 0); // Initialize all servers' loads to 0

    // List of loads to be assigned
    std::vector<int> loads;
    loads.push_back(3);
    loads.push_back(5);
    loads.push_back(8);
    loads.push_back(2);
    loads.push_back(7);
    // Assign loads to servers
    for (size_t i = 0; i < loads.size(); ++i) {
        assignLoad(serverLoad, loads[i]);
    }

    return 0;
}

