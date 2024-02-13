#ifndef TCPCONNECTION
#define TCPCONNECTION
class TCPState;
class TCPConnection
{
    public:
        TCPConnection();
        void Connect();
        void Disconnect();
    private:
        void ChangeState(TCPState*);
        friend class TCPState;
    private:
        TCPState* _state;
};
#endif