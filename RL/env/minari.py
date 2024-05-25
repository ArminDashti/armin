import minari
from armin_utils.RL.modules.reply_memory import reply_memory


class make:
    def __init__(self, game='door-human-v2'):
        self.dataset = minari.load_dataset(game)
        
      
    @property
    def action_dim(self):
        return self.dataset[0].actions.shape[1:]
    
    
    @property
    def obs_dim(self):
        return self.dataset[0].observations.shape[1:]
    
    
    @property
    def time_steps_num(self):
        return self.dataset[0].total_timesteps
    
    
    @property
    def episodes_num(self):
        return (sum(1 for _ in self.dataset.iterate_episodes()))
    
    
    def raw_dataset(self, generator=False):
        if generator == True:
            return self.dataset.iterate_episodes()
        else:
            episodes = []
            for episode_data in self.dataset.iterate_episodes():
                
                episode = []
                for step in range(episode_data.total_timesteps):
                    sample = {}
                    sample['observations'] = episode_data.observations[step, :]
                    sample['actions'] = episode_data.actions[step]
                    sample['rewards'] = episode_data.rewards[step]
                    if (step == episode_data.total_timesteps-1):
                        sample['next_observations'] = episode_data.observations[step]
                    else:
                        sample['next_observations'] = episode_data.observations[step+1]
                    sample['terminations'] = episode_data.terminations[step]
                    sample['truncations'] = episode_data.truncations[step]
                    sample['infos'] = episode_data.infos['success'][step]
                    episode.append(sample)
                episodes.append(episode)
                
        return episodes
    
    
    def reply_memory(self):
        time_steps_num = self.time_steps_num
        episodes_num = self.episodes_num
        capacity = time_steps_num * episodes_num
        rm = reply_memory(capacity=capacity)
        
        dataset = self.raw_dataset()
        
        for episode in dataset:
            for step in episode:
                state = step['observations']
                action = step['actions']
                reward = step['rewards']
                terminations = step['terminations']
                truncations = step['truncations']
                infos = step['infos']
                if (terminations or truncations) == True:
                    done = True
                else:
                    done = False
                
                rm.push(state=state, action=action, reward=reward, done=done, next_state='')
                
        return rm