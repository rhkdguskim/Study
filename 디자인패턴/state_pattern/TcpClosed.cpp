#include "TcpClosed.hpp"
#include "TcpConnected.hpp"
#include <iostream>

using namespace std;
void TCPClosed::Connect(TCPConnection *t)
{
    cout << "TCPClosed -> TcpConnected State Chage" << endl;
    ChangeState(t, TcpConnected::Instance());
}

void TCPClosed::Disconnect(TCPConnection *t)
{
    cout << "Already Disconnected State : TCPClosed" << endl;
}
