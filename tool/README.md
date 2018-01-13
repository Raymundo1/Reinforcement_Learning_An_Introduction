# Simple Intro for some tools

## RL_glue
* RL-glue is a communication protocol
    * a system of rules that allow two or more entities to
transmit information 
    * ...defining the rules syntax, semantics and
synchronization of communication

* A Standard Interface
    * The implementation of the RL-glue protocol is realized as
a standard software interface that the agent and
environment must implement 

    * Agent - An agent that is compatible with RL-glue is required to
implement a set of standard functions:
        * agent_init, agent_start, agent_step, agent_cleanup,
agent_message
        * a python program implements these functions is
compatible with RL-glue. We call it an **agent program**

    * Environment - An environment that is compatible with RL-glue is
required to implement a set of standard functions:
        * env_init, env_start, env_step, env_cleanup,
env_message
        * a python program implements these functions is
compatible with RL-glue. We call it an **environment
program**

resource: rl-glue-tutorial made by [Richard Sutton](http://richsutton.com) Team
