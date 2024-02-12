#include "TcpConnection.hpp"
#include "TcpState.hpp"
#include "TcpClosed.hpp"

TCPConnection::TCPConnection()
{
    _state = TCPClosed::Instance();
}

void TCPConnection::Connect()
{
    _state->Connect(this);
}

void TCPConnection::Disconnect()
{
    _state->Disconnect(this);
}
