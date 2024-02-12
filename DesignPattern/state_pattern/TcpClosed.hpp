#ifndef TCPCLOSED
#define TCPCLOSED
#include "TcpState.hpp"
#include "../singleton_pattern/Singleton.hpp"
class TCPClosed : public TCPState, Singleton<TCPClosed>
{
    public:
        static TCPState* Instance()
        {
            return Singleton<TCPState>::Instance();
        }
        virtual void Connect(TCPConnection*);
        virtual void Disconnect(TCPConnection*);
};
#endif