#include "TcpConnected.hpp"
#include "TcpClosed.hpp"
#include <iostream>

using namespace std;

void TcpConnected::Connect(TCPConnection *t)
{
    cout << "Already Connected State : TcpConnected" << endl;
}

void TcpConnected::Disconnect(TCPConnection *t)
{
    cout << "TcpConnected -> TCPClosed State Chage" << endl;
    ChangeState(t, TCPClosed::Instance());
}
