#include "TcpState.hpp"

void TCPState::ChangeState(TCPConnection *instance, TCPState *state)
{
    instance->ChangeState(state);
}