#ifndef TCPCONNECTED
#define TCPCONNECTED
#include "TcpState.hpp"
#include "../singleton_pattern/Singleton.hpp"

class TcpConnected : public TCPState, Singleton<TcpConnected>
{
    public:
        static TCPState* Instance()
        {
            return Singleton<TcpConnected>::Instance();
        }
        virtual void Connect(TCPConnection*);
        virtual void Disconnect(TCPConnection*);
};
#endif