#ifndef TCPSTATE
#define TCPSTATE
#include "TcpConnection.hpp"

class TCPState
{
    public:
        virtual void Connect(TCPConnection*);
        virtual void Disconnect(TCPConnection*);
    protected:
        void ChangeState(TCPConnection*, TCPState*);
};
#endif