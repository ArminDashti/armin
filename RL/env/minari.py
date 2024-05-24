import minari


class make:
    def __init__(self, game='door-human-v2'):
        self.dataset = minari.load_dataset(game)
        
      
    @property
    def action_dim(self):
        return self.dataset[0].actions.shape
    
    
    @property
    def observation_dim(self):
        return self.dataset[0].observations.shape
    
    
    def get_dataset(self, generator=False):
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
                    sample['terminations'] = episode_data.terminations[step]
                    sample['truncations'] = episode_data.truncations[step]
                    sample['infos'] = episode_data.infos['success'][step]
                    episode.append(sample)
                episodes.append(episode)
                
        return episodes