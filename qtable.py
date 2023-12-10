import numpy as np
import pandas as pd
import os

class QTable:
    '''
    Q-learning
    e-greedy 
    '''
    def __init__(self,action:list,learning_rate:int=0.2,discount_factor:int=0.8,e_greedy:int=0.1):
        self.actions=action
        self.lr=learning_rate
        self.gamma=discount_factor
        self.epsilon=e_greedy
        self.q_table=dict()
        self.file_path = os.path.dirname(os.path.abspath(__file__))


    def check_state_exist(self,state:tuple)->None:
        if state not in self.q_table:
            self.q_table[state]={act :0 for act in self.actions} #{'r':0,'l':0,'u':0,'d':0}

    def learn(self,last_observation:tuple,action,reward:int,next_observation:tuple,done:bool)->None:
        self.check_state_exist(last_observation)
        if not done:
            self.check_state_exist(next_observation)
        q_predict=self.q_table[last_observation][action]
        if done:
            self.q_table[last_observation][action]= q_predict + self.lr*(reward - q_predict)
        else:
            next_q = self.q_table[next_observation][max(self.q_table[next_observation])]
            self.q_table[last_observation][action] = q_predict + self.lr*(reward+self.gamma*next_q - q_predict)
    
    def choose_action(self,observation:tuple)->str:
        self.check_state_exist(observation)
        if np.random.uniform()>self.epsilon: 
            state_action =self.q_table[observation]
            action =max(state_action)
        else:
            action = np.random.choice(self.actions)
        return action
    