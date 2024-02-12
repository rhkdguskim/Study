#include "TcpConnection.hpp"
#include "TcpClosed.hpp"
#include "TcpConnected.hpp"
#include "../singleton_pattern/Singleton.hpp"

// init singleton mutex
template <>
std::mutex Singleton<TcpConnected>::_mutex;
template <>
std::mutex Singleton<TCPClosed>::_mutex;

int main() {
    TCPConnection connection;

    connection.Connect();
    connection.Connect();

    connection.Disconnect();
    connection.Disconnect();

    return 0;
}